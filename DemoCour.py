# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
#driver.get("https://www.bdeb.qc.ca/")
driver.get("https://demo.nopcommerce.com/login?returnurl=%2F")
driver.maximize_window()
#time.sleep(5)
print(driver.title)
