import random

password_generator = random.SystemRandom()

def generate_password(length):
    password=""
    for i in range(length):
        password += password_generator.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print(password)

while True:
    try:
        num_caracteres = int(input("Entrez le nombre de caracteres : "))
        if num_caracteres > 0:
            break
        else:
            print("Le nombre de caracteres doit être positif")
    except ValueError:
        print("Le nombre de caracteres doit être un entier")

ganerate_password = generate_password(num_caracteres)
print("Mot de passe généré :", generate_password)