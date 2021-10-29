from selenium import webdriver
import requests
import time

class Login_school:
    def __init__(self):
        self.url = 'http://1.1.1.3/ac_portal/20191008142058/pc.html?template=20191008142058&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=http://1.1.1.3/homepage/index.html&policy=userself-reg&policy_type=account&controller_type=&mac=fc-d7-33-77-1a-af'
        self.username = "****"
        self.password = "****"

    # 判断当前是否可以连网
    def is_connect_web(self):
        try:
            status = requests.get("https://www.baidu.com")
            if (status.status_code == requests.codes.ok):
                return True
            else:
                return False
        except:
            return False
        print('error')


    def login(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        browser.implicitly_wait(10)
        user = browser.find_element_by_id('password_name')
        user.send_keys(self.username)
        pwd = browser.find_element_by_id('password_pwd')
        pwd.send_keys(self.password)
        browser.find_element_by_id('password_submitBtn').click()
        # 登录成功之后就可以关闭浏览器了
        browser.close()
while True:
    if Login_school().is_connect_web():
        print("已经联网")
        break
    else:
        Login_school().login()
        print("成功联网")
        break
