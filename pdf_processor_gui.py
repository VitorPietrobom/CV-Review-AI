from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QScrollArea
from PyQt5.QtGui import QImage, QPixmap
import fitz  # PyMuPDF

class pdf_processor_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Processor')
        self.setGeometry(500, 100, 800, 1000) 

        main_layout = QHBoxLayout()

        # Vertical layout for PDF viewer and extracted text
        pdf_layout = QVBoxLayout()

        self.upload_label = QLabel('Upload PDF:')
        pdf_layout.addWidget(self.upload_label)

        self.upload_button = QPushButton('Select File')
        self.upload_button.clicked.connect(self.openFileDialog)
        pdf_layout.addWidget(self.upload_button)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.processPDF)
        pdf_layout.addWidget(self.submit_button)

        self.pdf_viewer_label = QLabel()
        pdf_layout.addWidget(self.pdf_viewer_label)

        main_layout.addLayout(pdf_layout)

        # Vertical layout for extracted text title and text
        extracted_text_layout = QVBoxLayout()

        self.extracted_text_title = QLabel('Extracted Text:')
        extracted_text_layout.addWidget(self.extracted_text_title)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        

        self.extracted_text_container = QWidget()
        self.extracted_text_container_layout = QVBoxLayout()
        self.extracted_text = QLabel()
        self.extracted_text_container_layout.addWidget(self.extracted_text)
        self.extracted_text_container.setLayout(self.extracted_text_container_layout)

        self.scroll_area.setWidget(self.extracted_text_container)
        extracted_text_layout.addWidget(self.scroll_area)

        main_layout.addLayout(extracted_text_layout)

        self.setLayout(main_layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)", options=options)
        if fileName:
            self.upload_label.setText(f'Uploaded file: {fileName}')
            self.displayPDF(fileName)

    def displayPDF(self, file_path):
        self.file_path = file_path
        doc = fitz.open(file_path)
        page = doc.load_page(0)
        pixmap = self.render_page(page)
        self.pdf_viewer_label.setPixmap(pixmap)
        self.extracted_text.setText(page.get_text())

    def render_page(self, page):
        pix = page.get_pixmap()
        img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        return QPixmap.fromImage(img)

    def processPDF(self):
        print("Processing PDF...")
        
