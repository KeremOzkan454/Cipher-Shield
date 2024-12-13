import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import modules.main_module as main_module
import modules.AI_module as AI_module


class CipherShieldApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher Shield")
        self.setGeometry(200, 200, 800, 600)
        
        # Main Widget ve Layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        # GUI elemanları
        self.label = QLabel("Cipher Shield\nYour Digital Fortress")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 18, QFont.Bold))
        self.layout.addWidget(self.label)
        
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setFont(QFont("Calibri", 15))
        self.layout.addWidget(self.log_output)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Parolanızı buraya girin...")
        self.password_input.setFont(QFont("Calibri", 15))
        self.layout.addWidget(self.password_input)
        
        self.check_password_btn = QPushButton("Parola Güvenliğini Kontrol Et")
        self.check_password_btn.setFont(QFont("Calibri", 15))
        self.check_password_btn.clicked.connect(self.check_password)
        self.layout.addWidget(self.check_password_btn)
        
        self.pwned_check_btn = QPushButton("Veri İhlali Kontrolü")
        self.pwned_check_btn.setFont(QFont("Calibri", 15))
        self.pwned_check_btn.clicked.connect(self.check_pwned)
        self.layout.addWidget(self.pwned_check_btn)
        
        self.generate_password_btn = QPushButton("Güçlü Parola Önerisi")
        self.generate_password_btn.setFont(QFont("Calibri", 15)) 
        self.generate_password_btn.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_password_btn)
        
        self.vault_access_btn = QPushButton("Parola Kasa")
        self.vault_access_btn.setFont(QFont("Calibri", 15))
        self.vault_access_btn.clicked.connect(self.access_vault)
        self.layout.addWidget(self.vault_access_btn)
        
        self.ai_chat_btn = QPushButton("Shield AI ile Konuş")
        self.ai_chat_btn.setFont(QFont("Calibri", 15))
        self.ai_chat_btn.clicked.connect(self.start_ai_chat)
        self.layout.addWidget(self.ai_chat_btn)
        
        self.quit_btn = QPushButton("Çıkış")
        self.quit_btn.setFont(QFont("Calibri", 15)) 
        self.quit_btn.clicked.connect(self.close)
        self.layout.addWidget(self.quit_btn)
    
    # Fonksiyonlar:

    ## parola kontrol
    def check_password(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Hata", "Lütfen bir parola giriniz!")
            return
        
        uzunluk, kucuk_harf, buyuk_harf, sayi, karakter = main_module.password_control(password)
        deger = 0
        if uzunluk: deger += 2
        if kucuk_harf: deger += 1
        if buyuk_harf: deger += 2
        if sayi: deger += 2
        if karakter: deger += 3
        
        self.log_output.append(f"Parolanızın güvenlik düzeyi: {deger}/10")
        if deger < 5:
            self.log_output.append("Parolanız çok zayıf.")
        elif 5 <= deger < 9:
            self.log_output.append("Parolanız kısmen güvenli.")
        else:
            self.log_output.append("Parolanız oldukça güvenli!")
    
    ## pwned kontrol
    def check_pwned(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Hata", "Lütfen bir parola giriniz!")
            return
        
        is_pwned = main_module.check(password, "data/pwned.txt")
        if is_pwned:
            self.log_output.append("Parolanız bir veri ihlalinde açığa çıkmış. Hemen değiştirin!")
        else:
            self.log_output.append("Parolanız güvende. Hiçbir veri ihlalinde açığa çıkmamış.")
    
    ## parola öneri
    def generate_password(self):
        new_password = main_module.generate_password()
        self.log_output.append(f"Önerilen Güçlü Parola: {new_password}")
    
    ## Kasaya erişim
    def access_vault(self):
        QMessageBox.information(self, "Kasa", "Parola kasası şu anda desteklenmiyor. Bu özellik yakında eklenecek!")
    
    ## ShieldAI
    def start_ai_chat(self):
        QMessageBox.information(self, "Shield AI", "Shield AI sohbeti şu anda desteklenmiyor. Bu özellik yakında eklenecek!")


# Uygulamayı Çalıştır
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CipherShieldApp()
    window.show()
    sys.exit(app.exec_())
