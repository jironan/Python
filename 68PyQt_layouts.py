import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.initUI()

    def initUI(self):
         central_widget = QWidget()
         self.setCentralWidget(central_widget)

         label1  = QLabel("#1",self)
         label2  = QLabel("#2",self)
         label3  = QLabel("#3",self)
         label4  = QLabel("#4",self)
         label5  = QLabel("#5",self)

         label1.setStyleSheet("background-color:red;")
         label2.setStyleSheet("background-color:yellow;")
         label3.setStyleSheet("background-color:blue;")
         label4.setStyleSheet("background-color:purple;")
         label5.setStyleSheet("background-color:green;")

        # vbox = QVBoxLayout() Vertical Layout
         # vbox = QHBoxLayout() Horizontal Layout
         vbox = QGridLayout() #Grid Layout

         vbox.addWidget(label1,0,0)
         vbox.addWidget(label2,0,1)
         vbox.addWidget(label3,1,0)
         vbox.addWidget(label4,1,1)
         vbox.addWidget(label5,1,2)

        
         central_widget.setLayout(vbox) #Horizontal Layout

        


def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()