from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
import datetime as time
from DATABASE import EmailDatabase


# from DATABASE import fetch_data

import os

class Page2(QWidget):
    def __init__(self,controller=None):
        super().__init__()
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        self.controller=controller
        self.setup()
    def setup(self):
        mainLayout=QVBoxLayout()
        headerWidget=QWidget()
        headerLayout=QVBoxLayout()
        subheaderWidget=QWidget()
        subheaderLayout=QHBoxLayout()
        self.SubjectLabel=QLabel()
        self.SubjectLabel.setText("Subject")
        self.SubjectLabel.setObjectName("Subject2")
        self.FromLabel=QLabel()
        self.FromLabel.setText("From")
        self.ToLabel=QLabel()
        self.ToLabel.setText("To")
        self.DateLabel=QLabel()
        self.DateLabel.setText("Date")
        self.BackButton=QPushButton()
        self.BackButton.setText("<-")
        self.BackButton.setFixedWidth(10)
        
        
        
        
        
        self.BackButton.clicked.connect(self.controller.prev_page)
        
        self.webEngineView = QtWebEngineWidgets.QWebEngineView()
        # self.webEngineView.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        s=self.webEngineView.settings().WebAttribute
        s.AutoLoadIconsForPage=True
        s.LocalContentCanAccessRemoteUrls=True
        s.AllowRunningInsecureContent=True
        s.JavascriptEnabled=True
        s.JavascriptCanOpenWindows=True
        s.PdfViewerEnabled=True
        # print(s)
        # self.webEngineView.setMinimumWidth(800)
        self.webEngineView.loadStarted.connect(self.loadStartedHandler)
        self.webEngineView.loadProgress.connect(self.loadProgressHandler)
        self.webEngineView.loadFinished.connect(self.loadFinishedHandler)

    
        
        
        # with open("Part 0.txt") as f:
        #     Text=f.read()
        # Label_Text=QLabel()
        # Label_Text.setText(Text)
        subheaderLayout.addWidget(self.FromLabel)
        subheaderLayout.addWidget(self.DateLabel)
        subheaderWidget.setLayout(subheaderLayout)
        
        
        headerLayout.addWidget(self.SubjectLabel)
        headerLayout.addWidget(subheaderWidget)
        headerLayout.addWidget(self.ToLabel)
        headerLayout.addWidget(self.BackButton)
        headerWidget.setLayout(headerLayout)
        # mainLayout.addWidget(Label_Text)
        mainLayout.addWidget(headerWidget)
        mainLayout.addWidget(self.webEngineView,stretch=5)
        self.setLayout(mainLayout)
    
    @QtCore.pyqtSlot()
    def loadStartedHandler(self):
        print(time.time(), ": load started")

    @QtCore.pyqtSlot(int)
    def loadProgressHandler(self, prog):
        print(time.time(), ":load progress", prog)

    @QtCore.pyqtSlot()
    def loadFinishedHandler(self):
        print(time.time(), ": load finished")
    def load_widget(self,Id):
        file_path = os.path.join(self.CURRENT_DIR, 'email test',Id)
        files=os.listdir(file_path)
        l=[0,0]
        for file in files:
            if file.endswith(".html"):
                l[1]=file
            elif file.endswith(".txt"):
                l[0]=file
                
                
        if l[1]:
            filename = l[1]
        elif  l[0]:
            filename=l[0]
        filename=os.path.join(file_path,filename)
        query={"_id":Id}
        mngdb=EmailDatabase()
        headers=mngdb.fetch(query)[0]
        # headers=fetch_data(Id)
        self.SubjectLabel.setText(headers["Subject"])
        self.FromLabel.setText(headers["From"])
        self.ToLabel.setText(headers["To"])
        self.DateLabel.setText(headers["Date"])
        print("Loading .........")
        # filename=os.path.join(self.CURRENT_DIR,"SACHIN_PROOF.pdf")
        
        self.webEngineView.load(QtCore.QUrl().fromLocalFile(filename))
        print(self.webEngineView.loadProgress)
        print("Loaded.......................")
        # return(self.frame)
    def Item_Click(self):
        print("Hello")
    
if __name__ == '__main__':

    app = QApplication([])
    ex = Page2()
    # l=Email_Page()
    # ex.insert_page(l)
    # page1=Page1()
    # ex.insert_page(page1.return_widget())
    # for i in range(10):
    #     ex.insert_page(QLabel(f'This is page {i+1}'))
    ex.resize(800,300)
    ex.show()
    app.exec()