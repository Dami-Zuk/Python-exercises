title = 'Fill in the correct forms.'
keyword = 'coding'
words = ['oct', 'float', 'date', 'input', 'print', 'program']
explanations = ['Integer number expressed with base 8', 'Decimal point number',
                'Python library for handling dates', 'Built-in function to read user\'s input to the program',
                'Prints text to console', 'Set of operations executed together']

print(f"{title :^100}\n{'_'*100}")

# Hidden words list with extra spaces to align the keyword vertically.
hidden_words = ["    _ C _", "  _ _ O _ _", "      D _ _ _", "      I _ _ _ _", "_ _ _ N _", "_ _ _ G _ _ _"]

# For loop to print explanations and CODING keyword.
count1 = 0
for explanation in explanations:
    print(f"{explanations[count1] :<60}{': ' :>10}{hidden_words[count1] :>5}")
    count1 += 1
print("\n")

# Using for loop to ask the user and save his inputs in user_input list for later comparison.
user_guess = []
for string in explanations:
    guess = input(f"{string :<60}{': ' :>10}")
    user_guess.append(guess.lower())
print('\n')

# For loop for checking if user inputs are correct.
count2 = 0
for check in words:
    if words[count2] == user_guess[count2]:
        print(f"{explanations[count2] :<60}{': ' :>10}{words[count2] :>8}")
    else:
        print(f"{explanations[count2] :<60}{': ' :>10}{hidden_words[count2] :>5}")
    count2 += 1

print('_'*100)

# Final check and a message to user - if all guesses are correct or not
if user_guess == words:
    print('You cracked it, good work!')
else:
    print('Check your answers and try again!')
