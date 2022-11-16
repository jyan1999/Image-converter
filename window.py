from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox,QApplication
from PyQt6.QtCore import Qt
from convert import convert
import os 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,200,600,400)
        self.setAcceptDrops(True)
        self.imgLabel = ImageLabel()
        self.status = StatusLabel()
        #hardcoded from pillow docs
        self.items = sorted(["JPG","PNG","HEIC","PDF","TIFF","PPM"])
        self.supported_input = {"jpeg","jpg","png","heic","ppm", "blp",'bmp','dds','dib','eps','gif','icns','ico','im','msp','pcx','tiff', 'sgi','spider','tga','xbm'}
        self.dropdown = self.create_comboBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dropdown)
        mainLayout.addWidget(self.imgLabel)
        mainLayout.addWidget(self.status)
        self.setLayout(mainLayout)

        self.target = self.items[0]
    
    def change_target(self, text):
        self.target = text
    
    def acceptable(self,urls):
        for url in urls:
            extension = os.path.splitext(url)[1][1:]
            if extension.lower() not in self.supported_input:
                return False 
        return True
    
    def create_comboBox(self):
        combobox = QComboBox()
        combobox.setMaximumWidth(200)
        combobox.addItems(self.items)
        combobox.currentTextChanged.connect(self.change_target)
        return combobox

    
    def dragEnterEvent(self, event):
        event.accept()
        urls = event.mimeData().urls()
        urls = [url.toLocalFile() for url in urls]
        if self.acceptable(urls):
            self.status.setText("Images detected, release to start")
        else:
            self.status.setText("File formats not supported")
        
    def dragLeaveEvent(self,event):
        event.accept()
        self.status.setText("\n\nAccepting Images\n\n")
    
    def dropEvent(self, event):
        event.accept()
        urls = event.mimeData().urls()
        urls = [url.toLocalFile() for url in urls]
        if self.acceptable(urls):
            event.setDropAction(Qt.DropAction.CopyAction)
            self.status.setText("Image accepted, processing")
            self.status.repaint()
            QApplication.processEvents()
            self.status.update()
            for url in urls:
                convert(url,self.target)
        self.status.setText("\n\nAccepting Images\n\n")




class ImageLabel(QLabel):
    def __init__(self) -> None:
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("\n\nDrop Image here\n\n")
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

class StatusLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("\n\nAccepting Images\n\n")
        self.setMaximumHeight(100)
