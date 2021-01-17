from selenium import webdriver
wd = webdriver.Chrome(r'D:\Python\selenim\chromedriver.exe')
wd.get('http://www.baidu.com')


element = wd.find_element_by_id('kw')
element.send_keys('成都师范学院')

element = wd.find_element_by_id('su')
element.click()



