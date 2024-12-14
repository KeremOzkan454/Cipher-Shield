import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import modules.main_module as main_module
import modules.AI_module as AI_module


class CipherShieldApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher Shield")
        self.setGeometry(100, 100, 900, 600)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)


        self.password_tab = PasswordControlTab()
        self.vault_tab = CipherVaultTab()
        self.shieldai_tab = ShieldAITab()

        self.tabs.addTab(self.password_tab, "Password Control")
        self.tabs.addTab(self.vault_tab, "Cipher Vault")
        self.tabs.addTab(self.shieldai_tab, "Shield AI")

        # Tema
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #5DADE2;
                background: #EAF2F8;
            }
            QTabBar::tab {
                background: #AED6F1;
                color: black;
                padding: 15px;
                font: bold 16px;  
                min-width: 160px; 
                min-height: 20px;  
                border-radius: 8px; 
            }
            QTabBar::tab:selected {
                background: #5DADE2;
                color: white;
            }
            QMainWindow {
                background-color: #EAF2F8;
            }
        """)


class PasswordControlTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel("Password Control")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arimo", 16, QFont.Bold))
        layout.addWidget(self.title)

        # Parola girişi
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Parolanızı girin...")
        self.password_input.setFont(QFont("Arimo", 14))
        layout.addWidget(self.password_input)

        # Güvenlik kontrolü butonu
        self.check_password_btn = QPushButton("Parola Güvenliğini Kontrol Et")
        self.check_password_btn.setFont(QFont("Arimo", 12))
        self.check_password_btn.clicked.connect(self.check_password)
        layout.addWidget(self.check_password_btn)

        # Pwned kontrol butonu
        self.pwned_check_btn = QPushButton("Veri İhlali Kontrolü")
        self.pwned_check_btn.setFont(QFont("Arimo", 12))
        self.pwned_check_btn.clicked.connect(self.check_pwned)
        layout.addWidget(self.pwned_check_btn)

        # Güçlü parola önerisi butonu
        self.generate_password_btn = QPushButton("Güçlü Parola Önerisi")
        self.generate_password_btn.setFont(QFont("Arimo", 12))
        self.generate_password_btn.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_password_btn)

        # Log ekranı
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setFont(QFont("Arimo", 12))
        layout.addWidget(self.log_output)

        self.setLayout(layout)

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

    def check_pwned(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Hata", "Lütfen bir parola giriniz!")
            return

        is_pwned = main_module.check(password, "data/pwned.txt")
        if is_pwned:
            self.log_output.append("Parolanız bir veri ihlalinde açığa çıkmış!")
        else:
            self.log_output.append("Parolanız güvende.")

    def generate_password(self):
        new_password = main_module.generate_password()
        self.log_output.append(f"Önerilen Güçlü Parola: {new_password}")


class CipherVaultTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel("Cipher Vault")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arimo", 18, QFont.Bold))
        layout.addWidget(self.title)

        # Mesaj
        self.info_label = QLabel("Bu sekme parolalarınızı güvenli bir şekilde saklamanıza yardımcı olur.")
        self.info_label.setFont(QFont("Arimo", 12))
        layout.addWidget(self.info_label)

        self.setLayout(layout)


class ShieldAITab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel("ShieldAI - Siber Güvenlik Chatbot")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Arimo", 16, QFont.Bold))
        layout.addWidget(self.title)

        # Kullanıcı girişi
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Sorunuzu yazın...")
        self.user_input.setFont(QFont("Arimo", 14))
        layout.addWidget(self.user_input)

        # Yanıt ekranı
        self.chat_output = QTextEdit()
        self.chat_output.setReadOnly(True)
        self.chat_output.setFont(QFont("Arimo", 12))
        layout.addWidget(self.chat_output)

        # Gönder butonu
        self.send_button = QPushButton("Gönder")
        self.send_button.setFont(QFont("Arimo", 12))
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        user_input = self.user_input.text()
        if not user_input:
            QMessageBox.warning(self, "Hata", "Lütfen bir mesaj giriniz!")
            return

        response = AI_module.get_response(user_input)
        self.chat_output.append(f"Siz: {user_input}")
        self.chat_output.append(f"Shield AI: {response}")


# Uygulamayı Çalıştır
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CipherShieldApp()
    window.show()
    sys.exit(app.exec_())
