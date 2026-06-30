from random import randint
import re 
from hangman_art import HANGMANPICS

#hangman class object

class Hangman():
    def __init__(self):
        self.word = choose_word()
        self.guesses_left_counter = 6 
        self.revealed_letters = ['_','_','_','_','_']
        self.guessed = []
        self.current_guessed_letter = ''
        print("Welcome to hangman! Let's Play!!!\n")


##innit functions
def choose_word():
    """Chooses word for user to guess from random txt file"""
    random_seed = randint(0,49)
    word_path = 'python projects/hangman_remade/hangman_words.txt'
    with open(word_path) as opened_words:
        word_list = opened_words.read()
    
    word_list = word_list.split(',')

    return(word_list[random_seed].upper())


#user input response recording
def get_user_input(rev_list, guess_list):
    while True:
        output = input("please select a letter: \n")
        if len(output)==1:
            if output.upper() in rev_list or output.upper() in guess_list:
                print(f'You already guessed the letter {output.upper()}')
            elif re.search("[a-zA-Z]", output) is not None:
                    return(output.upper())
            else:
                print('invalid input, please selecter a letter')
        else:
            print('invalid input, please input a single letter.\n')


## letter assessment list
def compare_chosen_letter_against_list(letter,revealed_letters,word_list):
    if letter not in word_list:
        return(revealed_letters)
    else:
        for x in range(0,5):
            if word_list[x] == letter:
                revealed_letters[x] = letter
        return(revealed_letters)

def get_wrong_letters_list(inlist, letter,word):
    if letter not in word:
        inlist.append(letter)
    else:
        return(inlist)

### game over checks 
def check_game_over(guess_count, revealed_letters):
    if  '_' not in revealed_letters:
        return 'Won' 
    elif guess_count == 0:
         return 'Lost' 
    else: return 'Continue'

def game_over_message(result, word):
    if result == 'Won':
        return(f"You guessed the word {word} right, you won!")
    elif result == 'Lost':
        return(f"You have no turns left, game over, you lost, the word was {word}\n\nFinal Hangman Status:\n {HANGMANPICS[0]}\n")
    



def play_Hangman():
    hangman_game = Hangman()

    while True:
        print('========= N E W  T U R N ============')
        print(f'Current Hangman Status:\n {HANGMANPICS[hangman_game.guesses_left_counter]}\n')
        print(f'Revealed Letters: {hangman_game.revealed_letters}')
        print(f'Incorrectly Guessed Letters: {hangman_game.guessed}\n')
        placeholder_revealed_letters = hangman_game.revealed_letters[:]
        print(f'You have {hangman_game.guesses_left_counter} guess(es) left')

        user_letter = get_user_input(hangman_game.revealed_letters,hangman_game.guessed)
        get_wrong_letters_list(hangman_game.guessed, user_letter, hangman_game.word)
        hangman_game.revealed_letters = compare_chosen_letter_against_list(user_letter, hangman_game.revealed_letters, hangman_game.word)
        
        if placeholder_revealed_letters == hangman_game.revealed_letters:
            hangman_game.guesses_left_counter =  hangman_game.guesses_left_counter - 1 
            print(f'\n\n\nThe letter {user_letter} was not in the word :( \n')
        else: 
            print(f'\n\n\nThe letter {user_letter} was  in the word :D \n')
    


        game_check = check_game_over(hangman_game.guesses_left_counter, hangman_game.revealed_letters )

        if game_check != 'Continue': 
            print(game_over_message(game_check, hangman_game.word))
            
            break







if __name__ == '__main__':

    play_Hangman()

