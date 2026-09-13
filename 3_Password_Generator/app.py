import random
import string

def generate_password(length, include_numbers, include_special):
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits

    if include_special:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print("----- PASSWORD GENERATOR -----")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:

        numbers = input("Include numbers? (yes/no): ").lower()
        special = input("Include special characters? (yes/no): ").lower()

        include_numbers = numbers == "yes"
        include_special = special == "yes"

        password = generate_password(
            length,
            include_numbers,
            include_special
        )

        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter a valid number.")