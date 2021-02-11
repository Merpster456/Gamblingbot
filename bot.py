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
        driver.get("https://discord.com/channels/731310911792480256/808115279221358602/")
        sleep(5)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message #casino']")
        message_box.send_keys(".work")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys(".dep all")
        message_box.send_keys(Keys.RETURN)

    def hourly(self):
        driver = self.driver
        driver.get("https://discord.com/channels/731310911792480256/808115279221358602/")
        sleep(5)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message #casino']")
        message_box.send_keys(".hourly")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys(".roulette all")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys("green")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys(".dep all")
        message_box.send_keys(Keys.RETURN)

    def daily(self):
        driver = self.driver
        driver.get("https://discord.com/channels/731310911792480256/808115279221358602/")
        sleep(5)
        message_box = driver.find_element_by_xpath("//div[@aria-label='Message #casino']")
        message_box.send_keys(".daily")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys(".crash all")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys("bust")
        message_box.send_keys(Keys.RETURN)
        sleep(1)
        message_box.send_keys(".dep all")
        message_box.send_keys(Keys.RETURN)

email = input("Email: ")
pwd = getpass.getpass()

bot = Gambling_bot(email, pwd)
bot.initiate()
i = 0

while True:
    sleep(600)
    bot.work()
    i =+ 1
    if (i%6 == 0):
        bot.hourly()
    if (i%144 == 0):
        bot.daily()
        i = 0

