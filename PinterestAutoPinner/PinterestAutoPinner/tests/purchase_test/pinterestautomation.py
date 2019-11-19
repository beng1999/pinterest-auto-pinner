from selenium import webdriver
from pages.home.loginmethod import Login
from pages.home.autopinner import AutoPinner
import time

class PinterestPoster():
    baseURL = "https://www.pinterest.ca/"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)

    lg = Login(driver)
    pin = AutoPinner(driver)

    def testPost(self):
        self.lg.loginMethod()
        time.sleep(2)
        self.pin.PinningAutomation()
        time.sleep(2)
        self.driver.quit()

ff = PinterestPoster()
ff.testPost()