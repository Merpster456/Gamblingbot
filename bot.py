import re
import getpass
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
        driver = self.driver
        driver.get("https://discord.com/login/")
        sleep(5)
        username_field = driver.find_element_by_xpath("//input[@name='email']")
        username_field.clear()
        username_field.send_keys(self.username)
        password_field = driver.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        sleep(5)

    def work(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(5)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
        message_box.send_keys(".work")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        deposit()
       
    def hourly(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(5)
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
        deposit()

    def daily(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(5)
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
        deposit() 

    def get_bal(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(5)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
        message_box.send_keys(".bal")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        numbers_elem = driver.find_elements_by_xpath(
                "//code[@class='scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9 hljs cs']")
        numbers = []
        for elem in numbers_elem:
            numbers.append(elem.text)
        dirty_bal = numbers[-1]
        temp = re.findall(r"\d+", dirty_bal) 
        bal = int("".join(temp))
        return bal

    def withdraw(self, amount):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(3)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
        message_box.send_keys(".with ", amount)
        message_box.send_keys(Keys.RETURN)
        
    def deposit(self):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(3)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
        message_box.send_keys(".dep all")
        message_box.send_keys(Keys.RETURN)

    def flip(self, amount):
        driver = self.driver
        driver.get("https://discord.com/channels/@me/809096023037050930")
        sleep(5)
        """
        bal = self.get_bal()
        bet = int(bal/256)
        self.withdraw(bet)
        passed = True
        """
        self.withdraw(amount)
        sleep(1)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message @Gamble Bot']")
        message_box.send_keys(".flip ", amount)
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        results = driver.find_elements_by_xpath(
                "//div[@class='embedWrapper-lXpS3L embedFull-2tM8-- embed-IeVjo6 markup-2BOw-j']")
        print(results)
        print(results[-1].text)
        
        """
        r = []
        for elem in results:
            r.append(elem)
        """ 

            

#email = input("Email: ")
#pwd = getpass.getpass()
email = "rfq456@gmail.com"
pwd = "Poppk456"

bot = Gambling_bot(email, pwd)
bot.initiate()
bot.flip(1)
i = 0
"""
while True:
    sleep(600)
    bot.work()
    i =+ 1
    if (i%6 == 0):
        bot.hourly()
    if (i%144 == 0):
        bot.daily()
        i = 0
"""
