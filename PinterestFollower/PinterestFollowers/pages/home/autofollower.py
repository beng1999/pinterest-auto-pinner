from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import time

class AutoFollower(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)

    #Locators
    _search_bar = "//input[@data-test-id='search-box-input']"
    _follow_button = "//button[@aria-label='Follow']"

    def inputSearch(self, search="Save the bees"):
        element = self.sl.getElement(self._search_bar, locatorType="xpath")
        element.send_keys(search)
        element.send_keys(Keys.ENTER)

    def followUser(self):
        for i in range(1, 50):
            _images = "//*[@id='__PWS_ROOT__']/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[" + str(i) + "]/div/div/div/div/div/div/div[1]/a"

            self.elementClick(_images, locatorType="xpath")
            time.sleep(2)

            isUserFollowed = self.elementPresenceCheck(self._follow_button, byType="xpath")

            if isUserFollowed:
                self.elementClick(self._follow_button, locatorType="xpath")
                self.inputSearch()
            else:
                self.inputSearch()


    def FollowingAutomation(self):
        self.inputSearch()
        time.sleep(1)
        self.followUser()