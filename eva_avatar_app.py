
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QLineEdit, QPushButton, QTextEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import datetime

class EvaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EVA – Assistente da AZ Car Rental")
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        # Avatar da Eva
        self.avatar = QLabel(self)
        pixmap = QPixmap("Eva-avatar_1.png").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.avatar.setPixmap(pixmap)
        self.avatar.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.avatar)

        # Campo de exibição do diálogo
        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        layout.addWidget(self.chat_box)

        # Campo de entrada do usuário
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Digite sua pergunta aqui...")
        layout.addWidget(self.input)

        # Botão de enviar
        self.send_button = QPushButton("Enviar", self)
        self.send_button.clicked.connect(self.enviar_mensagem)
        layout.addWidget(self.send_button)

        self.setLayout(layout)
        self.saudacao_inicial()

    def saudacao_inicial(self):
        agora = datetime.datetime.now()
        msg = f"Olá! Eu sou a Eva, sua assistente da AZ Car Rental. Hoje é {agora.strftime('%A, %d de %B de %Y')}, {agora.strftime('%H:%M:%S')}.
Como posso te ajudar?"
        self.chat_box.append(f"Eva: {msg}")

    def enviar_mensagem(self):
        texto_usuario = self.input.text()
        if not texto_usuario.strip():
            return
        self.chat_box.append(f"Você: {texto_usuario}")
        resposta = self.gerar_resposta(texto_usuario)
        self.chat_box.append(f"Eva: {resposta}")
        self.input.clear()

    def gerar_resposta(self, pergunta):
        pergunta = pergunta.lower()
        if "família" in pergunta:
            return "Uma viagem em família? Que legal! Recomendo uma SUV ou uma minivan para mais conforto."
        elif "trabalho" in pergunta:
            return "Para negócios, os sedãs executivos são ideais. Posso mostrar alguns modelos."
        elif "econômico" in pergunta or "barato" in pergunta:
            return "Temos carros super econômicos para ajudar no seu bolso. Quer ver?"
        elif "seguro" in pergunta:
            return "Todos os carros contam com opções de seguro básico ou completo. Deseja saber os valores?"
        else:
            return "Posso te ajudar com recomendações personalizadas. Me diga: é uma viagem de lazer, trabalho ou outro motivo?"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = EvaApp()
    janela.show()
    sys.exit(app.exec_())
