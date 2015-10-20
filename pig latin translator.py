def toPigLatin(string):
    a, b, c, d = '', '', '', ''
    q = string.split()
    print q
    nonos = [' ', '.', ',', '!', '?', '(', ')']
    for e in q:
        print e
        for i in e:
            if i not in nonos:
                a += i
            else:
                if a[:2] == 'th' or a[:2] == 'Th' or a[:2] == 'ch' or a[:2] == 'Ch' or a[:2] == 'cr' or a[:2] == 'Cr' or a[:2] == 'tr' or a[:2] == 'Tr' or a[:2] == 'pr' or a[:2] == 'Pr' or a[:2] == 'st' or a[:2] == 'St' or a[:2] == 'str' or a[:2] == 'Str':
                    c = a[2:] + '-' + a[:2] + 'ay'
                    b += c + ' '
                    a = ''
                    c = ''
                elif a == 'and' or a == 'And':
                    c = a + '-ay'
                    b += c + ' '
                    a = ''
                    c = ''
                elif a == 'are' or a == 'Are':
                    c = a + '-ay'
                    b += c + ' '
                    a = ''
                    c = ''
                else:
                    c = a[1:] + "-" + a[:1] + 'ay'
                    b += c + ' '
                    a = ''
                    c = ''
            d += b
            b = ''
    return d
