import requests
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

ebutton_1 = "//div[]"


class HomePage:

    # header
    hillel_auto_logo = "//a[@class='header_logo']"
    home_button = "//a[@href='/' and text()='Home']"
    about_button = "//a//following-sibling::button[text()='About']"
    contacts_button = "//a//following-sibling::button[text()='Contacts']"
    guest_log_in_button = '//button[contains(@class, "guest") and text()="Guest log in"]'
    sign_in_button = '//button[contains(@class, "signin") and text()="Sign In"]'

    # body
    do_more_title = "//h1[text()='Do more!']"
    do_more_description = "//p[contains(text(), 'With the help')]"
    sign_up_button = "//p//following-sibling::button[text()='Sign up']"
    youtube_video = "//div[@class='hero-video']"

    # registration popup
    registration_popup = "//div[@class='modal-content']//h4[text()='Registration']"
    registration_name_input = "//input[@id='signupName']"
    registration_last_name_input = "//input[@id='signupLastName']"
    registration_email_input = "//input[@id='signupEmail']"
    registration_password_input = "//input[@id='signupPassword']"
    registration_repeat_password_input = "//input[@id='signupRepeatPassword']"
    registration_register_button = "//div[@class='modal-footer']//button[text()='Register']"

    # common
    close_icon = "//div[@class='modal-header']//button[@class='close']"

    # log in popup
    login_popup = "//div[@class='modal-content']//h4[text()='Log in']"
    login_email_input = "//input[@id='signinEmail']"
    login_password_input = "//input[@id='signinPassword']"
    login_remember_me_checkbox = "//div[@class='form-check']//input[@id='remember']"
    login_remember_me_text = "//div[@class='form-check']//label[text()=' Remember me ']"
    login_forgot_password_button = "//div[@class='form-check']//following-sibling::button[text()='Forgot password']"
    login_registration_button = "//div[contains(@class, 'modal-footer')]//button[text()='Registration']"
    login_button = "//div[contains(@class, 'modal-footer')]//button[text()='Login']"

    # forgot password form
    restore_access_popup = "//div[@class='modal-content']//h4[text()='Restore access']"
    restore_email_input = "//input[@id='signinEmail']"
    restore_send_button = "//div[@class='modal-footer']//button[text()='Send']"

    # about section
    fuel_expenses_img = "//img[@src='/assets/images/homepage/info_1.jpg' and @alt='Instructions']"
    instructions_img = "//img[@src='/assets/images/homepage/info_2.jpg' and @alt='Instructions']"
    log_fuel_expenses_title = "//p[text()='Log fuel expenses']"
    log_fuel_expenses_description = "//p[contains(text(), 'Keep track')]"
    instruction_title = "//p[text()='Instructions and manuals']"
    instructions_description = "//p[contains(text(), 'Watch over')]"

    # contacts section
    contacts_socials_icons_block = "//div[@class='contacts_socials socials']"
    fb_icon = "//div[contains(@class, 'socials')]//span[contains(@class, 'icon-facebook')]//ancestor::a"
    telegram_icon = "//div[contains(@class, 'socials')]//span[contains(@class, 'icon-telegram')]//ancestor::a"
    youtube_icon = "//div[contains(@class, 'socials')]//span[contains(@class, 'icon-youtube')]//ancestor::a"
    instagram_icon = "//div[contains(@class, 'socials')]//span[contains(@class, 'icon-instagram')]//ancestor::a"
    linkedin_icon = "//div[contains(@class, 'socials')]//span[contains(@class, 'icon-linkedin')]//ancestor::a"
    it_hillel_ua_label = "//a[@href='https://ithillel.ua' and text()='ithillel.ua']"
    support_email_link = "//a[@href='mailto:developer@ithillel.ua' and text()='support@ithillel.ua']"


class GaragePage(HomePage):

    # header
    garage_button = "//a[@href='/panel/garage' and text()='Garage']"
    fuel_expenses_button = "//a[@href='/panel/expenses' and text()='Fuel expenses']"
    instructions_button = "//a[@href='/panel/instructions' and text()='Instructions']"
    my_profile_dropdown = "//button[@id='userNavDropdown']"
    my_profile_garage_item = "//nav[@aria-labelledby='userNavDropdown']//a[text()='Garage']"
    my_profile_fuel_expenses_item = "//nav[@aria-labelledby='userNavDropdown']//a[text()='Fuel expenses']"
    my_profile_instructions_item = "//nav[@aria-labelledby='userNavDropdown']//a[text()='Instructions']"
    my_profile_logout_button = "//nav[@aria-labelledby='userNavDropdown']//button[text()='Logout']"
