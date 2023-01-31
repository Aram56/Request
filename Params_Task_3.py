from pprint import pprint
import requests

from fake_headers import Headers




def test_request():
    headers = Headers(browser='firefox', os='win').generate()
    url = "https://api.stackexchange.com/docs/questions"
    # params = {"fromdate": "2023-01-30", "todate": "2023-01-31", "tagged": "python"}
    params = {"fromdate": 1674950400, "todate": "1675036800", "tagged": "python"}
    response = requests.get(url, headers=headers, params=params, timeout=5)
    pprint(response)
    
    pprint(response.text)


if __name__ == '__main__':
    
    test_request()
