import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


def main():
    has_number = False
    has_special = False
    min_length = input("Enter the minimum length of the password?")
    number = input("Would you like numbers in you password? (yes/no)").lower()
    special = input(
        "Would you like special characters in your password? (yes/no)").lower()

    while True:
      if min_length.isdigit():
        min_length = int(min_length)
        break
      else:
        print("Enter valid number")  
    
    if number == "yes":
        has_number = True
    if special == "yes":
        has_special = True

    pwd = generate_password(min_length, has_number, has_special)
    print(f"The generated password is {pwd}")


main()
