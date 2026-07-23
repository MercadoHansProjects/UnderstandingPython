import string
import random

#print(string.ascii_letters) #just a sample
#print(string.digits) #just a sample
#print(string.punctuation) #just a sample
#all these string is just like a database where it would get the output needed 


characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length =(input("Enter password length (or 'exit' to close): "))
    if length == "exit":
        break
    length = int(length)
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print(f"Your password: {password}")

