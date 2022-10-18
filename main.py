import requests
from pprint import pprint

heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = "https://akabab.github.io/superhero-api/api/"
response = requests.get(url + 'all.json')
r_j = response.json()
for l in r_j:
    name = l['name']
    target = l['powerstats']['intelligence']
    if name in heroes_list:
        intelligence_dict[l['name']] = l['powerstats']['intelligence']
print(max(intelligence_dict, key=intelligence_dict.get))
#


class my_files_upload:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        source = requests.get(upload_url, headers = headers, params = params)
        source_getted = source.json()
        href = source_getted.get("href", "")
        result = requests.put(href, data = open(filename, 'rb'))
        return result

if __name__ == '__main__':
    token = "y0_AgAAAAB........."
    uploader = my_files_upload(token)
    pprint(uploader.upload('first.txt', "second.txt"))
