import json
import os
import pytest
from locator.checkout_page_locator import CheckoutPage
from locator.payment_page_locator import PaymentLocators
from pages.Home.checkout_page import Checkout
from pages.Home.home_page import homepage
from pages.Home.payment_page import PaymentPage
from pages.Home.register_login_page import RegisterLogin
from locator.login_form_locators import HomepageLocators
from locator.Register_login_form_locator import RegisterLoginForm


def test_login(driver):
    # Create a new instance of the Home page
    home_page = homepage(driver)
    register_login = RegisterLogin(driver)
    checkout_page = Checkout(driver)
    payment_page= PaymentPage(driver)
    # Load the Home page
    home_page.load_URL()
    # Verify that home page is visible successfully
    assert "Automation Exercise" in driver.title
    # Using this because due to google adds, preventing ElementClickInterceptedException
    driver.execute_script("window.scrollBy(0, 500)")
    # Add products to cart and Click 'Cart' button
    home_page.add_cart_item()
    # Verify that cart page is displayed (assert BY URL also can do some other strategy)
    assert 'https://automationexercise.com/view_cart' in driver.current_url
    # Click Proceed To Checkout
    home_page.click_on_element(HomepageLocators.checkout_button_locator)
    # Click 'Register / Login' button
    home_page.click_on_element(HomepageLocators.register_login_button_locator)
    # Set the working directory to the root directory of project
    project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(project_directory)
    with open('assets/register_data.json') as json_file:
        register_data = json.load(json_file)
    # Provided Registration DATA
    register_login.provide_initial_register_info(register_data)

    # Fill all details in Sign up and create account
    with open('assets/singup_data.json') as json_file:
        singup_data = json.load(json_file)
    register_login.provide_singup_info(singup_data)
    # Verify 'ACCOUNT CREATED!'
    account_created_text = driver.find_element(*RegisterLoginForm.account_created_text_locator).text
    assert "ACCOUNT CREATED!" in account_created_text
    # Click 'Continue' button
    register_login.click_on_element(RegisterLoginForm.continue_button_locator)

    # Verify ' Logged in as username' at top
    logged_as_text = driver.find_element(*RegisterLoginForm.logginAs_locator).text
    assert "Logged in as Test User" in logged_as_text
    # Click 'Cart' button
    home_page.click_on_element(HomepageLocators.add_cart_locator)
    home_page.click_on_element(HomepageLocators.view_cart_button_locator)
    # Click 'Proceed To Checkout' button
    home_page.click_on_element(HomepageLocators.checkout_button_locator)
    # Verify Address Details and Review Your Order
    checkout_page.perform_checkout()
    # Enter description in comment text area and
    checkout_page.provide_order_messages(singup_data)
    # Click 'Place Order'
    checkout_page.click_on_element(CheckoutPage.place_order_button)
    # Enter payment details: Name on Card, Card Number, CVC, Expiration date
    with open('assets/payment_data.json') as json_file:
        payment_data = json.load(json_file)
    payment_page.provide_payment_info(payment_data)
    # Verify the success message 'Your order has been placed successfully!'
    order_placed_text = driver.find_element(*PaymentLocators.order_placed_message_locator).text
    assert "Congratulations! Your order has been confirmed!" in order_placed_text

