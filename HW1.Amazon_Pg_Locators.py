from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver_path = ChromeDriverManager().install()


service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.com/")

#Amazon Logo locators
driver.find_element(By.XPATH, "//a[@aria-label='www.amazon.com']")
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")

#Email locators
driver.find_element(By.ID,  "ap_email")
driver.find_element(By.XPATH, "//input[@name='email']")


#Locators for Continue Button
driver.find_element(By.ID,"continue" )
driver.find_element(By.XPATH, "//input[@class ='a-button-input']")

#Locator for Conditions of use
driver.find_element((By.XPATH, "//a[contains(text(),'Conditions of Use')]"))

#Locator for privacy notice
driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Notice')]")

#Locators for Need help?
driver.find_element(By.XPATH, "//a[@role='button']").click()

#Locators for Forgot your password
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.XPATH, "//a[contains(text(),'Forgot your password?')]")

#Locators for Other issues
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.XPATH,"//a[contains(text(), 'Other issues')]" )

#Locators for Buying for work?
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-micro']")
driver.find_element(By.XPATH, "//span[contains(text(),'Buying for work?')]" )

#Locators for Shop on Amazon Business
driver.find_element(By.ID, 'ab-signin-ingress-link')
driver.find_element(By.XPATH, "//span[contains(text(),'Shop on Amazon Business')]")

#Locators for Create Your Amazon Account
driver.find_element(By.ID, 'createAccountSubmit')
driver.find_element(By.XPATH, ("//a[@class='a-button-text']"))
driver.find_element(By.XPATH, "//a[contains(text(), 'Create your Amazon account')]")



