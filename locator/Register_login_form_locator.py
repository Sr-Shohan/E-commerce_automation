from selenium.webdriver.common.by import By


class RegisterLoginForm:
    # Initial register Info
    register_name_locator = (By.XPATH, '//input[@name= "name"]')
    register_email_locator = (By.XPATH, "//input[@name='email' and @data-qa='signup-email']")
    register_submit_button_locator = (By.XPATH, "//button[@type='submit' and @data-qa='signup-button']")

    # singUp info Locator
    gender_title_locator = (By.XPATH, "//input[@id='id_gender1']")
    password_locator = (By.XPATH, '//input[@id="password"]')
    first_name_locator = (By.XPATH, '//input[@id="first_name"]')
    last_name_locator = (By.XPATH, '//input[@id="last_name"]')
    company_locator = (By.XPATH, '//input[@id="company"]')
    address1_locator = (By.XPATH, '//input[@id="address1"]')
    address2_locator = (By.XPATH, '//input[@id="address2"]')
    state_locator = (By.XPATH, '//input[@id="state"]')
    city_locator = (By.XPATH, '//input[@id="city"]')
    zip_locator = (By.XPATH, '//input[@id="zipcode"]')
    mobile_number_locator = (By.XPATH, '//input[@id="mobile_number"]')
    create_account_locator = (By.XPATH, '//button[@data-qa="create-account" and @type="submit"]')
    account_created_text_locator = (By.XPATH, '//h2[@class="title text-center" and @data-qa="account-created"]//b')
    continue_button_locator = (By.XPATH, '//a[@href="/" and @data-qa="continue-button" and contains(@class, "btn-primary")]')
    logginAs_locator = (By.XPATH, "//a[contains(., 'Logged in as') and .//b[text()='Test User']]")

    # label
    country_label = 'Country '








