
responses = ["Yes oh yes", "Maybe, I really don't know", "Engk, Engot", "Ask again later alligator"]

import random


#while True:
    #question = input("Ask your question here: ")
    #answer = random.choice(responses)
    #print(answer)

    #if question == "no"
    #break
    #All of this is wrong because python reads the code line by line
    #This doesn't work and the one on the bottom does! <3

while True:
    question = input("Ask your question here: ")
    if question == "no":
        break
    answer = random.choice(responses)
    print(answer)

    


