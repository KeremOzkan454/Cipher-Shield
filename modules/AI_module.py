import sys
import json
import random
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit


# JSOn dan veri transferi
def get_info(konu):
    try:
        with open('data/database.json', 'r', encoding='utf-8') as dosya:
            data = json.load(dosya)
            return random.choice(data.get(konu, ["Bu konuda bilgi bulunmamaktadır."]))
    except FileNotFoundError:
        return "Veritabanı bulunamadı."


# PyQT GUI sınıfı
class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shield AI")
        self.setGeometry(100, 100, 600, 400)

        # Ana widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Arayüz öğeleri
        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Bir şey yazın ve Enter'a basın...")
        self.layout.addWidget(self.input_box)

        self.send_button = QPushButton("Gönder")
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        # Sinyaller
        self.send_button.clicked.connect(self.handle_input)
        self.input_box.returnPressed.connect(self.handle_input)

    def handle_input(self):
        user_input = self.input_box.text()
        self.chat_display.append(f"Siz: {user_input}")
        self.input_box.clear()

        # Çıkış kontrolü
        if re.search(r"çık|kapat|kapa|çıkış", user_input.lower()):
            self.chat_display.append("Shield AI: Görüşmek üzere!")
            QApplication.instance().quit()
            return

        # Yanıt oluşturma
        response = self.get_response(user_input)
        self.chat_display.append(f"Shield AI: {response}")

    def get_response(self, user_input):
        # Kullanıcı girdisi kontrolü
        if re.search(r"merhaba|selam|hoş geldin|naber", user_input.lower()):
            response = get_info("merhaba")

        elif re.search(r"şifre güvenliği|şifre oluşturma|güvenli şifre|şifre|parola", user_input.lower()):
            response = get_info("şifre güvenliği")

        elif re.search(r"veri ihlali|hesap güvenliği|hack", user_input.lower()):
            response = get_info("veri ihlali")

        elif re.search(r"çift faktörlü doğrulama|2fa|iki aşamalı doğrulama", user_input.lower()):
            response = get_info("çift faktörlü doğrulama")

        elif re.search(r"phishing|kimlik avı|sahte e-posta", user_input.lower()):
            response = get_info("phishing")

        elif re.search(r"veri güvenliği|bilgi güvenliği|hassas veri", user_input.lower()):
            response = get_info("veri güvenliği")

        elif re.search(r"güncelleme|yazılım güncelleme", user_input.lower()):
            response = get_info("güncellemeler")

        elif re.search(r"antivirüs|virüs taraması", user_input.lower()):
            response = get_info("antivirüs")

        elif re.search(r"kötü amaçlı yazılım|malware", user_input.lower()):
            response = get_info("kötü amaçlı yazılımlar")

        elif re.search(r"sosyal mühendislik|manipülasyon", user_input.lower()):
            response = get_info("sosyal mühendislik")

        elif re.search(r"şifre yöneticisi|şifre saklama", user_input.lower()):
            response = get_info("şifre yöneticileri")

        elif re.search(r"tarayıcı güvenliği|https|güvenli tarayıcı", user_input.lower()):
            response = get_info("tarayıcı güvenliği")

        elif re.search(r"e-posta güvenliği|güvenli e-posta|mail güvenliği", user_input.lower()):
            response = get_info("e-posta güvenliği")

        elif re.search(r"bulut güvenliği|bulut depolama", user_input.lower()):
            response = get_info("bulut depolama güvenliği")

        elif re.search(r"wi-fi güvenliği|wifi güvenliği|ağ güvenliği", user_input.lower()):
            response = get_info("Wi-Fi güvenliği")

        elif re.search(r"kimlik avı|phishing saldırısı|kimlik avı saldırısı", user_input.lower()):
            response = get_info("kimlik avı saldırıları")

        elif re.search(r"güvenlik duvarı|firewall", user_input.lower()):
            response = get_info("güvenlik duvarı")

        elif re.search(r"veri yedekleme|yedekleme|yedek alma", user_input.lower()):
            response = get_info("veri yedekleme")

        elif re.search(r"siber saldırılar|ağ saldırıları", user_input.lower()):
            response = get_info("siber saldırılar")

        elif re.search(r"siber güvenlik|cyber security|siber güvenliğ", user_input.lower()):
            response = get_info("siber güvenlik")
            
        else:
            response = "Bu konuda bilgiye sahip değilim. Daha fazla bilgi için başka bir konu deneyebilirsiniz."
        return response