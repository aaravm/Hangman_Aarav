count = 0
lives = 6
invalid_lives = 5
words = []
guessed = []
win = -1
print("Instructions")
print("1. All answers are in the form letters only. Don't use numbers or any special characters.")
print("2. All letters are lowercase")

from art import *

tprint("hangman")


def drawings(guesses):
    if guesses == 6:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")

        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\\|")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif guesses == 0:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\\|/")
        print("|	 |")
        print("|	/ \\ ")
        print("|________")


file = open("wordlist.txt", "r")
lines = len(file.readlines())
file.seek(0)
for i in range(lines):
    word_from_file = file.readline()
    words.append(word_from_file.rstrip('\n'))

file.close()


def play_hangman():
    global lives, win, invalid_lives
    import random
    ran_num = random.randint(0, lines - 1)
    word = words[ran_num]
    len_word = len(word)
    guess = []
    for j in range(0, len_word):
        guess.append('_ ')
    print("Initial word is:")
    for j in range(0, len_word):
        print(guess[j], end=" ")
    while lives > 0 or invalid_lives > 0 or win == 1:
        a = input("\nGuess a letter ")
        if a in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']:
            if a in guessed:
                print("word already guessed")
                print("current word is:")
                for j in range(0, len_word):
                    print(guess[j], end=" ")
            else:
                guessed.append(a)
                if a in word:
                    for j in range(0, len_word):
                        if word[j] == a:
                            guess[j] = a
                    if '_ ' not in guess:
                        print(guess[j], end=" ")
                        tprint("YOU WIN!!!")
                        win = 1
                        break
                    for j in range(0, len_word):
                        print(guess[j], end=" ")
                else:
                    lives = lives - 1
                    if lives == 0:
                        drawings(lives)
                        tprint("You Lose :(")
                        print("The correct word was", word)
                        win = 1
                        break
                    else:
                        drawings(lives)
                        print("lives left =", lives)
                        print("current word is:")
                        for j in range(0, len_word):
                            print(guess[j], end=" ")
        else:
            print("Enter a valid letter")
            invalid_lives = invalid_lives - 1
            if invalid_lives == 0:
                drawings(lives)
                tprint("You Lose :(")
                print("The correct word was", word)
                win = 1
                break
            else:
                print("Invalid lives left =", invalid_lives)
                print("current word is:")
                for j in range(0, len_word):
                    print(guess[j], end=" ")


play_hangman()
while True:
    inp = input("Do you want to play again?(y/n)")
    if inp == 'y' or inp == 'Y':
        count = 0
        lives = 6
        invalid_lives = 5
        win = -1
        guessed = []
        play_hangman()
    else:
        break
