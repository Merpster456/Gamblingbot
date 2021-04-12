import re
import getpass
from time import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Gambling_bot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def initiate(self):
        try:
            driver = self.driver
            driver.get("https://discord.com/login/")
            sleep(3)
            username_field = driver.find_element_by_xpath("//input[@name='email']")
            username_field.clear()
            username_field.send_keys(self.username)
            password_field = driver.find_element_by_xpath("//input[@name='password']")
            password_field.clear()
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)
            sleep(2)
            driver.get("https://discord.com/channels/@me/809096023037050930")
            sleep(5)
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def work(self):
        try:
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".work")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            self.deposit()
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()
       
    def hourly(self):
        try:
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".hourly")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            message_box.send_keys(".roulette all")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            message_box.send_keys("green")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            self.deposit()
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def daily(self):
        try:
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".daily")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            message_box.send_keys(".crash all")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            message_box.send_keys("bust")
            message_box.send_keys(Keys.RETURN)
            sleep(1)
            self.deposit() 
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def get_bal(self):
        try: 
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".bal")
            message_box.send_keys(Keys.RETURN)
            sleep(3)
            numbers_elem = driver.find_elements_by_xpath(
                    "//code[@class='scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9 hljs cs']")
            numbers = []
            for elem in numbers_elem:
                numbers.append(elem.text)
            dirty_bal = numbers[-1]
            temp = re.findall(r"\d+", dirty_bal) 
            bal = int("".join(temp))
            return bal
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def withdraw(self, amount):
        try:
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".with ", amount)
            message_box.send_keys(Keys.RETURN)
            sleep(2)
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()
    def deposit(self):
        try:
            driver = self.driver
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".dep all")
            message_box.send_keys(Keys.RETURN)
            sleep(2)
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def flip(self, amount):
        try:
            driver = self.driver
            self.withdraw(amount)
            message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
            message_box.send_keys(".flip ", amount)
            message_box.send_keys(Keys.RETURN)
            sleep(2)
            results = driver.find_elements_by_xpath(
                    "//div[@class='embedWrapper-lXpS3L embedFull-2tM8-- embed-IeVjo6 markup-2BOw-j']")
            
            dirty_sty = results[-1].get_attribute("style")
            temp = re.findall(r"\d+", dirty_sty) 
            sty = int("".join(temp))
            if sty == 25534:
                self.deposit()
                return True
            else:
                return False
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

    def flip_loop(self):
        try:
            bal = self.get_bal()
            bet = int(bal/1024)
            trigger = True
            while True:
                if self.flip(bet):
                    break
                else:
                    bet = bet*2
        except KeyboardInterrupt:
            self.deposit()
            self.close_browser()

email = input("Email: ")
pwd = getpass.getpass()

bot = Gambling_bot(email, pwd)
bot.initiate()
bot.flip_loop()
t0 = round(time(), 3)
i = 0
try:
    while True:
        bot.flip_loop()
        t1 = round(time(), 3)
        print("--- %s seconds ---" % (t1 - t0))
        print(".")
        if (t1 - t0 >= 600):
            bot.work()
            i += 1
            t0 = round(time(), 3)
        if (i != 0 and i%6 == 0):
            bot.hourly()
        if (i != 0 and i%144 == 0):
            bot.daily()
            i = 0
except KeyboardInterrupt:
    bot.deposit()
    bot.close_browser()
