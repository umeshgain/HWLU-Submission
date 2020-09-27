import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import pyperclip

# Follow steps to start a debug environment
# IMPORTANT: GO TO CMD
# IMPORTANT: CD INTO CHROME.EXE FOLDER AND TYPE
# chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\Umesh\MyPythonScripts\Mdatag\Browser"


start = time.time()

# recursion
loop=True
# Keep the driver in same path or mention the path
# Use Chromedriver for more precision
# Given chrome driver version in rep = 85.0.4183.121
chrome_browser = r'chromedriver(2).exe'
chrome_options = Options()

# Edit the port to next available port if 9222 is used
# DONOT EDIT LOOPBACK ADDRESS "127.0.0.1"
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(chrome_browser, options=chrome_options)


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
    #time.sleep(2) ONLY FOR SLOW INTERNET uncomment this
    main()
    element = browser.find_element_by_xpath(r'//*[@id="n7lv7yjyC35__section-pagination-button-next"]')
    try:
        element.click()
    except WebDriverException:
        print("Button is not clickable")
        loop = False

