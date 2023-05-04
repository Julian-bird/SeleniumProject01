import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.maximize_window()
#driver.get("https://www.bdeb.qc.ca/")
driver.get("https://demo.nopcommerce.com/login?returnurl=%2F")
driver.find_element(By.ID,"Email").send_keys("test@test.com")
driver.find_element(By.ID,"Password").send_keys("test")
driver.find_element(By.CLASS_NAME,"login-button").click()
driver.find_element(By.CLASS_NAME,"validation-summary-errors").is_displayed()
texterror=driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
time.sleep(5)
print(texterror)
#assert "Login was unsuccessful" in texterror
assert texterror == """Login was unsuccessful. Please correct the errors and try again.
No customer account found"""
driver.close()