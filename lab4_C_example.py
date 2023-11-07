'''
print crossword puzzle from explanations and words showing a keyword, _ replaces other letters
than what are in the keyword
e.g.
words:

   print
  type
 int
   hex
 float  
  input
  
are printed:
                            Fill in the correct terms                             
__________________________________________________________________________________
Outputs text to console                                          P  _  _  _  _ 
Describes how much space the value needs in the memory        _  Y  _  _ 
Integer number                                             _  _  T 
Integer number with base number 16                               H  _  _ 
Decimal point number                                       _  _  O  _  _ 
Built-in function to read user's input to the program         _  N  _  _  _ 
'''

# required variables
title = "Fill in the correct terms"
puzzles = {
    1:{
    'keyword' : 'python' ,
    'explanations' : ('Outputs text to console', \
               'Describes how much space the value needs in the memory', \
               'Integer number', \
               'Integer number with base number 16', \
               'Decimal point number', \
               'Built-in function to read user\'s input to the program'),
    'words' : ('print', 'type', 'int', 'hex', 'float', 'input')
    },
    2: {
    'keyword' : 'editor',
    'explanations' : ('Describes how much space the value needs in the memory',\
               'Python library for handling dates', \
               'Built-in function to read user\'s input to the program', \
               'Integer number',  \
               'Decimal point number', \
               'Named place in program memory accessed with a name'),
    'words' : ('type', 'date', 'input', 'int', 'float', 'variable')
    },
    3:{
    'keyword' : 'coding',
    'explanations' : ('Integer number expressed with base 8', \
               'Decimal point number', \
               'Python library for handling dates', \
               'Built-in function to read user\'s input to the program', \
               'Prints text to console', \
               'Set of operations executed together'),           
    'words' : ('oct', 'float', 'date', 'input', 'print', 'program')
    }
    }

#  loop through puzzles
for key, value in puzzles.items():
    print()
    while True:
        #  extract individual puzzles
        keyword = value['keyword']
        explanations = value['explanations']
        words = value['words']
        hwords = ['']*len(words) #  list of formatted hidden words
        awords = ['']*len(words) #  list of formatted actual words, later changed to a tuple

        empty = ' _ '
        max_expl_len = max(map(len, explanations))
        max_field_len = max(map(len, words))
        result = True

        for i, word in enumerate(words):
            #  get the key position in a word and slice the word
            pos = word.index(keyword[i])
            start = word[:pos]
            key = keyword[i].upper()
            end = word[pos+1:]
            awords[i] = f'{start:>{2*max_field_len}}{key:^3}{end}' 
            hwords[i] = f'{len(start)*empty:>{2*max_field_len}}{key:^3}{len(end)*empty}'
        awords = tuple(awords) #  immutable

        # print the puzzle
        print()
        print(f'{title:^{max_expl_len + 5 * max_field_len}}') #  title
        print('_'* (3 + max_expl_len + 5 * max_field_len))  #  underline
        for (explanation, hword) in zip(explanations, hwords):
            print(f'{explanation:<{max_expl_len}} {hword}')
        print('_'* (3 + max_expl_len + 5 * max_field_len))  #  underline
        print()

        #  ask line by line the correct words and add aword to hwords if correct
        for i, (explanation, word) in enumerate(zip(explanations, words)):
            if word == input(f'{explanation:<{max_expl_len}}: '):
                hwords[i] = awords[i]

        # print the puzzle
        print()
        print('_'* (3 + max_expl_len + 5 * max_field_len))  #  underline
        for (explanation, hword) in zip(explanations, hwords):
            print(f'{explanation:<{max_expl_len}} {hword}')
        print('_'* (3 + max_expl_len + 5 * max_field_len))  #  underline
        print()

        #  final result, re-do the puzzle or go to the next
        if tuple(hwords) == awords:
            print('You cracked it, good work!')
            break
        else:
            if input('Do you want to try again [Y|N]?').upper() == 'Y':
                continue
            else:
                break

#  the loop was executed successfully          
else:
    print()
    print('That was all, there are no more puzzles!')








