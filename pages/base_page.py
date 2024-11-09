from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def driver_open_page(self, url):
        self.driver.get(url)

    def get_element_after_visible(self, el_xpath, time):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(el_xpath))

    def ac_click_element(self, el_xpath):
        the_element = self.get_element_after_visible(el_xpath, 10)
        actions = ActionChains(self.driver)
        actions.click(the_element).perform()
        return the_element

    def fill_field(self, el_xpath, load_data):
        the_element = self.ac_click_element(el_xpath)
        the_element.send_keys(load_data)

    def wait_element_in_dom(self, el_xpath, time):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(el_xpath))
