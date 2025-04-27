import requests
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

ebutton_1 = "//div[]"

# XPath локатори

header_logo_navigation_link = '//a[@routerlink="/" and @class="header_logo"]'
header_home_link = '//header//a[text()="Home"]'
header_about_button = '//header//button[text()="About"]'
header_contacts_button = '//header//button[text()="Contacts"]'
header_guest_login_button = '//header//button[text()="Guest log in"]'
header_sign_in_button = '//header//button[text()="Sign In"]'
header_my_profile_button = '//header//button[@id="userNavDropdown"]'
header_profile_drop_down_menu = '//header//nav[@aria-labelledby="userNavDropdown"]'
header_profile_drop_down_menu_garage = '//header//nav[@aria-labelledby="userNavDropdown"]/a[text()="Garage"]'
header_profile_drop_down_menu_fuel_expenses = '//header//nav[@aria-labelledby="userNavDropdown"]/a[text()="Fuel expenses"]'
header_profile_drop_down_menu_instructions = '//header//nav[@aria-labelledby="userNavDropdown"]/a[text()="Instructions"]'
header_profile_drop_down_menu_logout = '//header//nav[@aria-labelledby="userNavDropdown"]/button[text()="Logout"]'

main_title_text = '//div/app-home//h1'
main_paragraph_text = '//p[@class="hero-descriptor_descr lead"]/text()'
sign_up_button = '//button[text()="Sign up"]'
hero_section_video_iframe = '//section[@class="section hero"]//iframe[@class="hero-video_frame"]'
about_section = '//div[@id="aboutSection"]'

contacts_section = '//div[@id="contactsSection"]'
contacts_section_heading_text = '//div[@id="contactsSection"]//h2/text()'
facebook_link = '//div[@class="contacts_socials socials"]//a[contains(@href, "facebook.com")]'
telegram_link = '//div[@class="contacts_socials socials"]//a[contains(@href, "t.me")]'
youtube_link = '//div[@class="contacts_socials socials"]//a[contains(@href, "youtube")]'
instagram_link = '//div[@class="contacts_socials socials"]//a[contains(@href, "instagram")]'
linkedin_link = '//div[@class="contacts_socials socials"]//a[contains(@href, "linkedin.com")]'
support_email_link = '//div[@id="contactsSection"]//a[contains(@href, "mailto:developer@ithillel.ua")]'
hillel_site_link = '//div[@id="contactsSection"]//a[contains(@href, "https://ithillel.ua")]'

footer_section = '//footer'
footer_logo = '//footer//a[@class="footer_logo"]'
modal_close_button = '//div[@class="modal-header"]/button[@class="close"]' #can be used with any modal

log_in_form = '//app-signin-modal'
log_in_modal_email_input = '//app-signin-modal//input[@id="signinEmail"]'
log_in_modal_password_input = '//app-signin-modal//input[@id="signinPassword"]'
log_in_modal_remember_me_checkbox = '//div[@class="modal-body"]//div[@class="form-check"]/input'
log_in_modal_remember_me_label = '//div[@class="modal-body"]//div[@class="form-check"]/label'
log_in_modal_forgot_pussword = '//div[@class="modal-body"]//button[text()="Forgot password"]'
log_in_modal_registration_button = '//div[contains(@class, "modal-footer")]/button[text()="Registration"]'
log_in_modal_login_button_disabled = '//app-signin-modal//button[@disabled and text()="Login"]'
log_in_modal_login_button_enabled = '//app-signin-modal//button[not(@disabled) and text()="Login"]'

restore_access_modal = '//app-forgot-password-modal'
restore_access_email_input = '//app-forgot-password-modal//input[@id="signinEmail"]'
restore_access_send_button_disabled = '//app-forgot-password-modal//button[@disabled and text()="Send"]'
restore_access_send_button_enabled = '//app-forgot-password-modal//button[not(@disabled) and text()="Send"]'

registration_modal = '//app-signup-modal'
registration_modal_name_input = '//app-signup-modal//input[@id="signupName"]'
registration_modal_last_name_input = '//app-signup-modal//input[@id="signupLastName"]'
registration_modal_email_input = '//app-signup-modal//input[@id="signupEmail"]'
registration_modal_password_input = '//app-signup-modal//input[@id="signupPassword"]'
registration_modal_reenter_password_input = '//app-signup-modal//input[@id="signupRepeatPassword"]'
registration_modal_register_button_disabled = '//app-signup-modal//button[@disabled and text()="Register"]'
registration_modal_register_button_enabled = '//app-signup-modal//button[not(@disabled) and text()="Register"]'\

add_car_button = '//button[text()="Add car"]'
add_car_modal = '//app-add-car-modal'
add_car_modal_add_button_disaled = '//app-add-car-modal//button[@disabled and text()="Add"]'
add_car_modal_add_button_enabled = '//app-add-car-modal//button[not(@disabled) and text()="Add"]'
