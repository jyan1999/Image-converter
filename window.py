from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox,QApplication, QFileDialog
from PyQt6.QtCore import Qt
from convert import convert, acceptable
import time 

#hardcoded from pillow docs
SUPPORTED_INPUTS = {"jpeg","jpg","png","heic","ppm", "blp",'bmp','dds','dib','eps','gif','icns','ico','im','msp','pcx','tiff', 'sgi','spider','tga','xbm'}
SUPPORTED_OUTPUTS = sorted(["JPG","PNG","HEIC","PDF","TIFF","PPM"])

class StatusLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("\n\nAccepting Images\n\n")
        self.setMaximumHeight(100)

#Putting these in global so all widgets have access to them
#whacky hacks but work
status = StatusLabel()
target = SUPPORTED_OUTPUTS[0]

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,200,600,400)
        self.setAcceptDrops(True)
        self.imgLabel = ImageLabel()
        self.status = status
        self.dropdown = self.create_comboBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dropdown)
        mainLayout.addWidget(self.imgLabel)
        mainLayout.addWidget(self.status)
        self.setLayout(mainLayout)

    
    def change_target(self, text):
        target = text
    
    def create_comboBox(self):
        combobox = QComboBox()
        combobox.setMaximumWidth(200)
        combobox.addItems(SUPPORTED_OUTPUTS)
        combobox.currentTextChanged.connect(self.change_target)
        return combobox

    
    def dragEnterEvent(self, event):
        event.accept()
        urls = event.mimeData().urls()
        urls = [url.toLocalFile() for url in urls]
        if acceptable(urls,SUPPORTED_INPUTS):
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
        if acceptable(urls, SUPPORTED_INPUTS):
            event.setDropAction(Qt.DropAction.CopyAction)
            self.status.setText("Image accepted, processing")
            self.status.repaint()
            QApplication.processEvents()
            for url in urls:
                convert(url,target)
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
    
    
    def mousePressEvent(self, event) -> None:
        event.accept()
    
    def mouseReleaseEvent(self, event) -> None:
        event.accept()
        urls = QFileDialog.getOpenFileUrls(self,"open files")[0]
        urls = [url.toLocalFile() for url in urls]
        if acceptable(urls,SUPPORTED_INPUTS):
            for url in urls:
                status.setText("Image accepted, processing")
                status.repaint()
                QApplication.processEvents()
                convert(url,target)
        else:
            status.setText("File formats not supported")
            status.repaint()
            QApplication.processEvents()
            time.sleep(2)
        status.setText("\n\nAccepting Images\n\n")
            
