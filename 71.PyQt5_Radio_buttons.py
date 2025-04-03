import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Buttons")
        self.setGeometry(700, 300, 500, 500)  # (x, y, width, height)
        self.setWindowIcon(QIcon("Python\\czard.jpg"))

        # Create radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("Store", self)
        self.radio5 = QRadioButton("Online", self)

        # Grouping the radio buttons
        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup1.addButton(self.radio1)
        self.buttonGroup1.addButton(self.radio2)
        self.buttonGroup1.addButton(self.radio3)

        self.buttonGroup2 = QButtonGroup(self)
        self.buttonGroup2.addButton(self.radio4)
        self.buttonGroup2.addButton(self.radio5)

        

        self.radio1.setGeometry(50, 50, 300, 50)
        self.radio2.setGeometry(50, 100, 300, 50)
        self.radio3.setGeometry(50, 150, 300, 50)
        self.radio4.setGeometry(50, 200, 300, 50)
        self.radio5.setGeometry(50, 250, 300, 50)

       

        self.setStyleSheet("QRadioButton {"
                           "font-family: Arial;"
                           "font-size: 30px;"
                           "padding: 10px;"
                           "}")
        
        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)
    
    def radio_button_change(self):
        radio_buttond = self.sender()
        if radio_buttond.isChecked():
            print(f"{radio_buttond.text()} is selected ")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
