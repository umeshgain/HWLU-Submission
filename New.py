import time
from selenium import webdriver
# IMPORTANT
from selenium.webdriver.chrome.options import Options
import pyperclip

chrome_browser = r'chromedriver(2).exe'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(chrome_browser, options=chrome_options)

#bs= browser.find_element_by_xpath(r'/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div').text
bs= browser.find_element_by_xpath(r'//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[3]/div/div/div[2]/div[1]/div/div').text
print(bs)

pyperclip.copy(bs)
