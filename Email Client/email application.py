from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
from functools import partial


from Page_1 import Page1
from Page_2 import Page2
from TEXTEDIT import TextEditor
from GoogleLogin import Login

import os

class EmailApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.glogin=Login()
        # self.gservice=glogin.service
        self.initUI()
        

    def initUI(self):
        hbox1=QHBoxLayout(self)
        vbox1=QVBoxLayout()
        line=QFrame()
        line.setGeometry(30,0,61,301)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        vbox2=QVBoxLayout()
        
        buttons=[None for i in range(5)]
        b_label=["INBOX","OUTBOX","SENT","DRAFT","TRASH"]
        composeButton=QPushButton("Compose Email")
        composeButton.clicked.connect(self.ComposePage)
        for i in range(5):
            buttons[i] = QPushButton(f"{b_label[i]}",toolTip=b_label[i])
            buttons[i].clicked.connect(partial(self.show_category,b_label[i]))
        
        vbox1.addWidget(composeButton)   
        for button in buttons:
            vbox1.addWidget(button)

        w1=QWidget()
        w2=QWidget()
        w1.setLayout(vbox1)
        w1.setMaximumWidth(200)
        self.stacked_widget = QStackedWidget(w2)
        
        vbox2.addWidget(self.stacked_widget)
        # vbox2.addLayout(hbox3)
        w2.setLayout(vbox2)
        # w1.setGeometry()
        hbox1.addWidget(w1,stretch=1)
        hbox1.addWidget(line)
        # hbox1.addStretch(2)
        hbox1.addWidget(w2,stretch=3)
        

        self.setLayout(hbox1)
        
        
        page1=Page1(self)
        page2=Page2(self)
        textEdit=TextEditor(self,self.glogin)
        self.page2_controller=page2
        self.page1_controller=page1
        self.text_edit_controller=textEdit
        
        self.insert_page(page1)
        self.insert_page(page2)
        self.insert_page(textEdit)
    def show_category(self,label):
        self.page1_controller.fill_data(label)
        self.stacked_widget.setCurrentIndex(0)

    def insert_page(self, widget, index=-1):
        self.stacked_widget.insertWidget(index, widget)
        # self.set_button_state(self.stacked_widget.currentIndex())
    def ComposePage(self):
        self.stacked_widget.setCurrentIndex(2)

    def next_page(self,Id):
        new_index = self.stacked_widget.currentIndex()+1
        self.stacked_widget.setCurrentIndex(new_index)
        self.page2_controller.load_widget(Id)

    def prev_page(self):
        new_index = self.stacked_widget.currentIndex()-1
        if new_index >= 0:
            self.stacked_widget.setCurrentIndex(new_index)
            # self.stacked_widget.widgetRemoved()
    def Item_Click(self):
        print("Hello")
    

if __name__ == '__main__':

    app = QApplication([])
    app.setStyleSheet(open('Stylesheet.css').read()) 
    ex = EmailApplication()
    ex.resize(1280,720)
    ex.show()
    app.exec()