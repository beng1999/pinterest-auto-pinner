from selenium import webdriver
from pages.home.loginmethod import Login
from pages.home.autofollower import AutoFollower
import time

class PinterestPoster():
    baseURL = "https://www.pinterest.ca/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)

    lg = Login(driver)
    follow = AutoFollower(driver)

    def testPost(self):
        self.lg.loginMethod()
        self.follow.FollowingAutomation()
        self.driver.quit()

ff = PinterestPoster()
ff.testPost()