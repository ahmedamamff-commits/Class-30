import random
from turtle import color

class FruitQuiz:

    #Create a constructor
    def __init__(self):

        #Create a dictionary of fruits as the keys and colors as the values
        self.fruits = {'apple':'red', 'orange':'orange','watermelon':'green','banana':'yellow'}

    #Function for the quiz, here a fruit will be chosen randomly by a randomized picker
    def quiz(self):
        while (True):


            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct answer!")
            else:
                print("Wrong answer! Good luck next time!")

            option = int(input("Enter 0 if you want to quit the quiz. If you want to continue playing more rounds, press 1:"))

            if(option):
                break

print("Welcome to the fruit quiz!")
fq = FruitQuiz()
fq.quiz()