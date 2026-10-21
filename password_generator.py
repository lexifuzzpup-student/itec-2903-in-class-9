import random
import string

banner_message = "Welcome to password_generator.py. You can do anything at password_generator.py."
print("-" * len(banner_message))
print(banner_message)
print("-" * len(banner_message))

letters = string.ascii_letters

password_length = int(input("Enter password length: "))
password = ""

for i in range(password_length):
    password = password + random.choice(letters)

print(password)