#!/usr/bin/env python3

def translate(eng, key0, key1):
    dwf = ''
    for l in eng:
        if (l >= 'a' and l <= 'z'):
            i = key0.index(l.lower())
            dwf += key1[i]
        else:
            dwf += l
    return dwf

translationFile = 'dwarfKey.txt'
key0 = [' ']
key1 = [' ']

#Read in english
eng = raw_input('Give me a phrase!\n')

#Substitute the letters
with open(translationFile, 'r') as keyFile:
    for line in keyFile:
        key0.append(line.split()[0])
        key1.append(line.split()[1])

dwf = translate(eng, key0, key1)

#Output Dwarfish
print(dwf)
