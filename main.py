from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

rand_time = random.randint(0,3)


import undetected_chromedriver.v2 as uc
driver = uc.Chrome()
#with driver:
    #driver.get('https://nowsecure.nl')


driver.get('https://www.indeed.com/')


# ------------------------------ Search Bar ------------------------------------------
search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="text-input-what"]'))
        )
# Job Input
#time.sleep(rand_time)
input_job_search = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
input_job_search.clear()
input_job_search.send_keys('C++')


# Job Location
#time.sleep(rand_time)
input_job_location = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
input_job_location.send_keys(Keys.CONTROL + 'a')
input_job_location.send_keys(Keys.BACKSPACE)
input_job_location.send_keys('LA')

# Search Button
input_job_button = driver.find_element(By.XPATH, '//*[@id="whatWhereFormId"]/div[3]/button')
input_job_button.click()

# ------------------------------ My Soup ------------------------------------------

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Company': [''], 'Location': [''], 'Salary': ['']})

while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    posting = soup.find_all('a', class_='result')

    for post in posting:
        job_link = post.get('href')
        full_link = 'https://www.indeed.com' + job_link
        title = post.find('h2', class_='jobTitle').text.strip()
        company = post.find('span', class_='companyName').text.strip()
        try:
            location = post.find('div', class_='companyLocation').text.strip()
        except:
            location = 'NOT.F'
        try:
            salary = post.find('span', class_='salary-snippet').text.strip()
        except:
            salary = 'NOT.F'
        df = df.append({'Link': full_link, 'Title': title, 'Company': company, 'Location': location, 'Salary': salary}, ignore_index=True)

    try:
        next_button_link = soup.find('a', attrs ={'aria-label': 'Next'}).get('href')
        driver.get('https://www.indeed.com' + next_button_link)

    except:
        break


print(df)
