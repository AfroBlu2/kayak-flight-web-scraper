from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

chromedriver_path = '/Users/kenton/Documents/Programming/Personal Projects/Web Scrapers/Kayak Flight Web Scraper/chromedriver'

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

kayak = ''

