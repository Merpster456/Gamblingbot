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
        sleep(10)
        driver.get("https://discord.com/channels/731310911792480256/808115279221358602/")
        
email = input("Email: ")
pwd = getpass.getpass()

bot = Gambling_bot(email, pwd)
bot.initiate()
