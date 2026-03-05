# Automated Cookie Clicker


"""===Install Module==="""
# pip3 install selenium

"""===Load Modules==="""
"""time delay"""
import time

"""setup webdriver"""
from selenium import webdriver

"""manual setup of chrome driver"""
# from selenium.webdriver.chrome.service import Service

"""search and interact with element in html"""
from selenium.webdriver.common.by import By

"""wait for the presence of an element to exist"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""===Initialize WebDriver==="""
"""manual setup of chrome driver"""
# service = Service(executable_path="chromedriver.exe")

"""initialize web driver with manual chrome driver setup"""
# driver = webdriver.Chrome(service=service)
"""initialize web driver without it"""
driver = webdriver.Chrome()

"""grab cookie clicker website"""
driver.get("https://g8hh.github.io/cookieclicker/")

"""create variable for cookie id"""
cookie_id = "bigCookie"
cookies_id = "cookies"

"""create variable for product price"""
product_price_prefix = "productPrice"
product_prefix = "product"


"""===Find and Select English==="""
"""wait for language element in HTML that contains the text "English" to load"""
"""chatgpt to find targeted HTML element and create syntax for XPATH"""

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

"""find element by XPATH to click language"""
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

"""wait for cookie element by id to load"""
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))


""""===Find and Select Cookie==="""
"""wait for cookeie id to load"""
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

"""find element by id to click cookie"""
cookie = driver.find_element(By.ID, cookie_id)
# cookie.click()
# time.sleep(10)

"""===clicking loop==="""
while True:
    cookie.click()
    """select 1st segment of text of cookies_id"""
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    """remove commons in numbers"""
    cookies_count = int(cookies_count.replace(",", ""))
    # print(cookies_count)

    """===Find and Select Upgrades (Product Price)==="""
    """this program goes up to four products"""
    for i in range(4):
        """for context the HTML the id="productPrice0" hence productPrice + str(i)"""
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        """error handle if product price is int and not str"""
        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        """click the upgrade when cookie count is or greater than product price"""
        if cookies_count >= product_price:
            """find the product price button then click"""
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
