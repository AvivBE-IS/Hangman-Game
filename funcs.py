from art_constants import *

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function returns False in the following cases:
    If the letter_guessed string consists of two or more characters
    If the string letter_guessed contains a sign that is not an English letter (like: &, *)
    If the letter_guessed string is a character already in the old_letters_guessed list.
    That is, this character has been guessed before and therefore it is illegal to guess it again).
    The function returns True if the string letter_guessed consists of only one letter that is an English letter (and not another letter)
    that is not in the list old_letters_guessed (that is, this letter has not been guessed before).
    :param letter_guessed: A string representing the character received from the player.
    :param old_letters_guessed: A list containing the letters the player has guessed so far.
    :return: A Boolean value representing the string's correctness and whether the user has already guessed the character before
    """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


# The join function is one of the simplest methods to convert a list to a string in python. The main point to keep in
# mind while using this function is that the join function can convert only those lists into string that contains
# only string as its elements. Now, there may be a case when a list will contain elements of data type other than
# string. In this case, The join function can not be used directly. For a case like this, str() function will first
# be used to convert the other data type into a string and then further, the join function will be applied. Refer to
# the example given below to understand clearly.

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    If the character is correct, the function will add the letter_guessed character to the old_letters_guessed list.
    It will then return a true value
    If the character is incorrect, the function will print the character X and below it the list old_letters_guessed.
    The list will printed as a string of lowercase letters sorted from the smallest to the largest and separated from each other by arrows.
    The printing of the organs is to remind the player which characters he has already guessed.
    At the end, the function will return a False, which means that it is not possible to add the character to the list of already guessed characters.
    :param letter_guessed: A string representing the character received from the player.
    :param old_letters_guessed: A list containing the letters the player has guessed so far.
    :return: A boolean value.
    """
    while not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        print(show_old_letters_guessed(old_letters_guessed))
        letter_guessed = input("Invalid input. Please try again--> ")
    old_letters_guessed.append(letter_guessed.lower())
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function shows the player his progress in guessing the secret word.
    :param secret_word: A string representing the secret word that the player must guess. :param old_letters_guessed:
    A list containing the letters the player has guessed so far. :return: The function returns a string consisting of
    letters and underscores. The string shows the letters from the old_letters_guessed list that are in the
    secret_word string in their appropriate position, and the other letters in the string (which the player has not
    yet guessed) as underlines.
    """
    temp_string = ''
    letter_found = False
    for letter in secret_word[1]:
        for letter_guessed in old_letters_guessed:
            if letter == letter_guessed:
                temp_string += letter + ' '
                letter_found = True
                break
        if not letter_found:
            temp_string += "_ "
        letter_found = False
    return temp_string


def check_win(secret_word, old_letters_guessed):
    """
    A function that checks whether the player managed to guess the secret word and thus won the game.
    :param secret_word: The string represents the secret word that the player must guess.
    :param old_letters_guessed: A list containing the letters the player has guessed so far.
    :return: The function returns true if all the letters that make up the secret word are included in the list of letters that the user guessed. Otherwise, the function returns false.
    """
    for letter in secret_word[1]:
        if letter not in old_letters_guessed:
            return False
    return True


def print_hangman(num_of_tries):
    """
    Print one of the hangman status images, depending on the number of wrong guesses the player made.
    :param num_of_tries: Represents the number of failed attempts by the user so far.
    :return: None.
    """
    print(HANGMAN_PHOTOS.get("pic" + str(num_of_tries)))


def choose_word(file_path, index):
    """
    Choosing a secret word for the player from a text file containing a list of words separated by spaces.
    :param file_path: A string representing a path to the text file.
    :param index: An integer representing the position of a particular word in the file.
    :return: A function returns a tuple consisting of two members in the following order:
    The number of different words in the file, i.e. not including repeated words. A word in the position received as an
    argument to the function (index), which will be used as the secret word for guessing.
    """
    with open(file_path, "r") as secret_word_file:
        # The file must have one line and no punctuation marks.
        content = secret_word_file.read()
        words = content.split()
        if index > len(words):
            index %= len(words)
            # If the position (index) is greater than the number of words in the file,
            # the function continues to count positions in a circular fashion.
        return len(set(words)), words[index - 1]
    # The player enters as starting from 1 (and not from zero).


def welcome():
    """
    Printing the opening page.
    :return: None.
    """
    print(f'{HANGMAN_ASCII_ART}\n{MAX_TRIES}')
    print_hangman(1)


def get_secret_word():
    """
    Get secret word.
    Firstly getting 2 inputs from the user. Then calling the function 'choose_word'.
    choose_word getting a word from the file according the given index.
    :return: secret word.
    """
    file_path = input("Please enter file path to the words file--> ")
    # Enter words.txt
    word_index = input("Please enter word index--> ")
    return choose_word(file_path, int(word_index))


def show_old_letters_guessed(old_letters_guessed):
    """

    :return:
    """
    if len(old_letters_guessed) == 0:
        return "No previous guesses."
    return "Old letters guessed: " + '-> '.join(sorted(old_letters_guessed))


def show_how_tries_left(num_of_tries):
    tries_left = MAX_TRIES - num_of_tries + 1
    if tries_left == 1:
        return "It's your last try. Be careful."
    elif tries_left == 0:
        return "LOSE"
    else:
        return str(tries_left) + " tries left."

