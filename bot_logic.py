import random

def gen_password(lunghezza):
    maiuscole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscole = "abcdefghijklmnopqrstuvwxyz"
    caratteri = "!@#$%^&*()_+-=[]|;:',.<>?/`~"
    numeri = "1234567890"
    password = ""
    for i in range(lunghezza):
        scelta = random.randint(1, 4)
        if scelta == 1:
            lunghezza1 = random.randint(0, len(maiuscole) -  1)
            password += maiuscole[lunghezza1]
        elif scelta == 2:
            lunghezza2 = random.randint(0, len(minuscole) - 1)
            password += minuscole[lunghezza2]
        elif scelta == 3:
            lunghezza3 = random.randint(0, len(caratteri) - 1)
            password += caratteri[lunghezza3]
        else:
            lunghezza4 = random.randint(0, len(numeri) - 1)
            password += numeri[lunghezza4]
    return password
