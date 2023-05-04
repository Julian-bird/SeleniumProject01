from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# 创建一个ChromeService对象，指定ChromeDriver路径
service = ChromeService(executable_path=ChromeDriverManager().install())
# 通过ChromeService对象创建WebDriver实例
driver = webdriver.Chrome(service=service)

# 打开一个网页并进行操作
driver.get("https://www.google.com")

# ...

# 关闭浏览器
# driver.quit()