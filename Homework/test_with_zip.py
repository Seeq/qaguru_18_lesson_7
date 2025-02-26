import csv
import os
import pytest
from pypdf import PdfReader
from zipfile import ZipFile
from Homework.conftest import ARCHIVE_FILE_PATH



def test_pdf():

    with ZipFile(ARCHIVE_FILE_PATH) as zip_file:
        with zip_file.open("Python Testing with Pytest (Brian Okken).pdf") as pdf:
            pdf_reader = PdfReader(pdf)
            count_of_pages = len(pdf_reader.pages)

            assert count_of_pages > 0
            assert 'Pragmatic Bookshelf' in pdf_reader.pages[2].extract_text()

