from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from InternetSpeedTwitterBot import bot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "email"
TWITTER_PASSWORD = "password"
USERNAME = "username"


bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, USERNAME)

