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
            'https://x.com/dogs_airdrop/status/1820142241631101300',
            'https://x.com/dogs_airdrop/status/1820284335653843140',
            'https://x.com/dogs_airdrop/status/1820259294455185495'
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
        time.sleep(5)  # Wait for the login process to complete

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

    def run(self):
        self.twitterLogin()
        for tweet_url in self.tweet_urls:
            self.likeTweet(tweet_url)
            time.sleep(1)  # Wait 10 seconds between actions
            self.retweet(tweet_url)
            time.sleep(10)  # Wait again after retweeting

        self.driver.quit()

if __name__ == "__main__":
    accounts = [
        {'username': 'itachiiuchiha', 'password': 'achiiuc'},
        {'username': 'mightguy', 'password': 'achiiuc'}
    ]

    for account in accounts:
        print(f"Logging in as: {account['username']}")
        bot = TwitterBot(account['username'], account['password'])
        bot.run()
