import re
import random
import string
from cryptography.fernet import Fernet
import os

# Parola güç kontrolü
def password_control(parola):
    uzunluk = len(parola) >= 16
    kucuk_harf = bool(re.search(r"[qwertyuıopğüasdfghjklşizxcvbnmöç]", parola))
    buyuk_harf = bool(re.search(r"[QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ]", parola))
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
    if os.path.exists("data/key.key"):
        with open("data/key.key", "rb") as key_file:
            Key = key_file.read()
    else:
        Key = Fernet.generate_key()
        with open("data/key.key", "wb") as key_file:
            key_file.write(Key)
    return Key

def save_password(user_name, password, key):
    Fernet_key = Fernet(key)
    encrypted_password = Fernet_key.encrypt(password.encode())
    with open("data/Vault.txt", "a") as kasa:
        kasa.write(f"{user_name},{encrypted_password.decode()}\n")

def load_passwords(key):
    fernet_key = Fernet(key)
    with open("data/Vault.txt", "r") as kasa:
        for line in kasa:
            user_name, encrypted_password = line.strip().split(",")
            decrypted_password = fernet_key.decrypt(encrypted_password.encode())
            print(f"Kullanıcı: {user_name}, Şifre: {decrypted_password.decode()}")

        


# Vault acces olayları    
def write_vault_password(password):
    with open("data/VaultPass.txt","wb") as file:
        file.write(password.encode())

def check_vault_password(password):
    with open("data/VaultPass.txt","r") as file:
        true_password = file.read()
        if password == true_password:
            return True
        else:
            return False
        
def create_vault():
    with open("data/Vault.txt","wb"):
        return

def create_vault_pass():
    with open("data/VaultPass.txt","wb"):
        return

