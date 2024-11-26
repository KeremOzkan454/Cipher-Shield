import re
import random
import string
import cryptography
from cryptography.fernet import Fernet
import os

# Parola güç kontrolü
def password_control(parola):
    uzunluk = len(parola) >= 12
    kucuk_harf = bool(re.search(r"[a-z]", parola))
    buyuk_harf = bool(re.search(r"[A-Z]", parola))
    sayi = bool(re.search(r"[0-9]", parola))
    karakter = bool(re.search(r"[!@#$%^&*()_+]", parola))

    return uzunluk, kucuk_harf, buyuk_harf, sayi, karakter



# Pwned control
def check(parola,file):
    pwned = False

    with open(file, "r", encoding="ISO-8859-1") as dosya:
        for satır in dosya:
            if satır.strip() == str(parola):
                pwned = True
                break

    return pwned




# Parola oluşturma
def generate_password(leng=16):
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation
    
    password = ""
    for i in range(leng):
        password += random.choice(chars)
        
    return password





# fernet olayları
def create_or_load_key():
    isKey = os.path.exists("key.key")
    if isKey:
        with open("key.key","rb") as key:
            Key = key.read()
    else:
        with open("key.key","rw") as key:
            Key = Fernet.generate_key()
            key.write(Key)
    return Key

def save_password(user_name,password):
    with open("Vault.txt","w") as kasa:
        encrytep_password = Fernet.encrypt(password)
        kasa.write(f"{user_name},{encrytep_password}\n")

def load_passwords(key):
    with open("Vault.txt","r") as kasa:
        user_name,encrypted_password = kasa.read().strip().split()
        decrypted_password = Fernet.decrypt(encrypted_password.encode(),key)
        print(f"{user_name}  {decrypted_password.encode()}")
        


# Vault acces olayları    
def write_vault_password(password):
    with open("VaultPass.txt","rw") as file:
        file.write(password)

def check_vault_password(password):
    with open("VaultPass.txt","r") as file:
        true_password = file.read()
        if password == true_password:
            return True
        else:
            return False