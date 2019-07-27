import random

ROUNDS = 10
MAGENTA = "magenta"
WHITE = "white"
PURPLE = "purple"
YELLOW = "yellow"
GREEN = "green"
ORANGE = "orange"
NUM_SLOTS = 4
COLORS_LIST = ["magenta", "white", "purple", "yellow", "green", "orange"]
RED = 'Red'
BLACK = 'Black'
UNKNOWN = "Unknown"

class Game:
    
    def __init__(self):
        self.rounds = ROUNDS
        self.grades = []
        self.guesses = []
        self.secret = self.enterSecret()
        if self.secret == False:
            print("Quitting the game.")
            return
    
    def continueGame(self):
        while(True):
            currentRound = ROUNDS - self.rounds + 1
            if currentRound == ROUNDS + 1:
                print(f"You have used up all {ROUNDS} number of rounds of guesses. Game over! Try again?")
                return
            print(f"This is the {currentRound} round to guess.")
            self.rounds -= 1
            
            if self.guesses != []:
                print("Printing your previous guesses.")
                for i in range(len(self.guesses)):
                    print(f"This was guess # {i + 1} you made earlier.")
                    print(self.guesses[i])
            
            if self.grades != []:
                print("Printing your previous guesses graded.")
                for i in range(len(self.grades)):
                    print(f"This was graded guesss # {i + 1} you made earlier.")
                    print(self.grades[i])
                    
            guess = self.parser(False)
            if guess == False:
                print("Quitting the game.")
                return
            results = self.gradeTry(guess)
            
            print("This is the current result of your guess.")
            print("Red means one of your guesses color is the same as some other color in the secret code.")
            print("Black means one of your guesses is exactly the same color and position as in the secret code.")
            print("Unknown is a filler, and means your guess is not the same color or position.")
            print(results)
            self.guesses.append(guess)
            self.grades.append(results)
            
            winCondition = self.checkAllCorrect(results)
            if winCondition:
                print("You have guessed all the colors correct! You win!")
                return
            else:
                print("At least one of the positions is incorrect. Keep Trying.")
            
        
    
    def gradeTry(self, row):
        secret = self.secret
        samePosAndColor = 0
        places = []
        for i in range(4):
            if (row[i] == secret[i]):
                samePosAndColor += 1
                places.append(i)
                
        newRow = []
        newSecret = []
        for i in range(4):
            if i not in places:
                newRow.append(row[i])
                newSecret.append(secret[i])
        
        sameColor = 0
        newRowLength = len(newRow)
        newSecretLength = len(newSecret)
        secretIndex = []
        for i in range(newRowLength):
            for j in range(newSecretLength):
                if (newRow[i] == newSecret[j]) and (j not in secretIndex):
                    sameColor += 1
                    secretIndex.append(j)
                    
        printList = []
        for _ in range(samePosAndColor):
            printList.append(BLACK)
        for _ in range(sameColor):
            printList.append(RED)
            
        l = len(printList)
        if l < 4:
            for _ in range(4 - l):
                printList.append(UNKNOWN)
        
        finalPrintList = self.shuffle(printList)
        return finalPrintList
        
    def shuffle(self, orderedList):
        l = len(orderedList)
        randList = random.sample(range(0, l), l)
        newList = []
        for item in randList:
            newList.append(orderedList[item])
        return newList
    
    def checkAllCorrect(self, orderedList):
        for element in orderedList:
            if element != BLACK:
                return False
        return True
    
    def enterSecret(self):
        return self.parser(True)
    
    def parser(self, start):
        colorsEntered = []
        for item in range(NUM_SLOTS):
            toContinue = True
            
            if start:
                print(f"What is the color you want to give for pin # {item + 1}?")
            else:
                print(f"What do you think think pin # {item + 1} is?")
                
            while(toContinue):
                
                if start:
                    result = input("Input your color here: ").strip().lower()
                else:
                    result = input("Input your guess: ").strip().lower()
                    
                if result in COLORS_LIST:
                    toContinue = False
                    colorsEntered.append(result)
                elif result in ["quit"]:
                    toContinue = False
                    return False
                else:
                    print("That was not a valid color.")
                    print("The valid colors are: ")
                    list(map(print, COLORS_LIST))
                    print("To quit type 'quit'.")
                    print("Try again.")
        
        row = []
        for item in colorsEntered:
            color = self.translateColor(item)
            row.append(color)
        return row
    
        
    def translateColor(self, userColor):
        if userColor == 'magenta':
            return MAGENTA
        if userColor == 'white':
            return WHITE
        if userColor == 'purple':
            return PURPLE
        if userColor == 'yellow':
            return YELLOW
        if userColor == 'green':
            return GREEN
        return ORANGE
        
if __name__ == '__main__':
    g = Game()
    g.continueGame()