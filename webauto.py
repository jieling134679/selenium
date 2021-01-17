from selenium import webdriver
wd = webdriver.Chrome(r'D:\Python\selenim\chromedriver.exe')
# wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
wd.get('https://www.damai.cn/')

element = wd.find_element_by_class_name('input-search')
element.send_keys('周杰伦')
search_btn = wd.find_element_by_class_name('btn-search')
search_btn.click()

div = wd.find_element_by_class_name('search-box-flex')
span = div.find_elements_by_tag_name('span')
for i in span:
    print(i.text)

