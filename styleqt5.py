from PyQt5.QtWidgets import QApplication, QPushButton
app = QApplication([])
app.setStyleSheet("QPushButton {  background-color: yellow; margin: 100px; font-size:24px  }")
button = QPushButton('Hello World')
button.show()
app.exec()