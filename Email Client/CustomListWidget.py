import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngineWidgets
from functools import partial

class CustomListWidgetItem (QWidget):
    def __init__ (self, parent = None):
        super().__init__(parent)
        self.FromQLabel    = QLabel()
        self.FromQLabel.setObjectName("From")
        self.FromQLabel.setFixedWidth(200)
        # self.FromQLabel.setMinimumWidth(100)
        
        
        self.SubjectQLabel  = QLabel()
        self.SubjectQLabel.setObjectName("Subject")
        self.SubjectQLabel.setMinimumWidth(100)
        # self.SubjectQLabel.setMaximumWidth(150)
        
        
        self.allQHBoxLayout = QHBoxLayout()
        self.SnippetQLabel  = QLabel()
        self.SnippetQLabel.setObjectName("Snippet")
        # self.SnippetQLabel.setMaximumWidth(150)
        self.SnippetQLabel.setMinimumWidth(100)
        
        
        self.allQHBoxLayout.addWidget(self.FromQLabel, 0)
        self.allQHBoxLayout.addWidget(self.SubjectQLabel, 1)
        self.allQHBoxLayout.addWidget(self.SnippetQLabel, 2)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        # self.textUpQLabel.setStyleSheet('''
        #     color: rgb(0, 0, 255);
        # ''')
        # self.textDownQLabel.setStyleSheet('''
        #     color: rgb(255, 0, 0);
        # ''')

    def setTextUp (self, text):
        self.FromQLabel.setText(text)

    def setTextDown (self, text):
        self.SubjectQLabel.setText(text)

    def setSnippet (self, text):
        self.SnippetQLabel.setText(text)
class exampleQMainWindow (QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget = QListWidget(self)
        for index, name, icon in [
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = CustomListWidgetItem()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setSnippet(icon)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.setCentralWidget(self.myQListWidget)

if __name__=="__main__":

    app = QApplication([])
    window = exampleQMainWindow()
    window.show()
    sys.exit(app.exec_())