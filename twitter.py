from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

S = []

u = ''
p  = ''
t  = ""

driver = webdriver.Chrome()
wait = WebDriverWait(driver,36)
driver.maximize_window()
driver.get("https://twitter.com/login")
time.sleep(3)


e = wait.until(EC.visibility_of_element_located((By.NAME,'text'))).send_keys(u)
time.sleep(2)
n_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'))).click()
# time.sleep(2)
# user = wait.until(EC.visibility_of_element_located((By.NAME,'text'))).send_keys(t)
# time.sleep(2)
# n1_button = driver.find_element(By.CLASS_NAME,'css-1dbjc4n r-sdzlij r-1phboty r-rs99b7')
# n1_button.click()
time.sleep(2)
P = wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(p)
login = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'))).click() 
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
    S.append(url)

except:
  print("No profile found")

rowHeader = ['Twitter_Data']
df = pd.DataFrame(S)    
df.to_csv('Twitter_review.csv',index=False, header=rowHeader) 
