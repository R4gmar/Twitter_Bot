from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(45)
        self.up += float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.down += float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self, email, password, username):
        self.driver.get(url="https://twitter.com/?lang=ru")
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
        sleep(2)
        input_email = self.driver.find_element(By.CSS_SELECTOR, value="div input")
        input_email.send_keys(email)
        input_email.send_keys(Keys.ENTER)
        sleep(2)
        input_name = self.driver.find_element(By.CSS_SELECTOR, value='div input')
        input_name.send_keys(username)
        input_name.send_keys(Keys.ENTER)
        sleep(2)
        input_pass = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pass.send_keys(password)
        input_pass.send_keys(Keys.ENTER)
        sleep(4)

        tweet = f"Hey Internet Provider, whi is my internet speed {self.down}down/{self.up}"
        f"when I pay for 150down/10up?"
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post.click()

        sleep(2)
        send_tweet = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        send_tweet.send_keys(tweet)
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
        sleep(4)
        self.driver.quit()






bot = InternetSpeedTwitterBot()

