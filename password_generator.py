import random
import string


letters = string.ascii_letters

password_length = int(input("Enter password length: "))
password = ""

for i in range(password_length):
    password = password + random.choice(letters)

print(password)