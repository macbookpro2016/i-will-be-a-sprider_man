import requests 
from bs4 import BeautifulSoup
import time
myheaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
def down_loadpages(url):
	data = requests.get(url,headers = myheaders).content
	return data
def parse_html(html):
	soup = BeautifulSoup(html,'html.parser')
	job_div_soup = soup.find('div',attrs = {'class':'job-list'})
	job_ul_soup = job_div_soup.find('ul')
	job_li_soup = job_ul_soup.find('li')
	detail_url = 'http://www.zhipin.com'+job_li_soup.find('div',attrs = {'class':'info-primary'}).find('a')['href']
	print(detail_url)
	detail_html = down_loadpages(detail_url)
	detail_soup = BeautifulSoup(detail_html,'html.parser')
	website_p = detail_soup.find('div',attrs = {'class':'info-company'}).find_all('p')
	print(len(website_p))
def sleep():
	i = 1
	while i<=10:
		i+=1
		print(1)
		time.sleep(0.5)
		
def main():
	# url = 'http://www.zhipin.com/c101010100/e_104-d_203-h_101010100/?query=python&ka=sel-degree-203'
	# data = down_loadpages(url)
	# parse_html(data)
	sleep()

if __name__ == '__main__':
	main()