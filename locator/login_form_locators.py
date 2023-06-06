from selenium.webdriver.common.by import By


class HomepageLocators:
    # Add to cart
    feature_title_locator = (By.XPATH, '(//h2[@class= "title text-center"])[1]')
    add_cart_initial_locator = (By.XPATH, "(//h2[contains(text(), 'Rs. 500')])[1]")
    add_cart_locator = (By.XPATH, '(//a[@data-product-id="1"])[1]')
    modal_cart_locator = (By.XPATH, "//a[@href='/view_cart']/u[contains(text(), 'View Cart')]")

    checkout_button_locator = (By.XPATH, "//a[@class='btn btn-default check_out' and contains(text(), 'Proceed To Checkout')]")
    register_login_button_locator = (By.XPATH, "//a[@href='/login']/u[contains(text(), 'Register / Login')]")
    view_cart_button_locator = (By.XPATH, "//a[@href='/view_cart']/u[contains(text(), 'View Cart')]")
    home_cart_locator = (By.XPATH, "//a[contains(., 'Cart') and .//i[contains(@class, 'fa-shopping-cart')]]")





