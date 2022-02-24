import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    # word_list = ["navgurukul", "learning", "kindness"]
    with open("/home/navgurukul/Desktop/JSON/e-sreedharan-master/hangman/words.txt")as infile:
    # infile=open(word_file_name,"r")
       line=infile.readline()
       word_list=line.split()
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
    