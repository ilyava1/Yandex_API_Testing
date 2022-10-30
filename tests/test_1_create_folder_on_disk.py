import unittest
import requests
from parameterized import parameterized
from service_modules.sys_service import load_env_variables, write_token
from service_modules.ya_service import YaUploader

FIXTURES = [
    ('00_test', 'Папка 00_test создана'),
    ('00_test', 'Папка 00_test уже существует на Я.Диске')
]


class TestClass_1_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_create_folder_on_disk(self, folder_name, expected_result):
        config = load_env_variables()
        if 'YA_TOKEN'not in config.keys():
            config = write_token(config)
        token = config['YA_TOKEN']
        uploader = YaUploader(token)
        result = uploader.create_folder_on_disk(folder_name)
        self.assertEqual(result, expected_result)

