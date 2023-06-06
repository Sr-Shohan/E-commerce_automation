from pages.base_page import BasePage
from locator.payment_page_locator import PaymentLocators


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def provide_payment_info(self, payment_data):
        # Enter payment details: Name on Card, Card Number, CVC, Expiration date
        self.set_value_into_element(PaymentLocators.name_on_card_locator, payment_data['payment']['nameOnCard'])
        self.set_value_into_element(PaymentLocators.card_number_locator, payment_data['payment']['cardNumber'])
        self.set_value_into_element(PaymentLocators.cvc_locator, payment_data['payment']['cvc'])
        self.set_value_into_element(PaymentLocators.expiraration_locator, payment_data['payment']['expirationMonth'])
        self.set_value_into_element(PaymentLocators.year_locator, payment_data['payment']['expirationYear'])
        # Click 'Pay and Confirm Order' button
        self.click_on_element(PaymentLocators.pay_confirm_locator)
