import random

alphabets_small = "qwertyuiopasdfghjklzxcvbnm"
alphabets_big = "QWERTYUIOPASDFGHJKLZXCVBNM"
special_char = "!@#$&?_*"
numbers = "1234567890"


def password_generator(password_length, name, alphabets_big, special_char, numbers, alphabets_small):
    name = name.lower()
    name = name.replace("o", "0").replace("i", "1").replace("s","&")
    name = name.capitalize()
    
    remaining_length = password_length - len(name) - 1  
    
    all_chars = alphabets_big + alphabets_small + numbers + special_char
    random_part = ''.join(random.choice(all_chars) for _ in range(remaining_length))

    password = name + random.choice(special_char) + random_part
    return password
print("\n---WELCOME TO OUR PASSWORD GENRATOR 🔐---\n")
name = str(input("Enter your name: "))
password_length = int(input(f"Enter password lenght(minimum {len(name)+ 4}): "))
if password_length <len(name) + 4:
    print("choose a bigger number for password lenght.")
else:
    print(password_generator(password_length, name, alphabets_big, special_char, numbers, alphabets_small))