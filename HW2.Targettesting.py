from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver_path = ChromeDriverManager().install()


service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.target.com/")
sleep(2)

driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys("tea")
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

sign_in = driver.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")
sign_in.click()
sleep(5)
button_sign_in = (driver.find_element(By.XPATH,"//button[contains(text(),'Sign in')]").click())
sleep(5)

text_sign_in_page =(driver.find_element(By.XPATH, "//span[contains(text(),'Sign into your Target account')]")).text


assert "Sign into your Target account" in text_sign_in_page, f'("Text {text_sign_in_page} not found")'
print("Testing was successful")

driver.quit()