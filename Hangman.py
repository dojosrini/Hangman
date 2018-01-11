# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 11:32:45 2018

@author: dojosrini
"""
import random
from PyDictionary import PyDictionary
def randomWord():
    word = ['test','program']
    choice = random.choice(word)
    return choice
def builddashes(word,chtomask):
    s = list(chtomask)
    for i in range(0,len(s)):
        word = word.replace(s[i],'-')
    return word
    
def main():
   print "Welcome to Hangman"
   dictionary=PyDictionary()
   while True: 
    word = randomWord()
    print(word)
    print (dictionary.meaning(word))
    mask = list(set(word))
    output = builddashes(word,mask)
    print "Here's your word"
    print output
    trial = list("HANGMAN")
    counter = 0
    while True:
        while True:
            text = raw_input("guess a character :")
            if text.isalpha() & len(text) == 1:
                break
        if mask.__contains__(text.lower()):
            mask.remove(text.lower())
        else:
            counter = counter + 1 
        output = builddashes(word,mask)
        print output
        print '\033[1m' +''.join(trial[:counter]) + '\033[1m'
        if counter >= len(trial):
            break
        if word == output:
           print("Well done, You Won !!!")
           break
    print("Game Over !!!")    
    print (word)
    play_again = raw_input("Do you want to play again? (n to stop)")
    if play_again.lower() == 'n':
       break
            
if __name__ == "__main__":
    main()


