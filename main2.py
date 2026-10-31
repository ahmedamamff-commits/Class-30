class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        #We will return a string
        return self.word+' ( '+self.meaning+' )'

flash = []
print("Welcome to flashcard application.")

#The following loop will be repeated until the user stops to add the flashcards
while(True):
    word = input("Enter the name of the word you want to create the flashcard of:")
    meaning = input("Enter the meaning of the word that you want to create the flashcard of:")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another word as a flashcard, press 1."))

    if(option):
        break

#Printing all of the flashcards
print("\nYour flashcards:\n")
for i in flash:
    print(">", i)