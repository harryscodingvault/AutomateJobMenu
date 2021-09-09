

from IndeedBot import IndeedBot

import random

rand_time = random.randint(0, 4)


import undetected_chromedriver.v2 as uc
driver = uc.Chrome()
with driver:
    driver.get('https://nowsecure.nl')


indeed_bot = IndeedBot(job='java', location='ny', driver=driver, rand_time=rand_time)
indeed_bot.run_bot()