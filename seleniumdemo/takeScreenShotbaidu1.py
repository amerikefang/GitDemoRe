from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.fullscreen_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('seleniumhq'+Keys.RETURN)


time.sleep(2)
driver.save_screenshot('C:/test/takescreeshotbaidu1a.png')

driver.close()
