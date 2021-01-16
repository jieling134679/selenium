from selenium import webdriver
wd = webdriver.Chrome(r'D:\Python\selenim\chromedriver.exe')
wd.get('http://www.baidu.com')

print('你好')

element = wd.find_element_by_id('kw')
element.send_keys('中文')

element = wd.find_element_by_id('su')
element.click()
