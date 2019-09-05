from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get('http://www.yahoo.com')

assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')

elem.send_keys('seleniumhq')
elem.send_keys(Keys.RETURN)

time.sleep(2)
browser.save_screenshot('C:/test/screenshotsyahoo.png')
browser.quit()
