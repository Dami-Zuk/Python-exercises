title = 'Fill in the correct forms.'
keyword = 'coding'
words = ('oct', 'float', 'date', 'input', 'print', 'program')
explanations = ('Integer number expressed with base 8', 'Decimal point number',
                'Python library for handling dates', 'Built-in function to read user\'s input to the program',
                'Prints text to console', 'Set of operations executed together')

print(' '*34, title, '\n', '_'*100)

print(explanations[0], ' '*42 + '_', words[0][1].upper(), '_')
print(explanations[1], ' '*56 + '_ _', words[1][2].upper(), '_ _')
print(explanations[2], ' '*46, words[2][0].upper(), '_ _ _')
print(explanations[3], ' '*26, words[3][0].upper(), '_ _ _ _')
print(explanations[4], ' '*52 + '_ _ _', words[4][3].upper(), '_')
print(explanations[5], ' '*39 + '_ _ _', words[5][3].upper(), '_ _ _')

a = input(explanations[0] + ' '*43 + ': ')
b = input(explanations[1] + ' '*59 + ': ')
c = input(explanations[2] + ' '*46 + ': ')
d = input(explanations[3] + ' '*26 + ': ')
e = input(explanations[4] + ' '*57 + ': ')
f = input(explanations[5] + ' '*44 + ': ')

print('\n')

if a == words[0]:
    print(explanations[0], ' '*43, words[0].upper())
else:
    print(explanations[0], ' '*41, '_', words[0][1].upper(), '_')

if b == words[1]:
    print(explanations[1], ' '*59, words[1].upper())
else:
    print(explanations[1], ' '*55, '_ _', words[1][2].upper(), '_ _')

if c == words[2]:
    print(explanations[2], ' '*46, words[2].upper())
else:
    print(explanations[2], ' '*46, words[2][0].upper(), '_ _ _')

if d == words[3]:
    print(explanations[3], ' '*26, words[3].upper())
else:
    print(explanations[3], ' '*26, words[3][0].upper(), '_ _ _ _')

if e == words[4]:
    print(explanations[4], ' '*57, words[4].upper())
else:
    print(explanations[4], ' '*51, '_ _ _', words[4][3].upper(), '_')

if f == words[5]:
    print(explanations[5], ' '*44, words[5].upper())
else:
    print(explanations[5], ' '*38, '_ _ _', words[5][3].upper(), '_ _ _')

print('_'*100)

if a == words[0] and b == words[1] and c == words[2] and d == words[3] and e == words[4] and f == words[5]:
    print('You cracked it, good work!')
else:
    print('Check your answers and try again!')
