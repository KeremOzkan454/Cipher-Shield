import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.chat.util import Chat, reflections

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


# jsondan veri alma
def get_info(konu):
    try:
        with open('database.json', 'r', encoding='utf-8') as dosya:
            data = json.load(dosya)
            return str(data.get(konu, "Bu konuda bilgi bulunmamaktadır."))
    except FileNotFoundError:
        return "Veri dosyası bulunamadı."
    

print("Shield AI: Sohbetinize son vermek için 'kapat' yazabilirsiniz.")
while True:
    user_input = input("Siz: ")
    if user_input.lower() == "kapat":
        print("Shield AI: Görüşmek üzere.")
        break
    else:
        tokenized = word_tokenize(user_input)
        clear_text = set(tokenized) - set(stopwords.words("turkish"))
        for word in clear_text:
            if word.lower() == (r"merhaba|naber|nasılsın|sen nesin|nesin sen|selam|merhabalar|selamlar|adın|ismin|ismini|adını|meraba|merabalar"):
                response = get_info("merhaba")
                print(f"Shield AI: {response}")
            elif word.lower() == (r"şifre|şifrem|şifremi|şifrelerimi|parola|parolalarda|parolalar|şifreler|parolalarımı|parolam|parolamı"):
                response = get_info("şifre güvenliği")
                print(f"Shield AI: {response}")
