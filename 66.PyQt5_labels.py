#PyQt5 intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI")
        self.setGeometry(700,300,500,500) #(100, y, height, width)
        label = QLabel("Hello",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: red;"
                            "background-color:Black;"
                            "font:bold;"
                            "font-style:itallic;"
                            "text-decoration:underline;")
        
        #label.setAlignment(Qt.AlignBottom) VERTICALLY TOP
        #label.setAlignment(Qt.AlignVCenter) VERTICALLY BOTTOM


        #label.setAlignment(Qt.AlignRight) HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignLeft) HORIZONTALLY LEFT

        #label.setAlignment (Qt.AlignHCenter | Qt.AlignTop)
      #  label.setAlignment (Qt.AlignHCenter | Qt.AlignTop) #Centerand top
       # label.setAlignment (Qt.AlignHCenter | Qt.AlignBottom) #Center and bottom
       # label.setAlignment (Qt.AlignHCenter | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignCenter)



        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
 main()