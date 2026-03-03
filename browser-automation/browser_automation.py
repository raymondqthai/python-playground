# Browser Automation


"""===Install Module==="""
# pip3 install selenium


"""===Selenium and Chrome Driver Setup==="""
"""load module"""
import time
from typing import ByteString

"""setup chrome driver to initialize the web driver"""
"""selenium on Mac automatically finds and download chromedriver you need"""
from selenium import webdriver

"""search for element in html and interact however we please"""
from selenium.webdriver.common.by import By

"""sending [enter], [up arrow], [down arrow], [shift], [capital] strokes"""
from selenium.webdriver.common.keys import Keys

"""wait for the presence of an element to exist"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
I think you can use this code if you're on Windows
But because I'm on a Mac and don't want to compromise security settings
The code below is commented out
"""
# from selenium.webdriver.chrome.service import Service


"""download chrome driver"""
# https://sites.google.com/chromium.org/driver/home
# Latest ChromeDriver Binaries > the Chrome for Testing availability dashboard
# > Stable > chromedriver/mac-arm64/https://storage.googleapis.com/chrome-for-testing-public/146.0.7680.31/mac-arm64/chromedriver-mac-arm64.zip/200
"""
download zip folder in the same location as this python file
extract the folder that contains chromedriver
move chromedriver out to the same location as this python file
"""

"""web driver is an automation tool to control chrome"""
"""
I think you can use this code if you're on Windows
But because I'm on a Mac and don't want to compromise security settings
The code below is commented out
"""
"""This would've setup chrome driver"""
"""
service = Service(
    executable_path="/Users/rthai/MEGA/Self_Study/Python-Projects/project_3/chromedriver"
)
driver = webdriver.Chrome(service=service)
"""
"""initialize the web driver"""
driver = webdriver.Chrome()


"""grab a website"""
driver.get("https://www.startpage.com")


"""wait for the presence of an element to exist until selected class name is generated"""
"""if element doesn't appear after 5 seconds, crash"""
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "search-form-input"))
)


"""===Locating & Interacting with Elements==="""
"""find the search field, select, type, and enter"""
"""search field"""
# go to https://www.startpage.com
# [right click] the search field
# select [inspect]
# Elements tab > Highlighted box > class="search-form-input"
"""select"""
input_element = driver.find_element(By.CLASS_NAME, "search-form-input")
"""clear the search field"""
input_element.clear()
"""type"""
input_element.send_keys("linkedin raymond-thai-9552bb87" + Keys.ENTER)


"""===Clicking Links & Navigating Pages==="""
"""wait for the presence of an element to exist until selected partial link text is generated"""
"""make sure text is exact because it is case sensitive"""
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Raymond Thai"))
)


"""click on a link that redirects user to another page"""
"""make sure text is exact because it is case sensitive"""
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Raymond Thai")
link.click()


"""time delay for visibility purposes then quit"""
time.sleep(10)
driver.quit()
