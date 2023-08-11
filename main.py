import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servic = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servic, options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

time.sleep(2)

username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
username.clear()
username.send_keys("performance_glitch_user")

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.clear()
password.send_keys("secret_sauce")
password.send_keys(Keys.ENTER)
