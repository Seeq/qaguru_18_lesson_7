from zipfile import ZipFile
import os
import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
CURRENT_PROJECT_PATH = os.path.dirname(CURRENT_DIRECTORY)
TMP_FILES_PATH = os.path.join(CURRENT_PROJECT_PATH, "tmp")
ARCHIVE_FILE_PATH = os.path.join(TMP_FILES_PATH, "archive_files.zip")


@pytest.fixture(scope='function', autouse=True)
def create_archive():

    with ZipFile(ARCHIVE_FILE_PATH, 'w') as zip_file:
        for file in os.listdir(TMP_FILES_PATH):
            zip_file.write(os.path.join(TMP_FILES_PATH, file), file)

    yield

    os.remove(ARCHIVE_FILE_PATH)