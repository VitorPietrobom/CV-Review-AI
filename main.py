import sys
from PyQt5.QtWidgets import QApplication
from pdf_processor_gui import pdf_processor_gui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = pdf_processor_gui()
    gui.show()
    sys.exit(app.exec_())
