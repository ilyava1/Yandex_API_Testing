import requests
import datetime


def upload_starter(config):
    uploader = YaUploader(config['YA_TOKEN'])
    disk_file_path = config['DISK_FILE_PATH']
    filename = config['FILENAME']
    print()

    # Выделяем из пути на диске имя папки
    list1 = list(disk_file_path)
    list2 = list1
    for letter in reversed(list1):
        if letter != '/':
            list2.pop(-1)
        else:
            list2.pop(-1)
            break
    folder_name = ''.join(list2)

    print(f'{uploader.get_user_info().capitalize()}, файл {filename}'
          f' будет загружен в папку {folder_name} на вашем Я.Диске')

    uploader.create_folder_on_disk(folder_name)

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.now()} - пользователь:'
                   f' {uploader.get_user_info()} - тестирование'
                   f' загрузки на Яндекс.Диск - в папку {folder_name} - '
                   f'загружен файл {filename}\n')

    uploader.upload_file_to_disk(disk_file_path, filename)

    print()
    return

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_folder_on_disk(self, folder_name):
        create_folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(create_folder_url, headers=headers,
                                params=params)
        if response.status_code == 201:
            print()
            result = f'Папка {folder_name} создана'
            print()
            print(result)
        elif response.status_code == 409:
            result = f'Папка {folder_name} уже существует на Я.Диске'
            print()
            print(result)
        else:
            result = f'Ответ сервиса на запрос по созданию папки: {response.json()}'
            print()
            print(result)
            print()

        return result

    def get_user_info(self):
        user_info_url = "https://cloud-api.yandex.net/v1/disk"
        headers = self.get_headers()
        response = requests.get(user_info_url, headers=headers)

        return response.json()['user']['display_name']

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return(response.json())

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print()
            print(f'Файл {filename} успешно загружен на Диск')
        else:
            print()
            print(response.json())
        return


    def delete_folder_from_disk(self, folder_name):
        delete_folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.delete(delete_folder_url, headers=headers,
                                params=params)
        if response.status_code == 204:
            print()
            result = f'Папка {folder_name} удалена с Я.Диска'
            print(result)
        else:
            result = f'Папка {folder_name} не может быть удалена с Я.Диска'
            print(result, '. Response.status_code = ', response.status_code)
        return result