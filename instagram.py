from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

Q = []
U = ''
P = ''

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 36)
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input'))).send_keys(U)
pa =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#loginForm > div > div:nth-child(2) > div > label > input'))).send_keys(P)
login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3) > button'))).click()
time.sleep(2)


url = driver.current_url
wait.until(EC.url_to_be(url))
driver.get("https://www.google.com/")
keywords = input("ENTER THE KEYWORDS: ")
query =  wait.until(EC.visibility_of_element_located((By.NAME,'q'))).send_keys(keywords)
time.sleep(2)
query =  wait.until(EC.visibility_of_element_located((By.NAME,'q'))).send_keys(Keys.ENTER)
time.sleep(2)
top_result = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'h3'))).click()
time.sleep(2)
try:
    url = driver.current_url
    print(url)
    Q.append(url)

except:
  print("No profile found")

rowHeader = ['Instagram_Data']
df = pd.DataFrame(Q)    
df.to_csv('Instagram_review.csv',index=False, header=rowHeader) 
