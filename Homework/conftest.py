import os
from zipfile import ZipFile

import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
CURRENT_PROJECT_PATH = os.path.dirname(CURRENT_DIRECTORY)
TMP_FILES_PATH = os.path.join(CURRENT_PROJECT_PATH, "tmp")
ARCHIVE_FILE_PATH = os.path.join(TMP_FILES_PATH, "tmp_zip.zip")


@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if os.path.exists(ARCHIVE_FILE_PATH):
        print(f"Удаляем старый архив: {ARCHIVE_FILE_PATH}")
        os.remove(ARCHIVE_FILE_PATH)

    print(f"Создаем новый архив: {ARCHIVE_FILE_PATH}")
    with ZipFile(ARCHIVE_FILE_PATH, 'w') as zip_file:
        for file in os.listdir(TMP_FILES_PATH):
            file_path = os.path.join(TMP_FILES_PATH, file)
            if os.path.isfile(file_path) and file != "tmp_zip.zip":
                print(f"Добавляем файл в архив: {file_path}")
                zip_file.write(file_path, file)

    yield

    if os.path.exists(ARCHIVE_FILE_PATH):
        os.remove(ARCHIVE_FILE_PATH)
