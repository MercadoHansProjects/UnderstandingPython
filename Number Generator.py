#Number Generator

import random

while True:
    question = input("Want a random number? (type 'stop' to end): ")
    if question == "stop":
        break

    answer = random.randint(1, 100)
    print(answer)
    




