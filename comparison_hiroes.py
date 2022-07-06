from pprint import pprint
import requests

list_hiroes = ['Hulk', 'Captain America', 'Thanos']

def test_request():
    url = "https://akabab.github.io/superhero-api/api//all.json"
    response = requests.get(url=url)
    full_info = (response.json())
    intelect_hiroes = {}    
    for hiro in full_info:
        if hiro['name'] in list_hiroes:
            intelect_hiroes[hiro['name']] = hiro['powerstats']['intelligence']
    max_int_hiro_name = max(intelect_hiroes, key=intelect_hiroes.get)
    val_max_int_hiro = max(intelect_hiroes.values())
    pprint(f"Герой {max_int_hiro_name} - самый умный. Его интелект равен {val_max_int_hiro}")
 

if __name__ == '__main__':
    test_request()