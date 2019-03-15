'''
Created on Jan 31, 2018

@author: Ale
'''
from repository.Repository import Repo
from controller.Ctrller import Controller


class UI:
    def __init__(self, controller):
        self.controller = controller
        
    def start(self):
        while True:
            option = raw_input("Enter an option: ")
            
            if option == "1":
                print("You chose to add a sentence.")
                sentence = raw_input("Enter it: ")
                if self.controller.checkS(sentence) == True:
                    self.controller.addSentence(sentence)
                else:
                    print("Not a valid sentence")
            elif option == "2":
                attempts = list()
                k = 0
                hangman = "HANGMAN"
                h = ""
                print("You chose to start the game")
                s = self.controller.choose()
                new = self.controller.HangmanStyle(s)
                print(new)
                print("GAME ON")
                letter = raw_input("Your guess is: ")
                attempts.append(letter)
                result = self.controller.guesss(letter, s) 
                if result[0] == True:
                    new_output = self.controller.play(letter, attempts, s)
                    print(new_output)
                else:
                    h = h + hangman[k]
                    print("Try again" + h)
                    k = k + 1
                while k <= len(hangman):
                    letter = raw_input("Your guess is: ")
                    attempts.append(letter)
                    result = self.controller.guesss(letter, s)
                    if result[0] == True:
                        newnew_output = self.controller.play(letter, attempts, s)
                        print(newnew_output)
                        if self.controller.win(newnew_output) == True:
                            print("YOU WON")
                            break
                    else:
                        h = h + hangman[k]
                        print("Try again" + h)
                        k = k + 1
                    if h == "HANGMAN":
                            print("YOU LOST")
                            break
                        
            elif option == "5":
                self.controller.printAll()
            elif option == "0":
                print("Exited the program")
                break
            else:
                print("Not a valid option")


repo = Repo("sentences.csv")
controller = Controller(repo)
ui = UI(controller)
ui.start()