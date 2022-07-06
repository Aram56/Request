from pprint import pprint
from ya_disk import YandexDisk
import requests
import os

# D:\Арам\Нетология\ДЗ\requests\Aram_test.txt

TOKEN = " "

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()    
    
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
       
    
    def upload(self, file_path: str):
    #     """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(disk_file_path="Загрузки").get("href", "")
        print(href)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        
          
        # Тут ваша логика
        # Функция может ничего не возвращать

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.get_files_list()
    # pprint(ya.get_files_list())
    file_path: path_to_file
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Aram_test.txt'
    token = YandexDisk(token=TOKEN)
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)






