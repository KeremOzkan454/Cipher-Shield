import modules.AI_module as AI_module
import sys

if __name__ == "__main__":
    app = AI_module.QApplication(sys.argv)
    window = AI_module.ChatbotApp()
    window.show()
    sys.exit(app.exec_())