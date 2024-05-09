import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

driver_path = r"D:\sql\chrome-win64.zip"

# Set ChromeDriver path in the environment variable
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

# Create a ChromeOptions object
chrome_options = Options()

# Add experimental option
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)
#set ChromeDriver path in the environment variable
time.sleep(2)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()
username=driver.find_element(By. ID, "user-name")
username.click()
time.sleep(1)
username.send_keys("standard_user")
password=driver.find_element(By. ID,"password")
password.click()
time.sleep(1)
password.send_keys("secret_sauce")
login=driver.find_element(By. ID,"login-button")
login.click()
print(driver.title)
print(driver.current_url)
url = "https://www.saucedemo.com/"
#Send a GET request to the webpage
response = requests.get("https://www.saucedemo.com/")

#Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, "html.parser")

#Extract text from HTML
webpage_text = soup.get_text()

#Save the extracted text to a text file
file_name="webpage_page_task_11.txt"
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
   file.write(webpage_text)





