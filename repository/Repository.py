'''
Created on Jan 31, 2018

@author: Ale
'''
import random
from RepositoryException import *
class Repo:
    def __init__(self, fn):
        self.sentences = list()
        self.filename = fn
        self.loadFromFile()
        
    def loadFromFile(self):
        """
        Loads the data from the file
        output: None
        """
        try:
            file = open(self.filename, "r")
        
            for line in file:
                sentence = line
                self.sentences.append(sentence)
        
            file.close()
        except IOError as e:
            raise RepoException(str(e))
        
    def writeToFile(self):
        """
        Writes the list to the file
        output: None
        """
        try:
            file = open(self.filename, "w")
            for sentence in self.sentences:
                file.write(str(sentence))
            file.close()
        except IOError as e:
            raise RepoException(str(e))
        
    def add(self, sentence):
        self.sentences.append(sentence)
        self.writeToFile()
        
    def __str__(self):
        return str(self.sentences)
    
    def check(self, sentence):
        nr = 1
        c = 0
        for i in range(0, len(sentence)-1):
            if sentence[i] != ' ':
                c = 1
                j = i
                print(i)
                while sentence[j] != ' ' and j < len(sentence) - 1:
                    c = c + 1
                    j = j + 1
                i = j 
                #if c < 3:
                #    print(str(c) + str(j))
                #    return False
            elif sentence[i] == ' ' and sentence[i + 1] != ' ':
                nr = nr + 1
        if nr < 1:
            print(nr)
            return False
        return True
                
    def printList(self):
        for item in self.sentences:
            print(str(item))
            
    def chooseSentence(self):
        s = random.randint(0, len(self.sentences) - 1)
        return self.sentences[s]
    
    def printHangmanStyle(self, s):
        #s = self.chooseSentence()
        remember = list()
        new = ""
        new = new + s[0]
        remember.append(s[0])
        for character in range(1, len(s) - 1):
            if s[character] in remember:
                new = new + s[character]
            elif (s[character] != ' ' and s[character + 1] == ' ') or (s[character - 1] == ' ' and s[character] != ' '):
                new = new + s[character] 
                remember.append(s[character])
            elif s[character] != ' ':
                new = new + "_"
            else:
                new = new + " "
            character += 1
        new = new + s[len(s) - 1]
        return new
    
    def guess(self, letter, s):
        #s = self.chooseSentence()
        poz = list()
        found = False
        for char in range(0, len(s) - 1):
            if s[char] == letter:
                found = True
                poz.append(char)
        return (found, poz)
            
    def goodGuess(self, letter, poz, attempts, s):
        #s = self.chooseSentence()
        new = ""
        remember = list()
        new = new + s[0]
        remember.append(s[0])
        for character in range(1, len(s) - 1):
            if s[character] in remember:
                new = new + s[character]
            elif character in poz:
                new = new + letter
            elif s[character] in attempts:
                new = new + s[character]
            elif (s[character] != ' ' and s[character + 1] == ' ') or (s[character - 1] == ' ' and s[character] != ' '):
                new = new + s[character] 
                remember.append(s[character])
            elif s[character] != ' ':
                new = new + "_"
            else:
                new = new + " "
            character += 1
        new = new + s[len(s) - 1]
        return new

    def checkWin(self, new):
        for i in range(0, len(new) - 1):
            if new[i] == '_':
                return False
        return True
            
        
        
        
        
        
        