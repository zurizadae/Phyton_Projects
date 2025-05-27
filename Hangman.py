import random 
word_bank = ['ability', 'challenge', 'journey', 'success', 'victory', 'food', 'friendship', 'happiness', 'knowledge', 'wisdom', 'courage', 'strength', 'growth', 'adventure', 'dreams','cat','star','moon','sun','sky','ocean',
             'forest','mountain','river','lake','desert','island','city','village','country','world','nature','beauty','art','music','dance','poetry','literature','science','technology','history','culture','language']
global attempts
attempts = 6

def choose_word():
    word = random.choice(word_bank)
    guessedWORD = ['_']*len (word)
    return word, guessedWORD

def restart_game():
    print("\nDo you want to play again? (yes/no)")
    choice = input().lower()
    if choice == 'yes':
        global attempts
        attempts = 6
        print("Starting a new game...\n")
        # Reinitialize the game with a new word
        global word, guessedWORD
        global word_bank
        random.shuffle(word_bank)
        main()  # Restart the main game function
        # Choose a new word from the shuffled word bank

        word, guessedWORD = choose_word()
        return word, guessedWORD
    elif choice == 'no':
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return restart_game()
    
def display_hangman():
    stages = [  
                # Initial empty state
                '''
                   -----
                   |   |
                   |   
                   | 
                   |  
                   -
                ''',
                # Head
                '''
                   -----
                   |   |
                   |   O
                   |  
                   |  
                   -
                ''',
            
                # Head & torso
                '''
                   -----
                   |   |
                   |   O
                   |   |
                   |  
                   -
                ''',        
                # Head, torso, one arms
                '''
                   -----
                   |   |
                   |   O
                   |  /|
                   |
                   -
                ''',
                # Head, torso, both arms
                '''
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |
                   -
                ''',
                # Head, torso, both arms, one leg
                '''
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  /
                   -   
                ''',
                # Head, torso, both arms, both legs
                '''
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  / \\
                   -
                ''']
    return stages[6 - attempts]

def used_letter(letter):
    global letter_bank
    if letter in letter_bank:
        print("You have already used this letter. Try another one.")
        return letter_bank
    
    letter_bank.append(letter)
    return letter_bank

def print_used_letters(guessedWORD):
    print("-------------------------------------------------------------------------------------------------")
    print("Used letters: ", ' '.join(letter_bank))  # joins the strings in letter_bank with a space
    print("-------------------------------------------------------------------------------------------------")

def main():
    global attempts
    global word, guessedWORD
    global letter_bank
    word, guessedWORD = choose_word()
    letter_bank = []
    
    while attempts > 0:
        print("\nCurrent word: ", ' '.join(guessedWORD)) # joins the strings in guessedWORD with a space
        print(display_hangman())
        print_used_letters(guessedWORD)
        guess = input("Enter a letter: ").lower()
        letter_bank = used_letter(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWORD[i] = guess
                    print('Great guess!')
        else:
            attempts -= 1
            print("Incorrect guess. Attempts left: " + str(attempts))

        if '_' not in guessedWORD:
            print("\nCurrent word: ", ' '.join(guessedWORD)) # joins the strings in guessedWORD with a space
            print(display_hangman())
            print_used_letters(guessedWORD)
            print('\nCongratulations!!! You guessed the word: ' + word)
            restart_game()

    else:
        print(display_hangman())
        print("\nSorry, you've run out of attempts. The word was: " + word)
        restart_game()

print("Welcome to Hangman!\n")
print("You have 6 attempts to guess the word.\n")
main()