from selenium import webdriver
import logging
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from retrying import retry
from selenium.webdriver import ActionChains

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class github():
    def __init__(self):
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.browser.maximize_window()   # 最大化窗口
        # self.browser.implicitly_wait(1)  # 隐式等待1秒
        self.domain = 'https://github.com/'
        self.action_chains = ActionChains(self.browser)

    def login(self, username, password):
        self.browser.get(self.domain)
        self.browser.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

class taobao():
    def __init__(self):
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.browser.maximize_window()   # 最大化窗口
        # self.browser.implicitly_wait(1)  # 隐式等待1秒
        self.domain = 'http://www.taobao.com'
        self.action_chains = ActionChains(self.browser)

    def login(self, username, password):
        while True:
            self.browser.get(self.domain)
            time.sleep(1)

            self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
            self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
            self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
            time.sleep(1)

            try:
                slider = self.browser.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
                if slider.is_displayed():
                    self.action_chains.drag_and_drop_by_offset(slider, 258, 0).perform()   # 拖拽滑块
                    time.sleep(0.5)
                    self.action_chains.release().perform()  # 释放拖拽
            except (NoSuchElementException, WebDriverException):
                logger.info('未出现登录验证码')

            self.browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()  # 点击登录



            break



if __name__ == '__main__':
    username = '123456'
    password = '!@#$%^'
    # tb = taobao()
    # tb.login(username, password)
    git = github()
    git.login(username, password)