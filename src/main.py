import os
import shutil
import time
from conf import ConfData
from mody_file.mody_file import ModyFile
from pages.login_page import LoginPage
from pages.apps_page import AppsPage
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from mody_file.mody_file import ModyFile


if __name__ == "__main__":
    download_dir = ConfData.firefox_sert_temp_folder
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
    os.makedirs(download_dir)

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", download_dir)
    profile.set_preference("browser.download.folderList", 2)
    options = Options()
    options.profile = profile
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.input_login()
    login_page.input_pass()
    login_page.click_butt_login()
    apps_page = AppsPage(driver)
    apps_page.click_bm_apps()
    apps_page.check_n_delete_past_string()
    apps_page.click_button_add_apps()
    apps_page.input_name()
    apps_page.input_descr()
    apps_page.input_pass()
    apps_page.click_add_button_save()
    apps_page.enable_add_string()
    apps_page.activate_check_boxes()
    apps_page.click_button_save_matrix()
    time.sleep(1)
    apps_page.enable_add_string()
    time.sleep(1)
    apps_page.click_button_sertif()
    time.sleep(2)
    apps_page.click_button_create_sertif()
    time.sleep(2)
    apps_page.click_button_sertif_export()
    time.sleep(10)
    driver.quit()



