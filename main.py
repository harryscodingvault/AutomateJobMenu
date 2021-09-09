from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from IndeedBot import IndeedBot

import random

rand_time = random.randint(0,4)


import undetected_chromedriver.v2 as uc
driver = uc.Chrome()
with driver:
    driver.get('https://nowsecure.nl')


indeed_bot = IndeedBot(job='java', location='ny', driver=driver, rand_time=rand_time)
indeed_bot.run_bot()