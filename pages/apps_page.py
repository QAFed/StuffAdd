from pages.base_page import BasePage
from selenium.webdriver.common.by import By
# import requests

class AppsPage(BasePage):
    xp_bkmark_apps = By.XPATH, '//div[text()="Приложения"]'
    xp_buton_add_apps = By.XPATH, '//span[text()="Сертификат"]/../../../..//span[text()="Добавить..."]'
    xp_button_sertif = By.XPATH, '//span[text()="Сертификат"]'
    xp_button_delete = By.XPATH, '//span[text()="Сертификат"]/../../../..//span[text()="Удалить"]/../..'
    xp_adding_string = By.XPATH, '//div[text()="PostLink"]'
    xp_add_name_input = By.XPATH, '//div[contains(@style,"top: 30px;")]/input'
    xp_add_descript_input = By.XPATH, '//div[contains(@style,"top: 60px;")]/input'
    xp_add_pass_sert_input = By.XPATH, '//div[contains(@style,"top: 90px;")]/input'
    xp_add_button_save = By.XPATH, '//div[contains(@style,"top: 30px;")]/input/../../../..//span[text()="Сохранить"]'
    xp_button_sert_create = By.XPATH, '//span[text()="Создать"]'
    xp_button_sert_export = By.XPATH, '//span[text()="Экспорт"]'
    check_box_matrix = (
        "Просмотр справочников",
        "Редактирование справочников",
        "Просмотр списка приложений",
        "Редактирование списка приложений",
        "Просмотр атрибутов приложений",
        "Редактирование атрибутов приложений",
        "Просмотр списка администраторов",
        "Редактирование списка администраторов",
        "Просмотр дерева подразделений",
        "Редактирование дерева подразделений",
        "Просмотр списка пользователей",
        "Создание сертификата",
        "Экспорт сертификата"
        )
    xp_button_save_matrix = By.XPATH, '//span[text()="Сохранить"]/..'
    xp_dwnld_cert = By.XPATH, '//iframe[contains(@src, "certificate.pfx")]'
    xp_dwnld_pswd = By.XPATH, '//iframe[contains(@src, "password.pass")]'
    xp_delete_ok = By.XPATH, '//span[text()="Ok"]'


    def activate_check_boxes(self):
        for option in self.check_box_matrix:
            xp_check_box = By.XPATH, f'//div[text()="{option}"]/../..//div[contains(@style, "align: right")]//input'
            self.ac_click_element(xp_check_box)

    def enable_add_string(self):
        button_delete = self.get_element_after_visible(self.xp_button_delete, 2)
        if 'disabled' in button_delete.get_attribute('class'):
            self.ac_click_element(self.xp_adding_string)

    def check_n_delete_past_string(self):
        while True:
            try:
                self.ac_click_element(self.xp_adding_string)
                self.ac_click_element(self.xp_button_delete)
                self.ac_click_element(self.xp_delete_ok)
            except:
                break


    def click_bm_apps(self):
        self.ac_click_element(self.xp_bkmark_apps)

    def click_button_add_apps(self):
        self.ac_click_element(self.xp_buton_add_apps)

    def input_name(self):
        self.fill_field(self.xp_add_name_input, "PostLink")

    def input_descr(self):
        self.fill_field(self.xp_add_descript_input, "PostLink")

    def input_pass(self):
        self.fill_field(self.xp_add_pass_sert_input, '1234567890123456')

    def click_add_button_save(self):
        self.ac_click_element(self.xp_add_button_save)

    def click_button_save_matrix(self):
        self.ac_click_element(self.xp_button_save_matrix)

    def click_button_sertif(self):
        self.ac_click_element(self.xp_button_sertif)

    def click_button_create_sertif(self):
        self.ac_click_element(self.xp_button_sert_create)

    def click_button_sertif_export(self):
        self.ac_click_element(self.xp_button_sert_export)



    # def get_file(self, el_xpath, path_name):
    #     element = self.wait_element_in_dom(el_xpath, 10)
    #     file_url = element.get_attribute('src')
    #     response = requests.get(file_url)
    #     if response.status_code == 200:
    #         with open(f"{path_name}", 'wb') as file:
    #             file.write(response.content)
    #     else:
    #         print(response.status_code, file_url)
    #
    # def get_file_certificate(self):
    #     self.get_file(self.xp_dwnld_cert, 'certificate.pfx')
    #
    # def get_file_pass_pass(self):
    #     self.get_file(self.xp_dwnld_pswd, 'password.pass')




