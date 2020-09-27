
import time
from selenium import webdriver
import pyperclip
from selenium.common.exceptions import WebDriverException

start = time.time()

# Keep the driver in same path or mention the path
# Use Chromedriver for more precision
# Given chrome driver version in rep = 85.0.4183.121
browser = webdriver.Chrome(executable_path=r'chromedriver(2).exe')

# Website for scraping
browser.get('https://www.google.co.in/maps')

# Input Parameter
key = input('Enter the search parameters \n')

# Insert entered keys into search box
elem = browser.find_element_by_id('searchboxinput')
elem.click()
elem.send_keys(key)

# click search box to submit
Searchbutton = browser.find_element_by_id('searchbox-searchbutton')
Searchbutton.click()

# recursion
loop=True

time.sleep(1)

def main(*unused):
    time.sleep(2)
    bs = browser.find_element_by_xpath(r'/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div').text

    # normal split
    rbs = '\n'.join(bs.split('\n')[5:])

    # reverse split
    rrbs = rbs.rsplit("\n", 1)[0]
    print(rrbs)

    pyperclip.copy(rrbs)

    end = time.time()
    total = end - start
    print('Total time of execution:' + str(total))

main()

while loop:
    #time.sleep(2) uncomment this ONLY FOR SLOW INTERNET
    main()
    element = browser.find_element_by_xpath(r'//*[@id="n7lv7yjyC35__section-pagination-button-next"]')
    try:
        element.click()
    except WebDriverException:
        print("Button is not clickable")
        loop = False


