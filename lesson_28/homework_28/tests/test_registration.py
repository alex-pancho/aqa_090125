from faker import Faker
import allure

faker = Faker()


class TestRegistration:

    @allure.title("Test user registration")
    @allure.description("Test that the user was able to successfully registered")
    @allure.severity(allure.severity_level.MINOR)
    def test_user_registration(
            self, chrome_browser, open_page, open_registration_popup, fill_registration_popup,
            send_registration_popup, check_switch_to_garage_page
    ):
        with allure.step("Open page and registration popup"):
            open_page()

        with allure.step("Open registration popup"):  
            open_registration_popup()

        passowrd = faker.password()

        with allure.step("Fill registration popup"):
            fill_registration_popup(
                name=faker.last_name(),
                last_name=faker.last_name(), 
                email=faker.email(),
                password=passowrd,
                repeat_password=passowrd,
            )

        with allure.step("Send registration popup"):
            send_registration_popup()
        with allure.step("Check switch to garage page"):    
            check_switch_to_garage_page()
        