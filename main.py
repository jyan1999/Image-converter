from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication([])
    from window import Window 
    window = Window()
    window.show()
    sys.exit(app.exec())
