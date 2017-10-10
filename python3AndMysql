#coding = 'utf-8'
import pymysql
import requests
from bs4 import BeautifulSoup

# 2.爬取豆瓣图书  https://book.douban.com/top250
book_url = 'https://book.douban.com/top250'
myheaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
#下载网页内容方法
def download_page(url):
	print('下载网页')
	data = requests.get(url,headers = myheaders).content
	return data  
#解析网页内容，获取目的内容
def parse_html(url,html,cursor):
	print('解析网页')
	source_url = url
	print('source_url:' + source_url)
	soup = BeautifulSoup(html,"html.parser")
	book_div_soup = soup.find('div',attrs = {'class':'indent'})
	for book_table in book_div_soup.find_all('table'):
		detail = book_table.find('tr',attrs = {'class':'item'})
		book_name = detail.find('div',attrs = {'class':'pl2'}).find('a').get('title')
		sql = 'insert into book_top_250 (book_name,source) values ("'+ str(book_name) + '","' + str(source_url) + '")'
		print(sql)
		bookcursor = cursor
		bookcursor.execute(sql)
	next_page = soup.find('span',attrs = {'class':'next'}).find('a')
	if next_page:
		return next_page['href']
	print('存储完了，老铁！！！')
	return None

def main():
	# 1.连接数据库并创建相应表
	db = pymysql.connect('localhost','python','python','python3test',use_unicode=True, charset="utf8")
	# db.set_character_set('utf8')
	cursor = db.cursor()
	# db.set_character_set('utf-8')
	cursor.execute('SET NAMES utf8') 
	cursor.execute('SET CHARACTER SET utf8')
	cursor.execute('SET character_set_connection=utf8')
	url =  book_url
	while url:
		data = download_page(url)
		url = parse_html(url,data,cursor)
	db.commit()
	db.close()
if __name__ == '__main__':
	main()
