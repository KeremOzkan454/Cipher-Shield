import json
from nltk.chat.util import Chat, reflections

# jsondan veri alma
def get_info(konu):
    try:
        with open('database.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return str(data.get(konu, "Bu konuda bilgi bulunmamaktadır."))
    except FileNotFoundError:
        return "Veri dosyası bulunamadı."
    
x1 = get_info("Şifre Güvenliği")
x2 = get_info("Veri İhlali")
x3 = get_info("Çift Faktörlü Doğrulama")
x4 = get_info("Merhaba")



# cevap vereceği zımbırtılar
patterns = [
    (r'^(şifre güvenliği|güçlü şifre|şifre|şifremi nasıl korurum)$',x1),

    (r'^(veri ihlali|veri güvenliği|hesap güvenliği)$',x2),

    (r'^(çift faktörlü doğrulama|2fa|2 faktörlü doğrulama|iki faktör doğrulama|iki faktörlü doğrulama)$',x3),

    (r'^(merhaba|selam|merhabalar|nesin sen|sen nesin|adın ne|selamlar|naber|nabersin)$',x4),

    (r'(.*)$', 
     lambda x: "Üzgünüm, bu konuda bilgi veremiyorum. Başka bir konu hakkında sorunuz varsa, size yardımcı olabilirim.")
]

# Chatbot oluşturulması
chatbot = Chat(patterns, reflections)

#### Ana döngü ####

print("Chatbot'a 'kapat' yazana kadar sohbet edebilirsiniz.")
while True:
    user_input = input("Siz: ")
    if user_input.lower() == 'kapat':
        print("Chatbot: Görüşmek üzere!")
        break
    else:
        output = chatbot.respond(user_input)
        print(f"Chatbot: {output}")
