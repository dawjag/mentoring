from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from automation.pages.main_page.locators import main_page_main_locators

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    "C:\\Users\DawidJagoda\Desktop\python + Zyia\chromedriver.exe",
    chrome_options=chrome_options,
)
driver.get("http://automationpractice.com/index.php")
time.sleep(3)  # waiting to all page has been loaded
