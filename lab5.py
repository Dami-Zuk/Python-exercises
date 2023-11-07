def ask(word, user_input):
    return word == user_input


def prepare_puzzle(keyword, words):
    hwords = list(words)
    awords = list(words)
    empty = ' _ '
    max_field_len = max(map(len, words))
    for i, word in enumerate(words):
            pos = word.index(keyword[i])
            start = word[:pos]
            key = keyword[i].upper()
            end = word[pos+1:]
            awords[i] = f'{start:>{2*max_field_len}}{key:^3}{end}' 
            hwords[i] = f'{len(start)*empty:>{2*max_field_len}}{key:^3}{len(end)*empty}'
    return hwords, tuple(awords)


def print_puzzle(explanations, hwords, title=''):
    max_field_len = max(map(len, hwords))
    max_expl_len = max(map(len, explanations))
    print()
    print(f"{title :^175}")  # prints title
    print('_' * (3 + max_expl_len + 5 * max_field_len))  # prints the underlines
    for (explanation, hword) in zip(explanations, hwords):
        print(f'{explanation:<{max_expl_len}} {hword.upper()}')
    print('_' * (3 + max_expl_len + 5 * max_field_len))  # prints the underlines
    print()


def main():
    title = 'Fill in the correct forms.'
    puzzles = {
        1: {
            'keyword': 'python',
            'explanations': ('Outputs text to console',
                            'Describes how much space the value needs in the memory',
                            'Integer number',
                            'Integer number with base number 16',
                            'Decimal point number',
                            'Built-in function to read user\'s input to the program'),
            'words': ('print', 'type', 'int', 'hex', 'float', 'input')
        },
        2: {
            'keyword': 'editor',
            'explanations': ('Describes how much space the value needs in the memory',
                            'Python library for handling dates',
                            'Built-in function to read user\'s input to the program',
                            'Integer number',
                            'Decimal point number',
                            'Named place in program memory accessed with a name'),
            'words': ('type', 'date', 'input', 'int', 'float', 'variable')
        },
        3: {
            'keyword': 'coding',
            'explanations': ('Integer number expressed with base 8',
                            'Decimal point number',
                            'Python library for handling dates',
                            'Built-in function to read user\'s input to the program',
                            'Prints text to console',
                            'Set of operations executed together'),
            'words': ('oct', 'float', 'date', 'input', 'print', 'program')
        }
    }

    for key, value in puzzles.items():
        print()
        while True:
            #  getting single puzzle from the dictionary
            keyword = value['keyword']
            explanations = value['explanations']
            words = value['words']
            hwords, awords = prepare_puzzle(keyword, words)

            print_puzzle(explanations, hwords, title)

            for i, (explanation, word) in enumerate(zip(explanations, words)):
                if ask(word, input(f'{explanation:<{max(map(len, explanations))}}: ')): 
                    hwords[i] = awords[i]

            print_puzzle(explanations, hwords)

            if tuple(hwords) == awords:
                print('You cracked it, good work!')
                break
            else:
                if input('Do you want to try again [Y|N]?').upper() == 'Y' or 'YES':
                    continue
                else:
                    break
    else:
        print()
        print('That was all, there are no more puzzles!')


if __name__  == '__main__':
    main()