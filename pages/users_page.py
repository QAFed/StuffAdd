import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class UsersPage(BasePage):
    xp_bkmark_users = By.XPATH, '//div[text()="Пользователи"]'
    xp_button_add_users = By.XPATH, '//div[contains(@style, "-6px")]//span[text()="Добавить..."]'
    xp_input_family_user = By.XPATH, '//div[contains(@style,"top: 42px")]/input'
    xp_input_name_user = By.XPATH, '//div[contains(@style,"top: 72px")]/input'
    xp_input_second_name_user = By.XPATH, '//div[contains(@style,"top: 102px")]/input'
    xp_input_birth_day_user = By.XPATH, '//div[contains(@style,"top: 138px")]//input'
    xp_button_save = By.XPATH, '//span[text()="Сохранить"]'

    xp_button_add_contact = By.XPATH, '//div[contains(@style, "-7px")]//span[text()="Добавить..."]'
    xp_select_type = By.XPATH, '//select'
    xp_select_mob_tel = By.XPATH, '//select/option[text(),"Мобильный телефон"]'
    xp_input_tel = By.XPATH, '//select/../../../div/input'

    xp_button_add_job = By.XPATH, '//div[not(contains(@style, "-"))]/div/div/div/div/div/div/span/span[text()="Добавить..."]'

    def click_bm_users(self):
        self.ac_click_element(self.xp_bkmark_users)
    def add_user(self, user_list):
        self.ac_click_element(self.xp_button_add_users)
        self.fill_field(self.xp_input_family_user, user_list[0])
        self.fill_field(self.xp_input_name_user, user_list[1])
        self.fill_field(self.xp_input_second_name_user, user_list[2])
        self.fill_field(self.xp_input_birth_day_user, user_list[3])
        self.ac_click_element(self.xp_button_save)

    def add_tell(self, user_list):
        self.ac_click_element((By.XPATH, f'//tr/td/div[text()="{user_list[0]} {user_list[1]} {user_list[2]}"]'))
        self.ac_click_element(self.xp_button_add_contact)
        self.ac_click_element(self.xp_select_type)
        time.sleep(1)
        self.ac_click_element(self.xp_select_mob_tel)
        self.fill_field(self.xp_input_tel, user_list[4])
        self.ac_click_element(self.xp_button_save)

    def add_job(self, user_list):
        self.ac_click_element((By.XPATH, f'//tr/td/div[text()="{user_list[0]} {user_list[1]} {user_list[2]}"]'))
        self.ac_click_element(self.xp_button_add_job)
        self.ac_click_element((By.XPATH, f'//span[text()="{user_list[5]}"]'))
        self.ac_click_element(self.xp_select_type)
        self.ac_click_element((By.XPATH, f'//select/option[text(),"[{user_list[6]}"]'))
        self.ac_click_element(self.xp_button_save)



