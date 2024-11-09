from conf import ConfData
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    URL = ConfData.URL+'/#!LoginView'
    xp_login = By.XPATH, '//input[@type="text"]'
    xp_pass = By.XPATH, '//input[@type="password"]'
    xp_button_login = By.XPATH, '//div[@role="button"]'

    def input_login(self):
        self.fill_field(self.xp_login)

    def input_pass(self):
        self.fill_field(self.xp_pass)

    def click_butt_login(self):
        self.ac_click_element(self.xp_button_login)


