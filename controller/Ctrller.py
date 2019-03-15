'''
Created on Jan 31, 2018

@author: Ale
'''

class Controller:
    def __init__(self, sentences):
        self.sentences = sentences
        
    def addSentence(self, sentence):
        self.sentences.add(sentence)
        
    def printAll(self):
        self.sentences.printList()
        
    def choose(self):
        choose = self.sentences.chooseSentence()
        return choose
        
    def HangmanStyle(self, s):
        new  = self.sentences.printHangmanStyle(s)
        return new
        
    def guesss(self, letter, s):
        opt = self.sentences.guess(letter, s)
        return opt
    
    def play(self, letter, attempts, s):
        opt = self.sentences.guess(letter, s)
        result = self.sentences.goodGuess(letter, opt[1], attempts, s)
        return result

    def win(self, new):
        result = self.sentences.checkWin(new)
        return result
    
    def checkS(self, sentence):
        result = self.sentences.check(sentence)
        return result
        