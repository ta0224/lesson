from bs4 import BeautifulSoup as BS
import requests


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None



def get_data(html):
    soup = BS(html, 'html.parser')
    print(soup)




def main():
    URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
    html = get html(URL)
    get_data(html)


 if __name__ == '__main__':
    main()