#-------------------------------------------------------------------------------
# Name:        Pyg Latin
# Purpose:     To translate English into Pig Latin.
#
# Author:      Alexander
#
# Created:     04/20/2012
# Copyright:   (c) Alexander 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def toPigLatin(string):
    a, b, c, d = '', '', '', ''
    q = string.split()
    p = ['th', 'Th', 'ch', "Ch", 'cr', 'Cr', 'tr', 'Tr', 'pr', 'Pr', 'st', 'St', 'al', 'Al', 'ph', 'Ph', 'qu', 'Qu']
    m = ['str', 'Str', 'scr', 'Scr']
    #l = ['and', 'And', 'are', 'Are', 'is', 'Is', 'am', 'Am', 'an', 'An']
    l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nonos = ['.', ',', '!', '?', '(', ')']

    for e in q:
        if e[-1] in nonos: #removes punctuation at end of string
            a = e[-1]
            e = e[:-1]

        if e[:2] in p:
            c = e[2:] + e[:2] + 'ay'
            b += c
            c = ''
        elif e[:3] in m:
			c = e[3:] + e[:3] + 'ay'
			b += c
			c = ''
        #elif e in l or len(e) == 1:
        #    c = e + 'ay'
        #    b += c
        #    c = ''
        elif e[0] in l:
            c = e + 'way'
            b += c
            c = ''
        else:
            c = e[1:] + e[:1] + 'ay'
            b += c
            c = ''

        if q[-1] == e:
            d += b + "."
        else:
            d += b + " "

        b = ''
    return d + a

again = "y"
while again == 'Y' or again == 'y':
    phrase = raw_input('Enter phrase to translate: ')
    print toPigLatin(phrase)
    again = raw_input('Translate again? (Y/N) ')