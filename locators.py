from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    "C:\\Users\DawidJagoda\Desktop\python + Zyia\chromedriver.exe",
    chrome_options=chrome_options,
)
driver.get("http://automationpractice.com/index.php")
time.sleep(3)  # waiting to all page has been loaded


CONTACT_US = driver.find_element_by_id("contact-link")
SIGN_IN = driver.find_element_by_class_name("login")
SEARCH_BOX = driver.find_element_by_id("search_query_top")
MAGNIFIER = driver.find_element_by_name("submit_search")
CART = driver.find_element_by_css_selector(
    ".shopping_cart [title='View my shopping cart']"
)
WOMEN = driver.find_element_by_css_selector("a[title='Women']")
DRESSES = driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[2]/a")
TSHIRTS = driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[3]/a")
POPULAR = driver.find_element_by_css_selector("#home-page-tabs a[class='homefeatured']")
BEST_SELLERS = driver.find_element_by_css_selector(
    "#home-page-tabs a[class='blockbestsellers']"
)
SHORT_SLEEVE = driver.find_element_by_css_selector(
    "a[class='product_img_link'] [title='Faded Short Sleeve T-shirts']"
)
# BLOUSE = driver.find_element_by_class_name(
#     "a[class='product_img_link'] [title='Blouse']"
# )

# Rest clothes and images I can find only by Xpath. I don't know how to find it in another way

FOLLOW_ON_FB = driver.find_element_by_css_selector("#facebook_block .facebook-fanbox")
COME_VISIT_US = driver.find_element_by_css_selector("#icon-truck")
SELENIUM_FRAMEWORK = driver.find_element_by_link_text("Selenium Framework")
NEWSLETTER = driver.find_element_by_css_selector(
    "input[class='inputNew form-control grey newsletter-input']"
)
SUBMIIT_BTN = driver.find_element_by_css_selector("button[name='submitNewsletter']")
FB = driver.find_element_by_class_name("facebook")
TWITTER = driver.find_element_by_class_name("twitter")
YOUTUBE = driver.find_element_by_class_name("youtube")
GOOGLE = driver.find_elements_by_class_name("google-plus")
FOLLOW_US = driver.find_elements_by_link_text("Follow us")
CAT_WOMEN = driver.find_element_by_css_selector("a[title='Women']")
SPECIALS = driver.find_element_by_css_selector(".toggle-footer a[title='Specials']")
NEW_PRODUCTS = driver.find_element_by_css_selector(
    ".toggle-footer a[title='New products']"
)
BST_SELLERS = driver.find_element_by_css_selector(
    ".toggle-footer a[title='Best sellers']"
)
OUR_STORES = driver.find_element_by_css_selector(".toggle-footer a[title='Our stores']")
CNTCT_US = driver.find_element_by_css_selector(".toggle-footer a[title='Contact us']")
TERMS = driver.find_element_by_css_selector(
    ".toggle-footer a[title='Terms and conditions of use']"
)
ABOUT_US = driver.find_element_by_css_selector(".toggle-footer a[title='About us']")
SITEMAP = driver.find_element_by_css_selector(".toggle-footer a[title='Sitemap']")
MY_ACCOUNT = driver.find_element_by_css_selector(
    "a[title='Manage my customer account']"
)
MY_ORDERS = driver.find_element_by_css_selector(".bullet a[title='My orders']")
MY_CREDIT_SLIPS = driver.find_element_by_css_selector(
    ".bullet a[title='My credit slips']"
)
MY_ADRESSES = driver.find_element_by_css_selector(".bullet a[title='My addresses']")
MY_PERSONAL_INFO = driver.find_element_by_css_selector(
    ".bullet a[title='Manage my personal information']"
)
EMAIL = driver.find_element_by_link_text("support@seleniumframework.com")
EMAIL.click()