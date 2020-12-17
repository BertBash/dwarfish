#!/usr/bin/env python3

def translate(eng, key0, key1):
    dwf =''
    i = 0
    j = 0

    while i < len(eng):
        while j < len(key0):
            t = key0[j]
            l = eng[i:i+len(t)].lower()
            if (l[0] >= 'a' and l[0] <= 'z'):
                if l == t:
                    #print("Matched!", t,l)
                    dwf += key1[j]
                    j = len(key0)
            else:
                dwf += l
                j = len(key0)
            j += 1
        j = 0
        i += len(t)
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
