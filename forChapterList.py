import requests
from bs4 import BeautifulSoup


start_url = 'https://www.biqupai.com/87_87676/'
source = requests.get(start_url)
source.encoding = 'utf-8'
soup = BeautifulSoup(source.content, 'lxml')
url_list = []
list_content = soup.find_all('dd')
for each in list_content:
    temp_url = 'https://www.biqupai.com/' + each.a['href']
    url_list.append(temp_url)

print(url_list)


