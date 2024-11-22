import tkinter as tk
from tkinter import messagebox
import re
import random
import string



def pass_cont(passwd):
    uzunluk = len(passwd) >= 12
    kucukh = bool(re.search(r"[a-z]", passwd))
    buyukh = bool(re.search(r"[A-Z]", passwd))
    sayi = bool(re.search(r"[0-9]", passwd))
    karakter = bool(re.search(r"[!@#$%^&*()_+]", passwd))
    return uzunluk, kucukh, buyukh, sayi, karakter

def check(passwd):
    pwned = False

    with open("pwned.txt", "r", encoding="ISO-8859-1") as dosya:
        for satır in dosya:
            if satır.strip() == str(passwd):
                pwned = True
                break

    return pwned

def check_pass_str():
    parola = entry.get()
    if not parola:
        messagebox.showwarning("Uyarı", "Lütfen bir parola girin!!!")
        return

    uzunluk, kucukh, buyukh, sayi, karakter = pass_cont(parola)
    uzu = len(parola)
    deger = 0

    if uzunluk:
        deger += 2
    if kucukh:
        deger += 1
    if buyukh:
        deger += 2
    if sayi:
        deger += 2
    if karakter:
        deger += 3

    result_text = f"Parolanızın güvenlik düzeyi: {deger} / 10\n"

    if deger == 0:
        result_text += "[_ _ _ _ _ _ _ _ _ _]"
    elif deger == 1:
        result_text += "[# _ _ _ _ _ _ _ _ _]"
    elif deger == 2:
        result_text += "[# # _ _ _ _ _ _ _ _]"
    elif deger == 3:
        result_text += "[# # # _ _ _ _ _ _ _]"
    elif deger == 4:
        result_text += "[# # # # _ _ _ _ _ _]"
    elif deger == 5:
        result_text += "[# # # # # _ _ _ _ _]"
    elif deger == 6:
        result_text += "[# # # # # # _ _ _ _]"
    elif deger == 7:
        result_text += "[# # # # # # # _ _ _]"
    elif deger == 8:
        result_text += "[# # # # # # # # _ _]"
    elif deger == 9:
        result_text += "[# # # # # # # # # _]"
    elif deger == 10:
        result_text += "[# # # # # # # # # #]"

    if uzunluk and kucukh and buyukh and sayi and karakter:
        result_text += "\nYaşasın! Parolanız oldukça güvenli."
    elif deger > 4 and deger < 10:
        result_text += "\nParolanız kısmen güvenli. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!"
    elif deger <= 4:
        result_text += "\nParolanız çok zayıf. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!"
    
    if not uzunluk:
        result_text += f"\nParolanız en az 12 karakter uzunluğunda olmalıdır! Sizin parolanız ise {uzu} uzunluğunda."
    if not kucukh:
        result_text += "\nParolanız küçük harf içermelidir!"
    if not buyukh:
        result_text += "\nParolanız büyük harf içermelidir!"
    if not sayi:
        result_text += "\nParolanız sayı içermelidir!"
    if not karakter:
        result_text += "\nParolanız özel karakter içermelidir!"

    result.delete(1.0, tk.END)
    result.insert(tk.END, result_text)

def check_pwned_pass():
    parola = entry.get()
    if not parola:
        messagebox.showwarning("Uyarı", "Lütfen bir parola girin!")
        return

    pwn = check(parola)
    result_text = ""

    if pwn:
        result_text = "\nEyvah! Parolanız daha önceki veri ihlallerinde açığa çıkarılmış. Derhal bu parolayı değiştirmeniz önerilir!"
    else:
        result_text = "\nParolanız şu ana kadarki hiçbir veri ihlalinde açığa çıkmamış. Parolanız güvende."

    result.delete(1.0, tk.END)
    result.insert(tk.END, result_text)

def generate_pass(leng=16):
    chars = string.ascii_letters
    chars += string.digits
    chars += string.punctuation
    
    passwd = ""
    result_text = ""
    for i in range(leng):
        passwd += random.choice(chars)
        
    result_text = passwd
    
    result.delete(1.0, tk.END)
    result.insert(tk.END, result_text)
        
        

def quit_prog():
    window.quit()


window = tk.Tk()
window.title("Cipher Shield")
window.geometry("600x700")
window.config(bg="#E1EFFF")

# Output text
result = tk.Text(window, height=15, width=40, wrap=tk.WORD, font=("Arial", 15), bg="#D1D9FF")
result.pack(pady=10)

# Kullanıcı giriş
entry_label = tk.Label(window, text="Parolanızı giriniz:", font=("Arial", 16), bg="#E1EFFF")
entry_label.pack(pady=5)
entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Butonlar
buton_check_pass = tk.Button(window, text="Parola Güvenliği Testi", width=30, font=("Arial", 12), bg="#4C79FF", command=check_pass_str)
buton_check_pass.pack(pady=5)

buton_check_pwned = tk.Button(window, text="Parola Pwned Kontrolü", width=30, font=("Arial", 12), bg="#4C79FF", command=check_pwned_pass)
buton_check_pwned.pack(pady=5)

buton_oner_pass = tk.Button(window, text="Parola Öner", width=30, font=("Arial",12),bg="#4C79FF",command=generate_pass)
buton_oner_pass.pack(pady=5)

buton_exit = tk.Button(window, text="Çıkış", width=30, font=("Arial", 12), bg="#FF4C4C", command=quit_prog)
buton_exit.pack(pady=5)

window.mainloop()
