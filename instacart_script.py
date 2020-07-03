import selenium
import time 
from selenium import webdriver
from pygame import mixer

driver = webdriver.Firefox(executable_path ='usr/local/bin {nameofyourlocalbinpath}')
driver.get('https://www.instacart.com')
driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/header/div/div[2]/div/button').click()
driver.find_element_by_xpath('//*[@id="nextgen-authenticate.all.log_in_email"]').send_keys("email")
driver.find_element_by_xpath('//*[@id="nextgen-authenticalte.all.log_in_password"]').send_keys("password")

driver.get('https//www.instacart.com/store/checkout_v3')

while True:
    time.sleep(30)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/h1')
    except:
        print('Exception occurred!')
        mixer.init()
        mixer.music.load('alarm.mp3')
        mixer.music.play()
