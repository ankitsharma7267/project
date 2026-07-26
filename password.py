<<<<<<< HEAD
import random

len = int(input("enter the password length"))

characters =  "1234567890ABCDEFGHIJKLabcdefghijkl@#$*&"

password = ""

for i in range(len):
    password += random.choice(characters) 

=======
import random

len = int(input("enter the password length"))

characters =  "1234567890ABCDEFGHIJKLabcdefghijkl@#$*&"

password = ""

for i in range(len):
    password += random.choice(characters) 

>>>>>>> 735208c1b1cc1c600577736dadadd8aaecb8bc03
print("Your Password is = ", password)