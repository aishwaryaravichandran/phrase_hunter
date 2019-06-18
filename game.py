# Create your Game class logic in here.
from phrase import Phrase

import random

class Game:
    
    def __init__(self, phrases):
        #maximum no.of guesses allowed
        self.lives = 5
        #list of all possible phrases
        self.phrases = [Phrase(phrase) for phrase in phrases]
        #current phrase to be guessed by the user
        self.current_phrase = random.choice(self.phrases)
        
    def start_game(self):
        guesses = []
        incorrect_guesses = []
        
        while True:
            phrase = self.current_phrase.show_phrase()
            print(phrase)
            #get input from user for a guess of character 
            guess = input("Guess a character: ")
            #if the guess is already guessed, print a message that it is already guessed
            if guess in guesses:
                print("You have already guessed {}".format(guess))
                continue
            #check if the guessed character is a single character, not a number and is in the current phrase    
            try:
                correct = self.current_phrase.check_guess(guess)
            except ValueError:
                print("Oops!! You must guess a character from a-z or A-Z")
                continue
            #append the guess into a list of guesses    
            guesses.append(guess)
            #if the guess is not correct, append the guess into a list of incorrect guesses
            if not correct:
                print("Oops!! Wrong guess :/")
                incorrect_guesses.append(guess)
                #The user loses game if the length of incorrect guesses is greater than or equal to lives
                if len(incorrect_guesses) >= self.lives:
                    print("Oh No!! You have run out of guesses..You lose :( ")
                    #ask the user if the game wants to be replayed
                    replay = input("Would you like to play the game again?? y/n ")
                    #if yes, reset and start game
                    if replay.lower() == 'y':
                        self.new_game()
                        self.start_game()
                        break
                    #else break
                    else:
                        print("Thanks for playing. See you until next time")
                        break
            #if there are no more '_' in the current phrase, 
            #the user wins and asked if the game wants to be replayed            
            if '_' not in self.current_phrase.show_phrase():
                print(self.current_phrase.show_phrase())
                print("Hurrayy!! You got it..You won the game!!")
                replay = input("Would you like to play the game again?? y/n ")
                if replay.lower() == 'y':
                    self.new_game()
                    self.start_game()
                    break
                else:
                    print("Thanks for playing. See you until next time")
                    break
            #let the user know how many lives are remaining
            print("You have {} more lives left of total {} lives".format(self.lives - 
                                                                         len(incorrect_guesses), self.lives))
            
    def new_game(self):
        #reset all the characters in each phrase as not guessed
        for phrase in self.phrases:
            phrase.reset_phrase()
        #select a random phrase as the current phrase for the user to find
        self.current_phrase = random.choice(self.phrases)
        
        
                    
                    
                    
                         
                          
            