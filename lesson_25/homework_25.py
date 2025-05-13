import requests
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

# ========== XPath ЛОКАТОРИ ==========

# Home page
'''1''' logo = '//a[@class="header_logo"]'
'''2''' home = '//a[@class="btn header-link -active"]'
'''3''' about = '//button[text()="About"]'
'''4''' contacts = '//button[text()="Contacts"]'
'''5''' guest_log_in = '//button[@class="header-link -guest"]'
'''6''' sing_in = '//button[@class="btn btn-outline-white header_signin"]'
'''7''' title_do_more = '//h1[@class="hero-descriptor_title display-2"]'
'''8''' descr_do_more = '//p[@class="hero-descriptor_descr lead"]'
'''9''' sing_up = '//button[@class="hero-descriptor_btn btn btn-primary"]'
'''10''' youtube_video = '//div[@class="hero-video"]'
'''11''' img_log = '//img[@src="/assets/images/homepage/info_1.jpg"]'
'''12''' title_log = '//p[@class="about-block_title h2" and text()="Log fuel expenses"]'
'''13''' descr_log = '//div[@class="col-12 col-lg-6"]/div/p[2]'
'''14''' img_instr = '//img[@src="/assets/images/homepage/info_2.jpg"]'
'''15''' title_instr = '//p[@class="about-block_title h2" and text()="Instructions and manuals"]'
'''16''' descr_instr = '//div[@class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"]/div/p[2]'
'''17''' facebook = '//span[@class="socials_icon icon icon-facebook"]'
'''18''' telegram = '//span[@class="class="socials_icon icon icon-telegram""]'
'''19''' youtube = '//span[@class="socials_icon icon icon-youtube"]'
'''20''' instagram = '//span[@class="socials_icon icon icon-instagram"]'
'''21''' linkedin = '//span[@class="socials_icon icon icon-linkedin"]'
'''22''' link_ithillel = '//a[@class="contacts_link display-4"]'
'''23''' link_support = '//a[@class="contacts_link h4"]'
'''24''' img_logo = '//a[@class="footer_logo"]'
'''25''' text_footer_1 = '//div[(@class="col-7 d-flex flex-column justify-content-center footer_item -left")]/p[1]'
'''26''' text_footer_2 = '//div[(@class="col-7 d-flex flex-column justify-content-center footer_item -left")]/p[2]'

# ========== CSS ЛОКАТОРИ ==========

# log in modal
'''1''' login_modal_title = 'app-signin-modal h4.modal-title'
'''2''' login_email_input = 'app-signin-form #signinEmail'
'''3''' login_password_input = 'app-signin-form #signinPassword'
'''4''' login_remember = 'app-signin-form #remember'
'''5''' login_forgot_pw = 'app-signin-form div.modal-body button.btn.btn-link'
'''6''' login_registration = 'app-signin-modal div.modal-footer button.btn.btn-link'
'''7''' login_login = 'app-signin-modal div.modal-footer button.btn.btn-primary'
# Restore access modal
'''8''' restore_modal_title = 'app-forgot-password-modal h4.modal-title'
'''9''' restore_email_input = 'app-forgot-password-form #signinEmail'
'''10''' restore_send = 'app-forgot-password-modal div.modal-footer button.btn.btn-primary'
# Registration modal
'''11''' reg_modal_title = 'app-signup-modal h4.modal-title'
'''12''' reg_name_input = 'app-signup-form #signupName'
'''13''' reg_lastname_input = 'app-signup-form #signupLastName'
'''14''' reg_email_input = 'app-signup-form #signupEmail'
'''15''' reg_password_input = 'app-signup-form #signupPassword'
'''16''' reg_reenter_input = 'app-signup-form #signupRepeatPassword'
'''17''' reg_register = 'app-signup-modal div.modal-footer button.btn.btn-primary'
# Garage page
'''18''' garage_header = 'a[routerlink="/panel/garage"].btn.header-link.-active'
'''19''' fuel_expenses_header = 'a[routerlink="/panel/expenses"].btn.header-link'
'''20''' instructions_header = 'a[routerlink="/panel/instructions"].btn.header-link'
'''21''' my_profile = 'div.user-nav.dropdown'
'''22''' my_profile_dropdown = 'nav.user-nav_menu.dropdown-menu.show'
'''23''' log_out = 'a.btn.btn-link.text-danger.btn-sidebar.sidebar_btn'
'''24''' garage_sidebar = 'a[routerlink="garage"]'
'''25''' fuel_expenses_sidebar = 'a[routerlink="expenses"]'
