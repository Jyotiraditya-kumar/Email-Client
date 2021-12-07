from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
from DATABASE import EmailDatabase
from CustomListWidget import CustomListWidgetItem
# import sqlite3
# con=sqlite3.connect("emails.db")
# cur=con.cursor()

import os

class Page1(QWidget):
    def __init__(self,controller=None,label="Inbox"):
        super().__init__()
        self.controller=controller
        self.setup()
        
    def setup(self):
        # self.frame=QWidget(self)
        MainLayout=QVBoxLayout()
        
        subLayout=QHBoxLayout()
        self.subWidget=QWidget()
        self.l=QLabel()
        self.l.setText("INBOX")
        self.RefreshButton=QPushButton("Refresh")
        self.RefreshButton.setMaximumWidth(100)
        
        subLayout.addWidget(self.l,stretch=5)
        subLayout.addWidget(self.RefreshButton,stretch=1)
        self.subWidget.setLayout(subLayout)
        
        self.List=QListWidget()
        self.List.setSelectionMode(QAbstractItemView.SingleSelection)
        self.List.itemClicked.connect(self.Item_Click)
        MainLayout.addWidget(self.subWidget)
        MainLayout.addWidget(self.List)
        # MainLayout.addWidget(self.b)
        self.setLayout(MainLayout)
        self.fill_data("INBOX")
     
        
    def fill_data(self,label):
        print(label)
        self.l.setText(label)
        # lst=cur.execute("select * from Messages")
        mngdb=EmailDatabase()
        query={"Labels":label}
        lst=mngdb.fetch(query)
        self.List.clear()
        # print(lst)
        for i in lst:
            myQCustomQWidget = CustomListWidgetItem()
            myQCustomQWidget.setTextUp(i["From"].split("<")[0])
            myQCustomQWidget.setTextDown(i["Subject"])
            myQCustomQWidget.setSnippet(i["Snippet"][:100])
            # myQCustomQWidget.setID(i["_id"])
            myQListWidgetItem = QListWidgetItem(self.List)
            myQListWidgetItem.setToolTip(i["_id"])
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.List.addItem(myQListWidgetItem)
            self.List.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            
            # print(i)
            # text="From : {:50} {:40}".format(i["From"].split("<")[0][:30],i["Snippet"][:40])
            # l=QListWidgetItem(text)
            # l.setToolTip(i["_id"])
            # self.List.addItem(l)
        mngdb.Close()
        # path=os.path.join("email_data")
        # l=os.listdir(path)
    
    def Item_Click(self):
        x=self.List.selectedItems()
        i=(x[0],x[0].toolTip())
        print(i)
        # print(x[0].toolTip())
        self.controller.next_page(i[1])
    
if __name__ == '__main__':

    app = QApplication([])
    ex = Page1()
    ex.resize(800,300)
    ex.show()
    app.exec()