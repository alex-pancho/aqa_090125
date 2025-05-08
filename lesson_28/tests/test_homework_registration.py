
from faker import Faker

faker = Faker()


class TestRegistration:

    def test_user_registration(
            self, chrome_browser, open_page, open_form_registration, fill_form_registration_and_send,
            send_form_registration, check_switch_to_garage_page
    ):
        open_page()
        open_form_registration()

        passowrd = faker.password()

        fill_form_registration_and_send(
            name=faker.last_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=passowrd,
            repeat_password=passowrd,
        )

        send_form_registration()
        check_switch_to_garage_page()
