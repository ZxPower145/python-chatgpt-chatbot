import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import qdarktheme
from PyQt6.QtGui import QFont
import back_end
import threading


class ChatBotWindow(QMainWindow):
    # Front-End
    def __init__(self):
        super().__init__()

        self.chatbot = back_end.ChatBot()

        self.setFixedSize(700, 500)

        self.setWindowTitle("ChatBot")

        # Set font
        font = QFont()
        font.setPointSize(14)
        font.setFamily("Times")

        # Add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setFont(font)
        self.chat_area.setReadOnly(True)
        self.chat_area.setGeometry(10, 10, 680, 380)
        # Add input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 400, 680, 40)
        self.input_field.returnPressed.connect(self.send_message)
        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(630, 450, 60, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#33C1FF'>User: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input).strip()
        self.chat_area.append(f"<p style='color:#33FF9C'>ChatBot: {response}</p>")



app = QApplication(sys.argv)
main_window = ChatBotWindow()
qdarktheme.setup_theme()
sys.exit(app.exec())
