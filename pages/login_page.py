from conf import ConfData
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = ConfData.URL_oss + '/#!LoginView'
    xp_login = By.XPATH, '//input[@type="text"]'
    xp_pass = By.XPATH, '//input[@type="password"]'
    xp_button_login = By.XPATH, '//div[@role="button"]'

    def open_page(self):
        self.driver_open_page(self.URL)

    def input_login(self):
        self.fill_field(self.xp_login, ConfData.login_oss)

    def input_pass(self):
        self.fill_field(self.xp_pass, ConfData.password_oss)

    def click_butt_login(self):
        self.ac_click_element(self.xp_button_login)
