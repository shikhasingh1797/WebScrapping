
import random 
def get_guessed_word(word, a):
    return a
name = input("What is your name?= ")
print ("Hello, " + name, "Time to play hangman!")
print("Start guessing...")
word = random.choice(["sec","app","dog"])
print(" random word --",word)
guesses = ""
def get_guessed_word(word,guesses):
    i = 0
    guessed_word = ""
    while (i< len(word)):
        if word[i] in guesses:
            guessed_word += word[i]
        else:
            guessed_word += "_"
        i=i+1
    return guessed_word
turns = 5
while turns > 0:         
    failed = 0
    guess=input("enter your guess=")
    letter=guess.lower()               
    if guess in word:
        guesses=guesses+guess
        print ("Good guess")
        print(get_guessed_word(word,guesses))
        if get_guessed_word(word,guesses)==word:      
            print ("You won")
            break
    if guess not in word:
        ("_")
        print("Ohhh this letter not in my word")                   
        turns -= 1        
        print ("You have", + turns, 'more guesses')
        if turns == 0:           
            print("You Lose")