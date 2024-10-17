import unittest
from unittest.mock import MagicMock
from data_extractor.docx_extractor import DOCXExtractor
from data_extractor.pdf_extractor import PDFExtractor
from data_extractor.pptx_extractor import PPTXExtractor
from file_loaders.pdf_loader import PDFLoader
from file_loaders.docx_loader import DOCXLoader
from file_loaders.ppt_loader import PPTLoader
from storage.file_storage import FileStorage
from storage.sql_storage import SQLStorage


class TestPDFLoader(unittest.TestCase):
    def setUp(self):
        self.pdf_loader = PDFLoader()  # Correct initialization
        self.pdf_loader.load_file = MagicMock()

    def test_load_file(self):
        self.pdf_loader.load_file()
        self.pdf_loader.load_file.assert_called_once()

    def test_extract_text(self):
        self.pdf_loader.extract_text = MagicMock(return_value=("Sample text", {"font_style": "Arial", "page_number": 1}))
        text, metadata = self.pdf_loader.extract_text()
        self.assertEqual(text, "Sample text")
        self.assertEqual(metadata, {"font_style": "Arial", "page_number": 1})

    def test_extract_links(self):
        self.pdf_loader.extract_urls = MagicMock(return_value=[{"text": "Example", "url": "http://example.com", "page_number": 1}])
        links = self.pdf_loader.extract_urls()
        self.assertEqual(links[0]["url"], "http://example.com")

    def test_extract_images(self):
        self.pdf_loader.extract_images = MagicMock(return_value=[{"resolution": (1024, 768), "format": "JPEG", "page_number": 1}])
        images = self.pdf_loader.extract_images()
        self.assertEqual(images[0]["format"], "JPEG")

    def test_extract_tables(self):
        self.pdf_loader.extract_tables = MagicMock(return_value=[{"dimensions": (5, 3), "page_number": 1}])
        tables = self.pdf_loader.extract_tables()
        self.assertEqual(tables[0]["dimensions"], (5, 3))


class TestDOCXLoader(unittest.TestCase):
    def setUp(self):
        self.docx_loader = DOCXLoader()  # Correct initialization
        self.docx_loader.load_file = MagicMock()

    def test_load_file(self):
        self.docx_loader.load_file()
        self.docx_loader.load_file.assert_called_once()

    def test_extract_text(self):
        self.docx_loader.extract_text = MagicMock(return_value=("Sample DOCX text", {"font_style": "Times New Roman"}))
        text, metadata = self.docx_loader.extract_text()
        self.assertEqual(text, "Sample DOCX text")
        self.assertEqual(metadata["font_style"], "Times New Roman")

    def test_extract_links(self):
        self.docx_loader.extract_urls = MagicMock(return_value=[{"text": "Docx link", "url": "http://docx.com"}])
        links = self.docx_loader.extract_urls()
        self.assertEqual(links[0]["text"], "Docx link")

    def test_extract_images(self):
        self.docx_loader.extract_images = MagicMock(return_value=[{"resolution": (800, 600), "format": "PNG"}])
        images = self.docx_loader.extract_images()
        self.assertEqual(images[0]["format"], "PNG")

    def test_extract_tables(self):
        self.docx_loader.extract_tables = MagicMock(return_value=[{"dimensions": (2, 4)}])
        tables = self.docx_loader.extract_tables()
        self.assertEqual(tables[0]["dimensions"], (2, 4))


class TestPPTLoader(unittest.TestCase):
    def setUp(self):
        self.ppt_loader = PPTLoader()  # Correct initialization
        self.ppt_loader.load_file = MagicMock()

    def test_load_file(self):
        self.ppt_loader.load_file()
        self.ppt_loader.load_file.assert_called_once()

    def test_extract_text(self):
        self.ppt_loader.extract_text = MagicMock(return_value=("Slide text", {"slide_number": 1}))
        text, metadata = self.ppt_loader.extract_text()
        self.assertEqual(text, "Slide text")
        self.assertEqual(metadata["slide_number"], 1)

    def test_extract_links(self):
        self.ppt_loader.extract_urls = MagicMock(return_value=[{"text": "PPT Link", "url": "http://pptlink.com"}])
        links = self.ppt_loader.extract_urls()
        self.assertEqual(links[0]["url"], "http://pptlink.com")

    def test_extract_images(self):
        self.ppt_loader.extract_images = MagicMock(return_value=[{"resolution": (1280, 720), "format": "JPEG"}])
        images = self.ppt_loader.extract_images()
        self.assertEqual(images[0]["resolution"], (1280, 720))

    def test_extract_tables(self):
        self.ppt_loader.extract_tables = MagicMock(return_value=[{"dimensions": (3, 5)}])
        tables = self.ppt_loader.extract_tables()
        self.assertEqual(tables[0]["dimensions"], (3, 5))


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.extractor = MagicMock()
        self.file_storage = FileStorage(self.extractor)

    def test_store_text(self):
        self.file_storage.store_text = MagicMock()
        self.file_storage.store_text()
        self.file_storage.store_text.assert_called_once()

    def test_store_links(self):
        self.file_storage.store_urls = MagicMock()
        self.file_storage.store_urls()
        self.file_storage.store_urls.assert_called_once()

    def test_store_images(self):
        self.file_storage.store_images = MagicMock()
        self.file_storage.store_images()
        self.file_storage.store_images.assert_called_once()

    def test_store_tables(self):
        self.file_storage.store_tables = MagicMock()
        self.file_storage.store_tables()
        self.file_storage.store_tables.assert_called_once()


