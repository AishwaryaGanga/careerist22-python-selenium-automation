from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#get the path to the ChromDriver executable
driver_path = ChromeDriverManager().install()

#create a new Chrome Browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

#open the url
driver.get("https://www.google.com/")
sleep(4)

#driver.find_element(By.XPATH, "//button[@aria-label='Stay signed out']").click()

search = driver.find_element(By.NAME,"q")
search.clear()
search.send_keys("Car")
sleep(5)
