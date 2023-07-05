from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://office.chameleoninfotech.com/member/dashboard"

driver = webdriver.Chrome() 
driver.get(url)

username = driver.find_element(By.ID,'email')
password = driver.find_element(By.ID, "password")
username.clear()
password.clear()
submit =  driver.find_element(By.CLASS_NAME,"btn")
submit.click()

username.send_keys("omsavani25@gmail.com")
username.send_keys(Keys.RETURN)
password.send_keys("w1FwNB28")
password.send_keys(Keys.RETURN)

try:
    clock_in= driver.find_element(By.ID,"clock-in")
    clock_in.click()
except:
    clock_out = driver.find_element(By.ID,"clock-out")
    clock_out.click()

time.sleep(5)
driver.close()


