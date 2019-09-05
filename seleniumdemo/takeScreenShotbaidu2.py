from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get('https://www.baidu.com/')

assert '百度' in browser.title

elem = browser.find_element_by_id('kw')

elem.send_keys('seleniumhq')
elem.send_keys(Keys.RETURN)

time.sleep(5)
browser.save_screenshot('C:/test/screenshotsbaidu2a.png')
browser.quit()
