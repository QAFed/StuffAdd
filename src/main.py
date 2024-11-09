import time

from pages.login_page import LoginPage
from pages.apps_page import AppsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == "__main__":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.input_login()
    login_page.input_pass()
    login_page.click_butt_login()
    apps_page = AppsPage(driver)
    apps_page.click_bm_apps()
    apps_page.click_button_add_apps()
    apps_page.input_name()
    apps_page.input_descr()
    apps_page.input_pass()
    apps_page.click_add_button_save()
    apps_page.enable_add_string()
    apps_page.activate_check_boxes()
    apps_page.click_button_save_matrix()
    apps_page.enable_add_string()
    apps_page.click_button_sertif()
    apps_page.click_button_create_sertif()
    apps_page.click_button_sertif_export()
    time.sleep(10)