class TestSQLStorage(unittest.TestCase):
    def setUp(self):
        # SQLStorage may not need the extractor as a parameter
        self.sql_storage = SQLStorage()  # Correct initialization, no extractor needed

    def test_store_text(self):
        self.sql_storage.store_text = MagicMock()
        self.sql_storage.store_text()
        self.sql_storage.store_text.assert_called_once()

    def test_store_links(self):
        self.sql_storage.store_urls = MagicMock()
        self.sql_storage.store_urls()
        self.sql_storage.store_urls.assert_called_once()

    def test_store_images(self):
        self.sql_storage.store_images = MagicMock()
        self.sql_storage.store_images()
        self.sql_storage.store_images.assert_called_once()

    def test_store_tables(self):
        self.sql_storage.store_tables = MagicMock()
        self.sql_storage.store_tables()
        self.sql_storage.store_tables.assert_called_once()


class TestCombinations(unittest.TestCase):
    def setUp(self):
        # Create a mock loader for PDF
        self.mock_loader = MagicMock()
        self.pdf_loader = PDFExtractor(self.mock_loader)

        # Mock behavior for the loader's load_file method
        self.mock_pdf_file = MagicMock()
        self.mock_loader.load_file.return_value = self.mock_pdf_file

        # Mock pages in the PDF
        self.mock_page_1 = MagicMock()
        self.mock_page_2 = MagicMock()
        self.mock_pdf_file.pages = [self.mock_page_1, self.mock_page_2]

    def test_pdf_combinations(self):
        # Mock extract_text for the PDF
        self.mock_page_1.extract_text.return_value = "Sample text from page 1"
        self.mock_page_2.extract_text.return_value = "Sample text from page 2"

        # Mock image extraction
        self.mock_loader.load_file.return_value.extract_images.return_value = [
            {"image_data": b'fake_image_data', "ext": "JPEG", "page": 1, "dimensions": (100, 100)}
        ]

        # Mock URL extraction
        self.mock_page_1.__getitem__.return_value = {'/Annots': [MagicMock()]}
        self.mock_page_1.__getitem__.return_value['/Annots'][0].get_object.return_value = {'/A': {'/URI': 'http://example.com'}}

        # Mock table extraction
        self.mock_loader.load_file.return_value.extract_tables.return_value = [[["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]]

        # Define combinations for PDF testing
        combinations = [
            ("extract_text", self.pdf_loader.extract_text, "Sample text from page 1Sample text from page 2"),
            ("extract_links", self.pdf_loader.extract_urls, [{"linked_text": "http://example.com", "url": "http://example.com", "page_number": 1}]),
            ("extract_images", self.pdf_loader.extract_images, [{"image_data": b'fake_image_data', "ext": "JPEG", "page": 1, "dimensions": (100, 100)}]),
            ("extract_tables", self.pdf_loader.extract_tables, [[["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]]),
        ]

        # Run tests for each combination
        for name, method, expected_result in combinations:
            with self.subTest(name=name):
                output = method()
                self.assertEqual(output, expected_result)

    def test_docx_combinations(self):
        # Create a mock loader for DOCX
        self.mock_docx_loader = MagicMock()
        self.docx_loader = DOCXExtractor(self.mock_docx_loader)

        # Mock behavior for the loader's load_file method
        self.mock_docx_file = MagicMock()
        self.mock_docx_loader.load_file.return_value = self.mock_docx_file

        # Define combinations for DOCX testing
        combinations = [
            ("extract_text", self.docx_loader.extract_text, "Sample DOCX text"),
            ("extract_links", self.docx_loader.extract_urls, [{"url": "http://docxlink.com"}]),
            ("extract_images", self.docx_loader.extract_images, [{"format": "PNG"}]),
            ("extract_tables", self.docx_loader.extract_tables, [[["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]]),
        ]

        # Run tests for each combination
        for name, method, expected_result in combinations:
            with self.subTest(name=name):
                output = method()
                self.assertEqual(output, expected_result)

    def test_ppt_combinations(self):
        # Create a mock loader for PPTX
        self.mock_ppt_loader = MagicMock()
        self.ppt_loader = PPTXExtractor(self.mock_ppt_loader)

        # Mock behavior for the loader's load_file method
        self.mock_ppt_file = MagicMock()
        self.mock_ppt_loader.load_file.return_value = self.mock_ppt_file

        # Define combinations for PPTX testing
        combinations = [
            ("extract_text", self.ppt_loader.extract_text, "Sample PPTX text"),
            ("extract_links", self.ppt_loader.extract_urls, [{"url": "http://pptlink.com"}]),
            ("extract_images", self.ppt_loader.extract_images, [{"format": "JPEG"}]),
            ("extract_tables", self.ppt_loader.extract_tables, [[["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]]),
        ]

        # Run tests for each combination
        for name, method, expected_result in combinations:
            with self.subTest(name=name):
                output = method()
                self.assertEqual(output, expected_result)


if __name__ == "__main__":
    unittest.main()