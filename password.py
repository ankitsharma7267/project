import random

len = int(input("enter the password length"))

characters =  "1234567890ABCDEFGHIJKLabcdefghijkl@#$*&"

password = ""

for i in range(len):
    password += random.choice(characters) 

print("Your Password is = ", password)