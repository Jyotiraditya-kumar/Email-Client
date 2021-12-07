from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
import sys
from email_test import GetMessage
# from DATABASE import EmailDatabase
# from CustomListWidget import CustomListWidgetItem

class TextEditor(QMainWindow):

    def __init__(self,controller=None,glogin=None):
        super().__init__()

        self.initUI()
        self.glogin=glogin


    def initUI(self):
        
        
        self.cWidget=QWidget()
        self.setCentralWidget(self.cWidget)
        
        mainLayout=QVBoxLayout() 
        formLayout=QFormLayout()
        self.textEdit = QTextEdit()
        
        self.formWidget=QWidget(self)
        self.FromEdit=QLineEdit()
        self.ToEdit=QLineEdit()
        self.SubjectEdit=QLineEdit()
        formLayout.addRow("From",self.FromEdit)
        formLayout.addRow("To",self.ToEdit)
        formLayout.addRow("Subject",self.SubjectEdit)
        self.sendButton=QPushButton("Send")
        formLayout.addWidget(self.sendButton)
        self.formWidget.setLayout(formLayout)
        # self.add
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setTextColor(QColor("Red"))
        self.textEdit.setFontPointSize(20)
        mainLayout.addWidget(self.formWidget,stretch=1)
        mainLayout.addWidget(self.textEdit,stretch=5)
        

        boldAct = QAction(QIcon('icons/bold.png'), 'Bold', self)
        boldAct.setShortcut('Ctrl+B')
        boldAct.setStatusTip('Bold Text')
        # boldAct.triggered.connect(self.Bold)
        
        underlineAct=QAction(parent=self,icon=QIcon("undeline.png"),text='Underline')
        boldAct.setShortcut('Ctrl+U')
        boldAct.setStatusTip('Underline Text')
        boldAct.triggered.connect(self.textUnderline)
        
        
        self.cWidget.setLayout(mainLayout)
        
        self.sendButton.clicked.connect(self.sendMessage)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(boldAct)

        # self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        # self.show()
    def sendMessage(self):
        From=self.FromEdit.text()
        To=self.ToEdit.text()
        Subject=self.SubjectEdit.text()
        a=GetMessage(From,To,Subject)
        msg=[[self.textEdit.toPlainText() ,"plain"],[self.textEdit.toHtml(),"html"]]
        a.create_message(msg)
        msg1=a.returnMessage()
        print(msg1)
        x=self.glogin.send_message(msg1)
        
        
    def textUnderline(self):
        if self.textEdit.fontUnderline():
            self.textEdit.setFontUnderline(False)
        else:
            self.textEdit.setFontUnderline(True)
        x=self.textEdit.toHtml()
        print(x)
    def textBold(self):
        if self.textEdit.fontBold():
            self.textEdit.setFontWeight()
        else:
            self.textEdit.setFontUnderline(True)
        


# def main():
#     app = QApplication(sys.argv)
#     ex = TextEditor()
#     ex.resize(1000,720)
#     sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication([])
    # app.setStyleSheet(open('Stylesheet.css').read()) 
    ex = TextEditor()
    ex.resize(1280,720)
    ex.show()
    app.exec()