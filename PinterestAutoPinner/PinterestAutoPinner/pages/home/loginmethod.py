from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl
import logging
import time

class Login(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)
        self.actions = ActionChains(driver)

    # Locators
    _login_option = "//a[contains(text(), 'Already a member? Log in')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[contains(text(), 'Log in')]//parent::button"
    _fb_button = "//*[@id='u_0_1']/div"
    _fb_frame = "//iframe[@title='fb:login_button Facebook Social Plugin']"

    def clickAlreadyAMemeber(self):
        self.elementClick(self._login_option, locatorType="xpath")

    def enterEmailField(self, email="ben_g98@hotmail.com"):
        self.sendKeys(email, self._email_field)

    def enterPasswordField(self, password="yruadreaded12"):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def switchFBFrame(self):
        fbFrame = self.sl.getElement(self._fb_frame, locatorType="xpath")
        self.driver.switch_to.frame(fbFrame)

    def clickFBButton(self):
        self.elementClick(self._fb_button, locatorType="xpath")

    def loginMethod(self):
        self.clickAlreadyAMemeber()
        time.sleep(2)
        self.enterEmailField()
        time.sleep(2)
        self.enterPasswordField()
        time.sleep(2)
        self.clickLoginButton()
        time.sleep(1)

