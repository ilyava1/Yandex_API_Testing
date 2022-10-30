import unittest
from parameterized import parameterized
from service_modules.ya_service import YaUploader
from service_modules.sys_service import load_env_variables

FIXTURES = [
    ('00_test', 'Папка 00_test удалена с Я.Диска'),
    ('11_test', 'Папка 11_test не может быть удалена с Я.Диска')
]


class TestClass_2_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_delete_folder_from_disk(self, folder_name, expected_result):
        config = load_env_variables()
        token = config['YA_TOKEN']
        uploader = YaUploader(token)
        result = uploader.delete_folder_from_disk(folder_name)
        self.assertEqual(result, expected_result)

