from locator.Register_login_form_locator import RegisterLoginForm
from pages.base_page import BasePage


class RegisterLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def provide_initial_register_info(self, register_data):
        self.set_value_into_element(RegisterLoginForm.register_name_locator,
                                    register_data['registration']['name'])
        self.set_value_into_element(RegisterLoginForm.register_email_locator, register_data['registration']['email'])
        self.click_on_element(RegisterLoginForm.register_submit_button_locator)

    def provide_singup_info(self, singup_data):
        self.click_on_element(RegisterLoginForm.gender_title_locator)
        self.set_value_into_element(RegisterLoginForm.password_locator, singup_data['singup']['password'])
        self.set_value_into_element(RegisterLoginForm.first_name_locator, singup_data['singup']['firstName'])
        self.set_value_into_element(RegisterLoginForm.last_name_locator, singup_data['singup']['lastName'])
        self.set_value_into_element(RegisterLoginForm.company_locator, singup_data['singup']['company'])
        self.set_value_into_element(RegisterLoginForm.address1_locator, singup_data['singup']['address1'])
        self.set_value_into_element(RegisterLoginForm.address2_locator, singup_data['singup']['address2'])
        self.set_value_into_element(RegisterLoginForm.state_locator, singup_data['singup']['state'])
        self.set_value_into_element(RegisterLoginForm.city_locator, singup_data['singup']['city'])
        self.set_value_into_element(RegisterLoginForm.zip_locator, singup_data['singup']['zipcode'])
        self.set_value_into_element(RegisterLoginForm.mobile_number_locator, singup_data['singup']['mobileNumber'])
        self.select_dropdown_value(RegisterLoginForm.country_label, singup_data['singup']['country'])
        self.click_on_element(RegisterLoginForm.create_account_locator)



