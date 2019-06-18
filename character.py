import re

# Create your Character class logic in here.
class Character:
    #initializer
    def __init__(self, char):
        if len(char) != 1:
            raise ValueError("Oops!! A character must contain only a single alphabet")
        else:
            #instance attribute to store a single character
            self.original = char
        #instance attribute to store a boolean value of whether or not if the letter has had been guessed or not
        self.was_guessed = False
        
    def update(self, guess):
        #check if the single character guessed by the user is a single character from a-z
        Character.check_char(guess)
        #update was_guessed to be true, if the guessed character is the exact match of original char
        if guess.lower() == self.original or guess.upper() == self.original:
            self.was_guessed = True
            return True
        else:
            return False
            
    def show(self):
        #to print the character if was_guessed is True
        if self.was_guessed == True:
            return self.original
        #else print '_'
        else:
            return '_'
    
    def reset(self):
        self.was_guessed = False
        
    @staticmethod
    def check_char(guess):
        pattern = r'^[a-zA-Z]$'
        regular_exp = re.compile(pattern)
        if not regular_exp.match(guess):
            raise ValueError("Oops!! A single character must be either from a-z or A-Z")
        
        
        