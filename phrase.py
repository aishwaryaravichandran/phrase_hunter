from character import Character
# Create your Phrase class logic here.
class Phrase:
    #initializer that recieves a phrase
    def __init__(self, phrase):
        
        character_list = []
        for each_character in phrase:
            character_list.append(Character(each_character))
        #attribute to hold the phrase parameter    
        self.phrase = character_list
        
    def show_phrase(self):
        #to print the phrase
        return ' '.join([c.show() for c in self.phrase])
    
    def reset_phrase(self):
        #to reset all the character of the phrase as not guessed
        for c in self.phrase:
            c.reset()
    
    def check_guess(self, guess):
        #to know if the entire phrase has been guessed
        correct = False
        for c in self.phrase:
            if c.update(guess) == True:
                correct = True
        return correct
            
                