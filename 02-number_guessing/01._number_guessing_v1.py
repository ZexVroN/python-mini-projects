import random

number = random.randint(1, 3)
cek = False

while cek == False:
    guess = int(input("Masukan nomor = "))
    if guess != number and guess > number:
        print("Tebakan salah, nilai terlalu besar")

    elif guess != number and guess < number:
        print("Tebakan salah nilai terlalu kecil")

    else:
        print(f"Tebakan benar, nomor = {number}")
        cek = True
