from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TwitterBot:
    def __init__(self, username, password):
        # Path to your WebDriver
        self.CHROME_DRIVER_PATH = 'C:/Users/ADMIN/Desktop/chromedriver-win32/chromedriver.exe'
        service = Service(self.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

        self.userName = username  # Twitter username
        self.password = password    # Twitter password
        self.tweet_urls = [
            'https://x.com/intent/like?tweet_id=1817610094768480605',
'https://x.com/intent/retweet?tweet_id=1817610094768480605'
        ]
        self.follow_urls = [
            'https://x.com/BRKTgg',
'https://x.com/BRKTLabs',
'https://x.com/InfiniseasDev',
'https://x.com/chazzgordon99',
'https://x.com/wasjakehere',
'https://x.com/buildnexio'
        ]

    def twitterLogin(self):
        self.driver.get('https://x.com/login')
        time.sleep(2)
        
        # Log in to Twitter
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(self.userName)
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)
        
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(1)  # Wait for the login process to complete

    def likeTweet(self, tweet_url):
        self.driver.get(tweet_url)
        time.sleep(2)
        
        try:
            # Like the tweet
            like_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-testid="like"]'))
            )
            like_button.click()
            print(f"Liked the tweet: {tweet_url}")
            time.sleep(2)  # Wait to mimic human behavior

        except Exception as e:
            print(f"Error liking the tweet {tweet_url}: {e}")

    def retweet(self, tweet_url):
        self.driver.get(tweet_url)
        time.sleep(2)

        try:
            # Click the retweet button
            retweet_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-testid="retweet"]'))
            )
            retweet_button.click()
            time.sleep(2)  # Wait for the retweet dialog to open

            # Confirm retweet
            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-testid="retweetConfirm"]'))
            )
            confirm_button.click()
            print(f"Retweeted the tweet: {tweet_url}")

        except Exception as e:
            print(f"Error retweeting the tweet {tweet_url}: {e}")

    def followAccount(self, follow_url):
        self.driver.get(follow_url)
        time.sleep(2)
        
        try:
            # Click the follow button using the provided XPath
            follow_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div/div[1]/button/div/span/span'))
            )
            follow_button.click()
            print(f"Followed the account: {follow_url}")

        except Exception as e:
            print(f"Error following the account {follow_url}: {e}")

    def run(self):
        self.twitterLogin()
        for tweet_url in self.tweet_urls:
            self.likeTweet(tweet_url)
            time.sleep(4)  # Wait 1 second between actions
            self.retweet(tweet_url)
            time.sleep(3)  # Wait again after retweeting
        
        for follow_url in self.follow_urls:
            self.followAccount(follow_url)
            time.sleep(2)  # Wait after following

        self.driver.quit()

if __name__ == "__main__":
    accounts = [
        {'username': 'itachiu03996712', 'password': 'Mohit868@'},
        {'username': '', 'password': ''}
    ]

    for account in accounts:
        print(f"Logging in as: {account['username']}")
        bot = TwitterBot(account['username'], account['password'])
        bot.run()
