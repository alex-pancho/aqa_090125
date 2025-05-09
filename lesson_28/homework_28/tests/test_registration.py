from faker import Faker

faker = Faker()


class TestRegistration:

    def test_user_registration(
            self, chrome_browser, open_page, open_registration_popup, fill_registration_popup,
            send_registration_popup, check_switch_to_garage_page
    ):
        open_page()
        open_registration_popup()

        passowrd = faker.password()

        fill_registration_popup(
            name=faker.last_name(),
            last_name=faker.last_name(), 
            email=faker.email(),
            password=passowrd,
            repeat_password=passowrd,
        )

        send_registration_popup()
        check_switch_to_garage_page()
        