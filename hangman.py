import string
from words import choose_word
from images import IMAGES


# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == (get_guessed_word(secret_word, letters_guessed)):
      return True
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    # import string
    all_letters = string.ascii_lowercase
    # letters_left = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
          letters_left += letter
    return letters_left



def ifValid(user_input):

    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False

def get_hint(secret_word, letters_guessed):

    '''
    secret_word: ek string word jo ki user ko guess karna hai

    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai

    returns: ek character jo abhi tak guess nahi hua hai

    '''


    import random

    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):

        letter = secret_word[index]

        if letter not in letters_guessed:

            if letter not in letters_not_guessed:

                letters_not_guessed.append(letter)


        index += 1


    return random.choice(letters_not_guessed)




    # True humne tab hi return kiya hai jab

    # user_input ki length 1 hai aur woh character hai

    return True

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print( "....Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    user_difficulty_choice = input("ON WHICH DIFFICULTY YOU WANY TO PLAY?=\na)\tEASY..\nb)\tMEDIUM..\nc)\tHARD..\n\n...CHOOSE YOUR CHOICE IN --a--b--c--\n=")
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]


    if user_difficulty_choice not in ["a", "b", "c"]:

        # print ("YOUR CHOICE IS INVALID.\n..YOU CAN START YOUR GAME IN EASY MODE..")
        pass


    else:

        if user_difficulty_choice == "b":

            total_lives = remaining_lives = 6

            images_selection_list_indices = [0, 2, 3, 5, 6, 7]


        elif user_difficulty_choice == "c":

            total_lives = remaining_lives = 4

            images_selection_list_indices = [1, 3, 5, 7]


    remaining_lives = 8

    while(remaining_lives > 0):
      available_letters = get_available_letters(letters_guessed)
      print ("..AVALIABLE LETTERS..= " + available_letters)
      
      guess =input("PLEASE GUESS THE LETTERS=")
      # letter = guess.lower()
      if guess == "hint":
        letter = get_hint(secret_word, letters_guessed)

      else:
        letter = guess.lower()
        if (ifValid(letter)):
          continue


      if letter in secret_word:
        letters_guessed.append(letter)
        print ("YEAHH...GOOD GUESS...🥳" + get_guessed_word(secret_word, letters_guessed))
        print ("")

        if is_word_guessed(secret_word, letters_guessed) == True:
            print (" * *🥳....CONGRATULATIONS YOU WON...🥳* * ")
            print ("")
            break

      else:
        print ("OOPS THIS WORD NOT IN MY WORD....SRY,,,😩" + get_guessed_word(secret_word, letters_guessed))
        # print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]]) ## <-- CHANGES HERE

        print (IMAGES[8-remaining_lives])
        print ("REMAINING LIVES=: ", remaining_lives)
        print("")
        letters_guessed.append(letter)
        remaining_lives -= 1
    else:
      print ("SORRY,🚷 YOU RUN OUT OF GUESS. THE WORD WAS... " + str(secret_word) + ".")
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
    


