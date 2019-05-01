from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import timedelta,date

DATA_DIR = 'data2'

def daterange(start_date,end_date):
    for n in range(int((end_date-start_date).days)):
        yield start_date + timedelta(n)

def main():
    start_date = date(2018,1,3)
    end_date = date(2018,10,6)
    driver = webdriver.Chrome('../chromedriver/chromedriver')
    for single_date in daterange(start_date,end_date):
        scrape_day(single_date.month,single_date.day,single_date.year,driver)

def scrape_day(month,day,year,driver):
    url = 'https://www.wunderground.com/history/daily/us/il/des-plaines/KORD/date/{}-{}-{}'.format(year,month,day)
    driver.get(url)
    done = False
    while not done:
        tables = WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))
        for table in tables:
            newTable = pd.read_html(table.get_attribute('outerHTML'))
            if newTable:
                newTable = newTable[0].fillna('')
                newTable.to_csv('{}/{}-{}-{}.csv'.format(DATA_DIR,month,day,year))
                done = True

main()
