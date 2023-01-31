from pprint import pprint
import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()
       
    
    def upload_file_to_disk(self, disk_file_path, filename):
        result = self._get_upload_link(disk_file_path=disk_file_path)
        href = result.get("href", "")
        # print(href)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
    
    def upload(self, file_path: str):
        full_file = os.path.basename(file_path) 
        # path_and_name_load = f'Комуналка/{file}' # Если надо указать конкретный каталог для файла
        # self.upload_file_to_disk(path_and_name_load, full_file)
        self.upload_file_to_disk({file}, full_file) 
       

if __name__ == '__main__':
    file = "ONE.txt"
    path_to_file = os.path.join(r"D:\Арам\Нетология\ДЗ\requests", file)
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)






