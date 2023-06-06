from selenium.webdriver.common.by import By


class CheckoutPage:
    full_name_locator = (
    By.XPATH, "//li[contains(@class, 'address_firstname') and contains(@class, 'address_lastname')]")
    company_name_locator = (
    By.XPATH, "(//li[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[1]")
    zip_road_locator = (By.XPATH, "(//li[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[2]")
    address2_locator = (By.XPATH, "(//li[contains(@class, 'address_address1') and contains(@class, 'address_address2')])[3]")
    city_state_locator = (By.XPATH, "(//li[contains(@class, 'address_city')][contains(@class, 'address_state_name')][contains(@class, 'address_postcode')])[1]")
    country_locator =(By.XPATH, "(//li[contains(@class, 'address_country_name')])[1]")
    mobile_number_locator = (By.XPATH , "(//li[contains(@class, 'address_phone')])[1]")
    order_message_field_locator = (By.XPATH, "//textarea[@name='message']")
    place_order_button = (By.XPATH, "//a[@class='btn btn-default check_out' and @href='/payment']")

