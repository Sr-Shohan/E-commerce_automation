from selenium.webdriver.common.by import By


class PaymentLocators:
    name_on_card_locator =(By.XPATH, "//input[@class='form-control' and @name='name_on_card']")
    card_number_locator = (By.XPATH, "//input[@name='card_number' and @data-qa='card-number']")
    cvc_locator = (By.XPATH, "//input[@name='cvc' and @data-qa='cvc']")
    expiraration_locator =(By.XPATH, "//input[@name='expiry_month' and @data-qa='expiry-month']")
    year_locator = (By.XPATH, "(//input[@name='expiry_year' and @data-qa='expiry-year'])[1]")
    pay_confirm_locator =(By.XPATH, "//button[@data-qa='pay-button' and @id='submit']")
    order_placed_message_locator =(By.XPATH, '//p[@style="font-size: 20px; font-family: garamond;"]')


