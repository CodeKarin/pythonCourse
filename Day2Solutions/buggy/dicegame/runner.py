from .die import Die
from .utils import i_just_throw_an_exception
import sys

class GameRunner:

    def __init__(self, round = 1, wins = 0, loses = 0):
        self.dice = Die.create_dice(6)
        #self.reset()
        self.round = round
        self.wins = wins
        self.loses = loses
        
    def round_update(self):
        self.round +=1    
        return round
    
    def reset(self):
        # self.dice = 0
        self.round = 0
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            #total += 1
            total += die.value    
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        round = 1
        wins = 0
        loses  = 0
        #runner = cls()
       
       
        while True:
            #runner = cls()  #OR  
            runner = GameRunner(round, wins, loses)
            
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
             #   print(die.value())
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess ==  runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                loses += 1
                c += 1
            print("Wins: {} Loses {}".format(wins, loses))
            round +=1

            if c == 6:
                print("You won...{} times. Congrats...".format(wins))
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                #runner.round_update()
                continue
            elif prompt == 'n':
               sys.exit()
            else:
                i_just_throw_an_exception()
       