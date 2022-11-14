import string
from words import choose_word
from images import IMAGES

def ifvalid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return True

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word==get_guessed_word(secret_word,letters_guessed):
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


def get_available_letters(letter_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left = string.ascii_lowercase
    for i in letter_guessed:
        letters_left=letters_left.replace(i," ")
    return letters_left

def get_hint(secret_word,lett):
    import random
    letters_not_gussed=[] 
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_gussed:
                letters_not_gussed.append(i)

    return random.choice(letters_not_gussed) 

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
    print ("Welcome to the game, Hangman!")
    print(secret_word,'secret_wordsecret_world')
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    level=input("enter the level in which u want  to play:\n(a for  easy\n""(b)for  mwadium\n""(c)for  hard level:")
    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]


    if level == "b":
        total_lives=remaining_lives = 6
        image_selection = [0, 2, 3, 5, 6, 7]
    elif level == "c":
        total_lives=remaining_lives = 4
        image_selection = [1, 3, 5, 7]
    elif  level == "a":
        total_lives=remaining_lives = 8
        image_selection=[0,1,2, 3,4, 5,6,7]  
    else:
        if level!="a":
            print("your chioce is invalid")

    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter=="hint":
            print("your hint for the secret word is",get_hint(secret_word,letters_guessed))


        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
            print ("")

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print(IMAGES[image_selection[total_lives-remaining_lives]])
            remaining_lives-=1
            print("remaining_lives:"+str(remaining_lives))
            print("")
    else:
        print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)