from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def set_value_into_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                             "Web element was not available within the specific time out. "
                                             "Locator: '" + str(locator) + "'")
        self.clear_field(locator)
        self.wait_for_presence_of_element(locator).send_keys(text)

    def clear_field(self, locator):
        self.wait_for_presence_of_element(locator)

    def click_on_element(self, locator, locator_initialization=False, time_out=10):
        if locator_initialization:
            locator = (By.XPATH, locator)
        else:
            WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                       "Web element was not available within the specific time out. "
                                                       "Locator: '" + str(locator) + "'")
            self.wait_for_element_to_be_clickable(locator).click()

    def wait_for_element_to_be_clickable(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator),
                                                          "Web element was not clickable within the specific time "
                                                          "out. Locator: '" + str(locator) + "'")

    def wait_for_presence_of_element(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                          "Web element was not present within the specific time "
                                                          "out. "
                                                          "Locator: '" + str(locator) + "'")

    def wait_for_presence_of_elements(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.presence_of_all_elements_located(locator),
                                                          "Web element was not present within the specific time "
                                                          "out. "
                                                          "Locator: '" + str(locator) + "'")

    def scroll_down_to_specific_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def select_dropdown_value(self, dropdown_label, dropdown_item="", select_by_value=False, value="1", index=1):
        locator = "(//label[contains(text(), '" + dropdown_label + "')]/..//select)[" + str(index) + "]"
        self.dropdown_selection(locator, dropdown_item, select_by_value, value)

    def dropdown_selection(self, locator, dropdown_item="", select_by_value=False, value="1"):
        self.wait_for_presence_of_element((By.XPATH, locator))
        self.wait_for_element_to_be_clickable((By.XPATH, locator))
        if select_by_value:
            Select(self.driver.find_element(By.XPATH, locator)).select_by_value(value)
        else:
            Select(self.driver.find_element(By.XPATH, locator)).select_by_visible_text(dropdown_item)
