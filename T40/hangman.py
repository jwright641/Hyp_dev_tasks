#  hangman challenge

import random

word_list = ['rarely', 'universe', 'notice', 'sugar', 'interference', 'constitution', 'we', 'minus', 'breath',
             'clarify', 'take', 'recording', 'amendment', 'hut', 'tip', 'logical', 'cast', 'title', 'brief', 'none',
             'relative', 'recently', 'detail', 'port', 'such', 'complex', 'bath', 'soul', 'holder', 'pleasant', 'buy',
             'federal', 'lay', 'currently', 'saint', 'for', 'simple', 'deliberately', 'means', 'peace', 'prove',
             'sexual', 'chief', 'department', 'bear', 'injection', 'off', 'son', 'reflect', 'fast', 'ago', 'education',
             'prison', 'birthday', 'variation', 'exactly', 'expect', 'engine', 'difficulty', 'apply', 'hero',
             'contemporary', 'that', 'surprised', 'fear', 'convert', 'daily', 'yours', 'pace', 'shot', 'income',
             'democracy', 'albeit', 'genuinely', 'commit', 'caution', 'try', 'membership', 'elderly', 'enjoy', 'pet',
             'detective', 'powerful', 'argue', 'escape', 'timetable', 'proceeding', 'sector', 'cattle', 'dissolve',
             'suddenly', 'teach', 'spring', 'negotiation', 'solid', 'seek', 'enough', 'surface', 'small', 'search']

#  opening text file and converting to list - read only
#  word_list_file = open("word_list.txt",'r')
#  word_list_file.seek(0)
#  content  = word_list_file.read()

#  content_list = content.split("\n")

#  word_list.extend(content_list)

#  print(word_list)

#  dictionary assigning value to each "hangman_states"

hangman_states = {0: '''
 ______
|
|
|
|
|
_______''', 1: '''
 ______
|     |
|
|
|
|
_______''', 2: '''
 ______
|     |
|     O
|
|
|
_______''', 3: '''
 ______
|     |
|     O
|     |
|
|
_______''', 4: '''
 ______
|     |
|     O
|    /|
|
|
_______''', 5: '''
 ______
|     |
|     O
|    /|\\
|
|
_______''', 6: '''
 ______
|     |
|     O
|    /|\\
|    /
|
_______''', 7: '''
 ______
|     |
|     O
|    /|\\
|    / \\
|
_______'''}

playing = True


# function to show the current state of hangman
def display_hangman(current_state):
    try:
        print(hangman_states[current_state])

    except:
        playing = False


def hidden_word(hangman_word):
    string = ""
    hangman_pos = 0
    for char in hangman_word:
        string += "*"
        hangman_pos += 1
    return string


def request_guess(hangman_word):
    guessing = True
    while guessing:
        player_input = (input("Please enter your next guess: ")).lower()
        # first check if player has guessed correct word
        if player_input == hangman_word:
            print("congratulations you win")
            return ("player wins")
        elif not player_input.isalpha():
            print("You did not enter a letter")
        elif len(player_input) != 1:
            print("Please select 1 letter")
        else:
            return player_input
            guessing = False


# check if letter is in word
def letter_check(hangman_word, letter):
    if letter in hangman_word:
        return letter


#  game logic

print("Welcome to hangman")

guess_count = 0

#  show the hangman status
display_hangman(guess_count)

#  computer randomly selects a word from the pre-determined list
hangman_word = random.choice(word_list)

#  tells player how many letters are in the word
print(f"The word has {len(hangman_word)} letters")

#  shows word with letters hidden using "*"
word_hidden = hidden_word(hangman_word)

#  temporarily included to show word
#  print(hangman_word)

letters_guessed = []

string = ""

while True:

    # request letter guess from player
    letter = request_guess(hangman_word)

    if letter == "player wins":
        playing = False
        break

    # print hidden word with guessed letters shown, updates letters for each new guess
    new_guessed_word = ""
    hangman_pos = 0
    for char in hangman_word:
        if char == letter:
            string += letter
        else:
            string += "*"
        hangman_pos += 1
    for index, char in enumerate(hangman_word):
        if char == letter:
            new_guessed_word += letter
        else:
            new_guessed_word += string[index]
    string = new_guessed_word

    # check if all letters have been guessed
    if "*" not in string:
        print("congratulations you win")
        playing = False
        break

    print(string)

    # increase guess count
    if letter not in hangman_word:
        guess_count += 1
        print("Letter is not in word")

    guesses_remaining = 7 - guess_count

    display_hangman(guess_count)

    letters_guessed.append(letter)

    # display letters guessed
    print(f"You have guessed the following letters: {letters_guessed}")
    print(f"You have {guesses_remaining} guesses remaining")

    if guesses_remaining == 0:
        print("you lose")
        playing = False
        break

print("game over")
