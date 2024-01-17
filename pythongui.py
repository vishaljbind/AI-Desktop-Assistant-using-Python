from Maingui import Ui_MainWindow
from PyQt6 import QtCore ,QtGui,QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt,QTimer,QTime,QDate
from PyQt6.uic import loadUiType
import ShaktiAI
import sys
import webbrowser as web
import subprocess


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        ShaktiAI.TaskExecution()

startExe = MainThread()
class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_Start.clicked.connect(self.startTask)
        self.gui.pushButton_Exit.clicked.connect(self.close)
        self.gui.pushButton_help.clicked.connect(self.help)
        self.gui.pushButton_chatmode.clicked.connect(self.ChatGPT)

    def startTask(self):
        self.gui.label = QtGui.QMovie("facerec.gif")
        self.gui.gif_1.setMovie(self.gui.label)
        self.gui.label.start()

        self.gui.label2 = QtGui.QMovie("__1.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.bg7 = QtGui.QMovie("Earth.gif")
        self.gui.gif_3.setMovie(self.gui.bg7)
        self.gui.bg7.start()

        self.gui.bg8 = QtGui.QMovie("B.G_Template_1.gif")
        self.gui.gif_4.setMovie(self.gui.bg8)
        self.gui.bg8.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def help(self):
        notepad_help_file = "help.txt"  
        try:
            subprocess.Popen(["hh", notepad_help_file])
        except FileNotFoundError:
            # Handle file not found error
            print("File not found or error opening the help file")
        

    def ChatGPT(self):
        web.open("https://chat.openai.com/")
        
        
        

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time:" + time
        label_date = "Date:" + date

        self.gui.textBrowser_Time.setText(label_time)
        self.gui.textBrowser_Date.setText(label_date)


    

if __name__=="__main__":
    GuiApp= QApplication(sys.argv)
    Ui_MainWindow = Gui_Start()
    Ui_MainWindow.show()
    exit(GuiApp.exec())


