import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    return password

print("--- PASSWORD GENERATOR ---")

try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Length must be greater than 0!")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")