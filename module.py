import re
import random
import string


def password_control(parola):
    uzunluk = len(parola) >= 12
    kucuk_harf = bool(re.search(r"[a-z]", parola))
    buyuk_harf = bool(re.search(r"[A-Z]", parola))
    sayi = bool(re.search(r"[0-9]", parola))
    karakter = bool(re.search(r"[!@#$%^&*()_+]", parola))

    return uzunluk, kucuk_harf, buyuk_harf, sayi, karakter

def check(parola,file):
    pwned = False

    with open(file, "r", encoding="ISO-8859-1") as dosya:
        for satır in dosya:
            if satır.strip() == str(parola):
                pwned = True
                break

    return pwned

def generate_password(leng=16):
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation
    
    password = ""
    for i in range(leng):
        password += random.choice(chars)
        
    return password