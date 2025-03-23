
import random

print("POSSWORD GENERATOR!")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"


numbers = int(input("How Many Possword You Want To Generate:"))

lenght = int(input("How Many Characters You Want In Your Posswords:"))

print("Here Are Your Posswords!")


for pswd in range(numbers):
    password = ""
    for c in range(lenght):
        password += random.choice(chars)
    print(password)