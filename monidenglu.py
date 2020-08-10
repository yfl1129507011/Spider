from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://www.baidu.com')
    # //*[@id="kw"]
    elem = browser.find_element_by_xpath('//*[@id="kw"]')
    elem.send_keys("python")
    elem.send_keys(Keys.RETURN)