import random

password_generator = random.SystemRandom()

def generate_password(length):
    password=""
    for i in range(length):
        password += password_generator.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print(password)

num_caracteres = int(input("Entrez le nombre de caracteres : "))
generate_password(num_caracteres)
