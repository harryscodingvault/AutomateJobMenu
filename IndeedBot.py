from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


class IndeedBot:
    def __init__(self, job, location, driver, rand_time):
        self.job = job
        self.location = location
        self.driver = driver
        self.rand_time = rand_time

    def run_bot(self):
        self.driver.get('https://www.indeed.com/')

        # ------------------------------ Search Bar ------------------------------------------
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="text-input-what"]'))
        )
        # Job Input
        time.sleep(self.rand_time)
        input_job_search = self.driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
        input_job_search.clear()
        input_job_search.send_keys(self.job)

        # Job Location
        time.sleep(self.rand_time)
        input_job_location = self.driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
        input_job_location.send_keys(Keys.CONTROL + 'a')
        input_job_location.send_keys(Keys.BACKSPACE)
        input_job_location.send_keys(self.location)

        # Search Button
        input_job_button = self.driver.find_element(By.XPATH, '//*[@id="whatWhereFormId"]/div[3]/button')
        input_job_button.click()

        # ------------------------------ DATA BOX ------------------------------------------

        # Dataframe
        df = pd.DataFrame({'Link': [''], 'Title': [''], 'Company': [''], 'Location': [''], 'Salary': ['']})

        while True:
            time.sleep(self.rand_time)
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
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
                df = df.append(
                    {'Link': full_link, 'Title': title, 'Company': company, 'Location': location, 'Salary': salary},
                    ignore_index=True)

            try:
                time.sleep(self.rand_time)
                next_button_link = soup.find('a', attrs={'aria-label': 'Next'}).get('href')
                self.driver.get('https://www.indeed.com' + next_button_link)

            except:
                break

        print(df)

