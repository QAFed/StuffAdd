from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DivisPage(BasePage):
    xp_bkmark_didvs = By.XPATH, '//div[text()="Подразделения"]'
    xp_button_add_division = By.XPATH, '//div[@style="height: 50%;"]/div/div/div/span/span[text()="Добавить..."]'
    xp_button_add_job = By.XPATH, '//div[not(@style="height: 50%;")]/div/div/div/span/span[text()="Добавить..."]'

    xp_input_code_divis = By.XPATH, '//div[contains(@style, "top: 6px;")]/input'
    xp_input_nane_divis = By.XPATH, '//div[contains(@style, "top: 36px;")]/input'
    xp_input_descr_divis = By.XPATH, '//div[contains(@style, "top: 66px;")]/input'
    xp_button_save_div = By.XPATH, '//span[text()="Сохранить"]'

    xp_input_nane_job = By.XPATH, '//div[contains(@style, "top: 0px;")]/input'
    xp_input_descr_job = By.XPATH, '//div[contains(@style, "top: 30px;")]/input'
    xp_input_count_job = By.XPATH, '//div[contains(@style, "top: 60px;")]/input'
    xp_button_save_job = By.XPATH, '//span[text()="Сохранить"]'

    def click_bm_divis(self):
        self.ac_click_element(self.xp_bkmark_didvs)

    def add_division(self, code, name, desc):
        self.ac_click_element(self.xp_button_add_division)
        self.fill_field(self.xp_input_code_divis, code)
        self.fill_field(self.xp_input_nane_divis, name)
        self.fill_field(self.xp_input_descr_divis, desc)
        self.ac_click_element(self.xp_button_save_div)

    def add_job(self, name, desc, count):
        self.ac_click_element(self.xp_button_add_job)
        self.fill_field(self.xp_input_nane_job, name)
        self.fill_field(self.xp_input_descr_job, desc)
        self.fill_field(self.xp_input_count_job, count)
        self.ac_click_element(self.xp_button_save_job)




