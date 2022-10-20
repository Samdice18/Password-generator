from curses.ascii import isdigit
import random as r

def password_length():
    print("The length of your password should be more than 8 characters long.\n")
    
    while True:
        user_length = input("Enter the length of your required password: ")

        if not user_length.isdigit():
            print("enter only numbers\n")

        elif user_length.isdigit():
            if int(user_length) <= 8 or int(user_length) > 56:
                print("\nThe length should be over 8 characters and less than 56 characters\n")
                continue
            
            if int(user_length) > 8:
                return user_length

def secret_password(length):
    numbers = "1234567890"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%+=~"

    characters_to_use = numbers + uppercase_letters + lowercase_letters + symbols

    password = r.sample(characters_to_use, int(length))

    return "".join(password)

if __name__ == '__main__':
    length = password_length()
    generated_password = secret_password(length)
    print(f"\nyour generated password : {generated_password} ")
