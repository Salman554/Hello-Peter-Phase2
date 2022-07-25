
from wave import Wave_write
import webbrowser
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd



list1 =[]
list2= []
list3 =[]
list4 =[]
def search_term():
   
    if(var2.get()==1):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver,36)
        driver.maximize_window() 
        driver.get("https://www.hellopeter.com/"+Term.get())
        time.sleep(5)
        title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'business-name'))).text 
        print(title)
        time.sleep(2)
        for i in range(1,12):
            u_n = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/section[2]/div/div[1]/div/div[2]/div[4]/div[4]/div['+str(i)+']/div/div/div[1]/h1/a'))).text
            list3.append(u_n)  
        
        print(list3)

        
        ru = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'blurb')))
        for i in ru:
            list4.append(i.text)

        print(list4)

        dict = {'Name': list3, 'Reviews': list4}
        df = df = pd.DataFrame.from_dict(dict, orient='index')
        df = df.transpose()
        df.to_csv('HelloPeter.csv') 

        url = driver.current_url
        wait.until(EC.url_to_be(url))
        driver.get("https://www.google.com/maps/@31.4884267,74.3704765,15z")
        time.sleep(2)
        query = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]'))).send_keys(title)
        time.sleep(2)
        query = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]'))).send_keys(Keys.ENTER)
        time.sleep(5)
        ratings = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span[1]'))).click()
        time.sleep(5)
        names = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'d4r55')))

        for i in names:
            list1.append(i.text)

        print(list1)
           
        for i in range(1,31,3):
            reviews = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/div['+str(i)+']/div/div[3]/div[4]/div[2]/span[2]'))).text
            list2.append(reviews)
       

        print(list2)   

        dict = {'Name': list1, 'Reviews': list2}
        df = df = pd.DataFrame.from_dict(dict, orient='index')
        df = df.transpose()
        df.to_csv('Google_reviews.csv')    

    
 
root=Tk()
root.resizable(False, False)
root.title("Hellopeter web scraper search")  
 
 
Term = StringVar(root, value="")
Term_entry=ttk.Entry(root,textvariable=Term,width=50)
Term_entry.grid(row=0, column=1,padx=10, pady=15,sticky=W+E)
Term_entry.focus()
 
submit_button = ttk.Button(root,text="Submit",command=search_term)
submit_button.grid(row=0, column=2,padx=9, sticky=W+E)
 
check=Frame(root).grid(row=0,column=0,columnspan=3)
 
var2 = IntVar(root,value=0)
Checkbutton(check, text="Hellopeter", variable=var2).grid(row=0,column=4)
 
Term_entry.bind("<Return>", (lambda event: search_term()))
 
root.mainloop()