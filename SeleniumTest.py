import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Settings for opening headless browser
op = webdriver.ChromeOptions()
op.add_argument('--headless')

# Setting browser
browser = webdriver.Chrome(
	executable_path='./chromedriver_win32/chromedriver.exe', 
	options = op
)

# Running test
# Opening the website
browser.get("https://deepsight.azurewebsites.net/")

# Filling the contact form
browser.find_element(By.NAME, "name").send_keys("Parth Kodnani", Keys.RETURN)
#browser.find_element(By.XPATH,'/html/body/main/section[5]/div/div[2]/div[2]/form/div[2]/input').send_keys("parthkodnani92@gmail.com", Keys.RETURN)
#browser.find_element(By.NAME, "message").send_keys("404 Error", Keys.RETURN)
# browser.find_element(By.NAME, "subject").send_keys("404 Error", Keys.RETURN)

print("Form Filled")

# Submit form
#browser.find_element_by_xpath('/html/body/main/section[5]/div/div[2]/div[2]/form/div[6]/button').click()

print("Form Submitted!")

if browser.current_url == "https://deepsight.azurewebsites.net/forms/contact.php":
	print("Successful Test")
	time.sleep(2)
	browser.quit()
else :
	browser.quit()
	exit(1)



