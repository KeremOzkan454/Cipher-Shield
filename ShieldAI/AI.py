import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.chat.util import Chat, reflections

nltk.download("punkt")
nltk.download("punkt_tab")

# jsondan veri alma
def get_info(konu):
    try:
        with open('database.json', 'r', encoding='utf-8') as dosya:
            data = json.load(dosya)
            return str(data.get(konu, "Bu konuda bilgi bulunmamaktadır."))
    except FileNotFoundError:
        return "Veri dosyası bulunamadı."
    

print("Yapay zeka ile sohbetinize son vermek için 'kapat' yazabilirsiniz.")
while True:
    user_input = input("Siz: ")
    tokenized = word_tokenize(user_input)
    print(tokenized)

