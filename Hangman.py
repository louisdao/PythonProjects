secret_word = ''

while True:

    secret_word = input('Please enter a word to be guessed\n'
                        'that does not contain ? or white space: ')
    secret_word = secret_word.strip()

    if not ('?' in secret_word or ' ' in secret_word or secret_word == ''):
        break

hangman = (
'\n'
' |',
'\n'
" |\n"
" 0",
'\n'
" |\n"
" 0\n"
" |",
'\n'
" |\n"
" 0\n"
"/|",
'\n'
" |\n"
" 0\n"
'/|\\\n',
'\n'
" |\n"
" 0\n"
"/|\\\n"
"/",
'\n'
" |\n"
" 0\n"
"/|\\\n"
"/ \\\n",
)

print("\n" * 31)
secret_word1 = ['?' * len(secret_word)]
print(''.join(secret_word1))
print('So far you have guessed: ')
hang_man = True

while hang_man:
    guess = None
    guessed_letters = []  # add all user guesses to this list
    blank_word = []  # replacing all letters of chosen word

    for letter in secret_word:
        blank_word.append('?')
        attempts = 7

    while attempts > 0:

        if attempts != 0 and "?" in blank_word and guessed_letters: #and guess not in '?' in guessed_letters:
            print("So far you have guessed: ", end='')
            guessed_letters.sort()
            print(", ".join(map(str, guessed_letters)))

        try:
            guess = str(input("Please enter your next guess: ")).lower()
        except:
            print("That is not valid input. Please try again.")
            continue

        else:
            if not guess.strip():
                print("You must enter a guess.")
                continue
            elif len(guess) > 1:
                print("You can only guess a single character.")
                continue
            elif guess in guessed_letters:
                print("You already guessed the character: %s" % guess)
                continue
            else:
                pass

            guessed_letters.append(guess)

            if guess not in secret_word:
                attempts -= 1
                print(hangman[(len(hangman) - 1) - attempts])
                print()
                while attempts in range(1,7):
                    print("".join(blank_word))
                    break
            else:
                searchMore = True
                startSearchIndex = 0

                while searchMore:
                    try:
                        foundAtIndex = secret_word.index(guess, startSearchIndex)
                        blank_word[foundAtIndex] = guess
                        startSearchIndex = foundAtIndex + 1

                    except:
                        searchMore = False

                if '?' in blank_word:
                    print()
                    print()
                    print("".join(blank_word))

            if attempts == 0:
                print("You failed to guess the secret word: {}".format(secret_word))
                hang_man = False
                break

            if "?" not in blank_word and attempts:
                print("You correctly guessed the secret word: {}".format(secret_word))
                hang_man = False
                break