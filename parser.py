import requests
from bs4 import BeautifulSoup as bs


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
base_url = 'https://hypeauditor.com/top-instagram-all-ukraine/?p={page_num}'


def bloggers_username_pars():
    blogger_list = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        for i in range(1,4):
            url = f'https://hypeauditor.com/top-instagram-all-ukraine/?p={i}'
            urls.append(url)

        for url in urls:
            request = session.get(url, headers=headers)
            soup = bs(request.content, 'html.parser')
            bloggers_table = soup.find('table', attrs={'id': 'bloggers-top-table'})
            bloggers_info = bloggers_table.find_all('td', attrs={'class': 'bloggers-top-name'})
            for blogger in bloggers_info:
                bloggername = {'bloggers-top-name': blogger.a.text}
                blogger_list.append(bloggername['bloggers-top-name'])
                print(blogger_list[-1:])

    else:
        print('ERROR')



bloggers_username_pars()