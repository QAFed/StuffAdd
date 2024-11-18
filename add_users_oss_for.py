import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from pages.divdsion_page import DivisPage
from pages.users_page import UsersPage

if __name__ == "__main__":
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.input_login()
    login_page.input_pass()
    login_page.click_butt_login()

    divis_page = DivisPage(driver)
    divis_page.click_bm_divis()
    divis_page.add_division('919', 'division', 'desk_division')
    divis_page.add_job('job_name', 'job_desc', '110')

    users_page = UsersPage(driver)
    users_page.click_bm_users()
    users_plan = (
        ('Voskresenskii', 'Ivan', 'Nikolaevich', '12-12-1980', '+79019019191', 'division', 'job_name'),
        ('Starshikova', 'Margarita', 'Tikhonovna', '10-10-1985', '+79029029292', 'division', 'job_name'),
    )
    time.sleep(1)
    for user_list in users_plan:
        users_page.add_user(user_list)
        time.sleep(1)

    for user_list in users_plan:
        users_page.add_tell(user_list)
        users_page.add_job(user_list)


    time.sleep(10)




