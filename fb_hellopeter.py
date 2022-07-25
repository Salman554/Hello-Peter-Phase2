from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

D = []

u = ''
p = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,36)
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(3)

E = driver.find_element(By.ID,'email').send_keys(u)
pas = driver.find_element(By.ID,'pass').send_keys(p)
time.sleep(2)
login = wait.until(EC.visibility_of_element_located((By.NAME,'login'))).click()
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
url = driver.current_url
print(url)
D.append(url)

rowHeader = ["FB_data"]
df = pd.DataFrame(D)    
df.to_csv('FB_review.csv',index=False, header=rowHeader) 
