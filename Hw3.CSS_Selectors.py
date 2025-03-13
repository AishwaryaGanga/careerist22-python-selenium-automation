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


#Amazon logo locators
driver.find_element(By.CSS_SELECTOR,'.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, "[role = 'presentation']")

#Create account locator
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#Your name locators
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR,"[name='customerName']")
driver.find_element(By.CSS_SELECTOR, "input[autocomplete='name']")
driver.find_element(By.CSS_SELECTOR, ".a-input-text.auth-required-field.a-span12.auth-autofocus")
driver.find_element(By.CSS_SELECTOR,".auth-autofocus")
driver.find_element(By.CSS_SELECTOR, "[aria-describedby*= 'ap_customer_name']")
driver.find_element(By.CSS_SELECTOR, "input.auth-autofocus[placeholder*='last name']")

#email locators
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "input[name='email']")
driver.find_element(By.CSS_SELECTOR, "[data-validation-id = 'email']")
driver.find_element(By.CSS_SELECTOR, ".a-input-text.a-span12.auth-required-field.auth-require-claim-validation")
driver.find_element(By.CSS_SELECTOR, '.auth-require-claim-validation')
driver.find_element(By.CSS_SELECTOR, "[class *= 'auth-required-field auth-require-claim-validatio']")
driver.find_element(By.CSS_SELECTOR, "input[aria-describedby *= 'ap_email_context_message'][autocomplete = 'email']")

#password locators
driver.find_element(By.CSS_SELECTOR, "[name='password']")
driver.find_element(By.CSS_SELECTOR, ".auth-require-fields-match.auth-require-password-validation")
driver.find_element(By.CSS_SELECTOR, "[class *= 'auth-require-password-validation'][name='password']")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "input[aria-describedby *= 'ap_password_context']")
driver.find_element(By.CSS_SELECTOR, ".auth-require-password-validation")

#Re-enter password locators
driver.find_element(By.CSS_SELECTOR,"#ap_password_check" )
driver.find_element(By.CSS_SELECTOR, "input[type='password'][name ='passwordCheck']")
driver.find_element(By.CSS_SELECTOR, "[autocomplete='new-password'][name ='passwordCheck']")
driver.find_element(By.CSS_SELECTOR, "[class *= 'a-input-text a-span12 auth-required-field'][id ='ap_password_check']")


#Continue Locators
driver.find_element(By.CSS_SELECTOR, "[aria-describedby ='legalTextRow']" )
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, ".a-button-input")
driver.find_element(By.CSS_SELECTOR, ".a-button-input[type = 'submit']")
driver.find_element(By.CSS_SELECTOR, "[aria-labelledby *= 'continue']")
driver.find_element(By.CSS_SELECTOR, "[aria-describedby = 'legalTextRow'][type='submit']")

#Conditions of use locator
driver.find_element(By.CSS_SELECTOR, "a[href *= 'ref=ap_register_notification_condition_of_use?']")

#Privacy Notice Locator
driver.find_element(By.CSS_SELECTOR, "[href *= 'ref=ap_register_notification_privacy_notice']")

#Create a free business account locators
driver.find_element(By.CSS_SELECTOR, "#ab-enhanced-registration-link")
driver.find_element(By.CSS_SELECTOR, ".a-link-normal[href *= 'https://www.amazon.com/business']")

#Sign in link locator
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
driver.find_element(By.CSS_SELECTOR, "[href *= '/ap/signin?openid.']")

