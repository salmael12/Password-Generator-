import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Longueur du mot de passe : "))
print("Mot de passe généré :", generate_password(length))
