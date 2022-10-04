from selenium import webdriver
from time import sleep, strftime
from random import randint


class Skyscanner:
    def __init__(self, city_from, city_to, date_start, date_to):
        self.city_from = city_from
        self.city_to = city_to
        self.date_start = date_start[2:].replace('-', '')
        self.date_to = date_to[2:].replace('-', '')

    def start_skyscanner(self):
        chromedriver_path = '/Users/kenton/Documents/Programming/Personal Projects/Web Scrapers/Kayak Flight Web Scraper/chromedriver'
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        sleep(2)

        print(self.date_start)

        skyscanner = 'https://www.skyscanner.ca/transport/flights/' + self.city_from + '/' + self.city_to + '/' + self.date_start + '/' + self.date_to + '/?adults=2&adultsv2=2&cabinclass=economy&children=0&childrenv2=&destinationentityid=27544072&inboundaltsenabled=false&infants=0&originentityid=27537336&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1'

        driver.get(skyscanner)
        sleep(randint(8, 10))
