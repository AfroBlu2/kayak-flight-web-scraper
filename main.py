from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

chromedriver_path = '/Users/kenton/Documents/Programming/Personal Projects/Web Scrapers/Kayak Flight Web Scraper/chromedriver'

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)



# MIGHT NEED TO TARGET THIS IN ANOTHER WAY IF CLASS ENDS UP BEING DYNAMIC GOOGLE SEARCH XPATHS


def close_popup():
    try:
        xp_popup_close = '.bBPb-closeIcon'
        driver.find_element_by_css_selector(xp_popup_close).click()
    except Exception as e:
        print('No popup displayed')
        return

def page_scrape():
    """
    Here we scrape

    """


def start_kayak(city_from, city_to, date_start, date_end):
    """
    This is the main function that starts the bot

        city_from, city_to : string (airport IAIA codes, three letters)
        date_start, date_end : string (date format YYYY-MM-DD)
    """
    kayak = ('https://www.ca.kayak.com/flights/' + city_from + '-' + city_to + '/' + date_start + '-flexible-3days/' + date_end + '-flexible-3days?sort=bestflight_a')
    driver.get(kayak)
    sleep(randint(8,10))

    close_popup()
    sleep(randint(60,95))

    print('Starting first scrape...')




start_kayak('YQB', 'ATH', '2023-03-12', '2023-03-18')






# FIND CHEAPEST FLIGHT
sleep(2)
cheapest_flight = ''



