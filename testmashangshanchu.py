import requests 
from bs4 import BeautifulSoup
import time
myheaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
url = 'http://www.xicidaili.com/nn'
def down_loadpages(url):
	data = requests.get(url,headers = myheaders).content
	return data
def parse_html(html):
	soup = BeautifulSoup(html,'html.parser')
	ip_tr_list = soup.find_all('tr',attrs = {'class':'odd'})
	for ip_tr in ip_tr_list:
		ip = ip_tr.find_all('td')[1].getText()
		print(ip)
def main():
	data = down_loadpages(url)
	parse_html(data)
if __name__  == '__main__':
	main()

