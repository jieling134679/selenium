from selenium import webdriver
wd = webdriver.Chrome(r'D:\Python\selenim\chromedriver.exe')
wd.implicitly_wait(10)

wd.get('https://www.baidu.com/')
wd.find_element_by_id('kw').send_keys('成都房价\n')

# import time
# time.sleep(1)

element = wd.find_element_by_id('1')
print(element.text)
