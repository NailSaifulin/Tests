#####################################ТЕСТ_ЗАДАЧА-2###################################################

import pytest, requests
from main import YaUploader


class testCreate_folder_ya():
    def test_get_folder_ya(self):
        response = YaUploader()
        if response.get_folder("netology").status_code == 200:
            response.delete_folder("netology")

        assert response.create_folder("netology").status_code == 200