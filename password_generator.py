import random
import string

def generate_password():
    print("---Password Generator---")
    lenght=int(input("Enter the lenght of the password:"))

    if(lenght<8):
        print("Password lenght must be atleast 8!")
        return
    
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation

    password=[
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars=lower+upper+digits+symbols

    for _ in range(lenght-4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    final_password="".join(password)

    print("\nGenerated Password:")
    print(final_password)

generate_password()