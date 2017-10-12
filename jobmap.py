#coding = utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
# 想法是爬取boss直聘上在北京python职位的薪资水平以及公司和地理位置
# 做一个简单的统计，结合echarts用地图的形式展现
# 本来是打算爬取拉钩的，但是拉钩需要登录，目前还不会这种
# 该网站每页显示10条数据，再次就按照默认排序爬取前150条数据，也就是10页，150之后的数据也没什么意义
boss_url = 'http://www.zhipin.com/c101010100/e_104-d_203-h_101010100/?query=python&ka=sel-degree-203'
# 1.访问网页
# 伪造浏览器headres
myheaders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
def down_loadpages(url):
	data = requests.get(url,headers = myheaders).content
	return data
def parse_html(times,html,cursor):
	times += 1
	soup = BeautifulSoup(html,'html.parser')
	job_div_soup = soup.find('div',attrs = {'class':'job-list'})
	job_ul_soup = job_div_soup.find('ul')
	job_li_list = job_ul_soup.find_all('li')
	for job_li_soup in job_li_list:
		job_name = job_li_soup.find('h3',attrs = {'class':'name'}).find('a').contents[0]
		job_salary = job_li_soup.find('h3',attrs = {'class':'name'}).find('a').find('span',attrs = {'class':'red'}).getText()
		# print(job_name+':'+job_salary)
		company_name = job_li_soup.find('div',attrs = {'class':'company-text'}).find('h3',attrs = {'class':'name'}).find('a').getText()
		# print(company_name)
		sql = 'insert into job_bj_py (description,salary,company) values("'+job_name+'","'+job_salary+'","'+company_name+'")'
		# print(sql)
		cursor.execute(sql)
	next_page = 'http://www.zhipin.com'+soup.find('div',attrs = {'class':'page'}).find('a',attrs = {'class':'next'})['href']
	# print(next_page)
	if times < 10:
		return times,next_page
	return times,None
# 创建表
def create_table():
	db = pymysql.connect('localhost','python','python','python3test',use_unicode = True,charset = 'utf8')
	cursor = db.cursor()
	cursor.execute('set names utf8')
	cursor.execute('set character set utf8')
	cursor.execute('set character_set_connection=utf8')
	cursor.execute('drop table if exists job_bj_py')
	sql = """create table job_bj_py(
		rank int primary key auto_increment,
		description varchar(100),
		salary varchar(100),
		company varchar(100)
		)auto_increment = 1"""
	cursor.execute(sql)
	# cursor.execute('select  * from book_top_250')
	# data = cursor.fetchone()
	# print(data)
	return db,cursor
def main():
	# 实现自动翻页，向后翻9次一共10页150条数据
	db,cursor = create_table()
	url = boss_url
	i = 0
	while url:
		html = down_loadpages(url)
		i,url = parse_html(i,html,cursor)
	db.commit()
	db.close()


if __name__ == '__main__':
	main()

