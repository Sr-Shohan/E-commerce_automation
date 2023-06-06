from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator.checkout_page_locator import CheckoutPage
from pages.base_page import BasePage


class Checkout(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def compare_data_with_html(self, xpath_locators, expected_data):
        actual_data = []

        for xpath_locator in xpath_locators:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(xpath_locator))
            data = element.text
            actual_data.append(data)

        assert actual_data == expected_data, "Data mismatch"

    def perform_checkout(self):
        xpath_locators = [
            CheckoutPage.full_name_locator,
            CheckoutPage.company_name_locator,
            CheckoutPage.zip_road_locator,
            CheckoutPage.address2_locator,
            CheckoutPage.city_state_locator,
            CheckoutPage.country_locator,
            CheckoutPage.mobile_number_locator,
        ]

        expected_data = [
            "Mr. Antanas Kujerus",
            "Pierogi",
            "1134 Columbia Road",
            "Most",
            "Dallas Texas 98607",
            "United States",
            "111222333"
        ]

        self.compare_data_with_html(xpath_locators, expected_data)

    def provide_order_messages(self, checkout_data):
        self.set_value_into_element(CheckoutPage.order_message_field_locator, checkout_data['singup']['order_message'])
