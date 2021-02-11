import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
while True:
    password_count = int(input("How many passwords you like generated? "))
    pass_length = int(input("What would you like the length of your password to be:  "))
    for c in range(0, password_count):
        password = ""
        for i in range(0, pass_length):
            password_chars = random.choice(chars)
            password += password_chars
        print(f"Your password(s): {password}")

