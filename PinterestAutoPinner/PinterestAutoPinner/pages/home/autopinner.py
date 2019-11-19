from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
from selenium.webdriver.common.keys import Keys
import time

class AutoPinner(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)

    #Locators
    _search_bar = "//input[@data-test-id='search-box-input']"
    _save_button = "//div[@data-test-id='SaveButton']"
    _board_selection = "//div[@data-test-id='board-selection']"
    _already_posted_img = "//div[@data-test-id='already-pinned']"
    _close_image_button = "//button[@aria-label='Close']"
    counter = 0

    def inputSearch(self, search="Save the bees"):
        element = self.sl.getElement(self._search_bar, locatorType="xpath")
        element.send_keys(search)
        element.send_keys(Keys.ENTER)

    def clickImages(self):
        for i in range(1, 6):
            _images = "//*[@id='__PWS_ROOT__']/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[" + str(i) + "]/div/div/div/div/div/div/div[1]/a"
            self.elementClick(_images, locatorType="xpath")
            time.sleep(2)
            self.clickSaveButton()
            time.sleep(1)

            alreadyHaveImage = self.elementPresenceCheck(self._already_posted_img, byType="xpath")
            print(alreadyHaveImage)

            if alreadyHaveImage is not True:
                self.boardSelection()
                time.sleep(2)
                self.inputSearch()
                self.counter += 1
                print(self.counter)
            else:
                self.elementClick(self._close_image_button, locatorType="xpath")
                self.inputSearch()


    def clickSaveButton(self):
        isSaveThere = self.elementPresenceCheck(self._save_button, byType="xpath")
        print(isSaveThere)
        self.elementClick(self._save_button, locatorType="xpath")

    def boardSelection(self):
        self.elementClick(self._board_selection, locatorType="xpath")

    def PinningAutomation(self):
        self.inputSearch()
        time.sleep(2)
        self.clickImages()
        time.sleep(2)
