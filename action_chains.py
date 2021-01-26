from selenium import webdriver

wd = webdriver.Chrome(r'D:\Python\selenim\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('https://www.bilibili.com/')

login = wd.find_element_by_css_selector('#app .name img')
login.click()

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    print(wd.current_url)
    if 'passport' in wd.current_url:
        break

wd.find_element_by_css_selector('#login-username').send_keys('274712917@qq.com')
wd.find_element_by_css_selector('#login-passwd').send_keys('cs1122330099')
wd.find_element_by_css_selector('[class="btn btn-login"]').click()