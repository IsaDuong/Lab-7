x = 1
while (x<300):
    print x
    x = x + 2
    
myList = [8,45,60,15,30,75,85,50,20,5]
index = 0
while (index < len(myList)):
    print myList[index]
    index = index + 1
    
import random
rand = random.randint(0,50)
userInput = raw_input()
print "Guess a number between 0-50"
while (userInput != rand):
    userInput = int(raw_input())
    if userInput > rand:
        print "Your guess was too high. Try again."
    if userInput < rand:
        print "Your guess was too low. Try again."
    if userInput == rand:
        print "Your guess was right"