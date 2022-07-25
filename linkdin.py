from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import pandas as pd

L = []


driver = webdriver.Chrome()
wait = WebDriverWait(driver,36)
driver.maximize_window()
driver.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in")
time.sleep(3)

with open('config.json','r') as f:
  config = json.load(f)

email = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[1]/input'))).send_keys(config['user']['name'])
pas = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[2]/input'))).send_keys(config['user']['password'])
time.sleep(3)
button = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[3]/button'))).click()
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
  user_url = wait.until(EC.visibility_of_element_located((By.ID,'top-card-text-details-contact-info'))).get_attribute("href")
  print(user_url)
  L.append(user_url)
  time.sleep(10) 
except:
  print("No profile found")

rowHeader = ['Linkdin_Data']
df = pd.DataFrame(L)    
df.to_csv('Linkdin_review.csv',index=False, header=rowHeader) 
