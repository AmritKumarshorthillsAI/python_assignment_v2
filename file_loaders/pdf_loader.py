import os
from PyPDF2 import PdfReader
# The PdfReader class from the PyPDF2 library is used to read PDF files in Python. It allows you to extract 
# information from PDF documents, such as text, metadata, and more.
from file_loaders.file_loader import FileLoader

class PDFLoader(FileLoader):
    

    def validate_file(self, file_path: str) -> bool:
        return file_path.lower().endswith('.pdf')

    def load_file(self, file_path: str) -> PdfReader:
        if not self.validate_file(file_path):
            raise ValueError("Invalid PDF file.")
        return PdfReader(file_path)

    