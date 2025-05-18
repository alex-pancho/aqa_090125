import requests
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

# XPath
logo = '//a[@class="header_logo"]'
home_btn = '//a[@class="btn header-link -active" and text()="Home"]'
about_btn = '//nav/button[@class="btn header-link" and text()="About"]'
contacts_btn = '//nav/button[@class="btn header-link" and text()="Contacts"]'
login_btn = '//button[@class="header-link -guest"]'
singin_btn = '//button[@class="btn btn-outline-white header_signin"]'
title_text = '//h1[@class="hero-descriptor_title display-2"]'
text1 = '//p[@class="hero-descriptor_descr lead"]'
singup_btn = '//button[@class="hero-descriptor_btn btn btn-primary"]'
img1 = '//img[@src="/assets/images/homepage/info_1.jpg"]'
img2 = '//img[@src="/assets/images/homepage/info_2.jpg"]'
title2 = '//p[text()="Log fuel expenses"]'
text2 = '//div[@class="col-12 col-lg-6"]/div/p[2]'
title3 = '//p[text()="Instructions and manuals"]'
text3 = '//div[@class="col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3"]/div/p[2]'
text_cont = '//div[@class="row"]/div/h2'
icon_facebook = '//span[@class="socials_icon icon icon-facebook"]'
icon_telegram = '//span[@class="socials_icon icon icon-telegram"]'
icon_inst = '//span[@class="socials_icon icon icon-instagram"]'
icon_youtube = '//span[@class="socials_icon icon icon-youtube"]'
icon_linkedin = '//span[@class="socials_icon icon icon-linkedin"]'
cont_link = '//a[@class="contacts_link display-4"]'
cont_link2 = '//a[@class="contacts_link h4"]'
footer_text1 = '//div[contains(@class="footer_item -left")]/p[1]'
footer_text2 = '//div[contains(@class, "footer_item -left")]/p[2]'

# CSS
footer_logo = 'a.footer_logo'
my_prof_btn = '#userNavDropdown'
menu_my_prof = 'nav[aria-labelledby="userNavDropdown"]'
garage_btn = 'a[routerlink="garage"]'
garage_text = 'div[class^="panel-page_heading"] h1'
add_car_btn = 'button[class="btn btn-primary"]'
text_on_garage_pg = 'p[class="h3 panel-empty_message"]'
form_add_car = 'div[class="modal-content"]'
select_brand = '#addCarBrand'
select_model = '#addCarModel'
input_mileage = '#addCarMileage'
cancel_btn = 'button[class="btn btn-secondary"]'
add_btn = 'div[class^="modal-footer"] button[class="btn btn-primary"]'
close_btn = 'button[class="close"]'
expenses_btn = 'a[routerlink="expenses"]'
text_expenses = 'div[class^="panel-page_heading"] h1'
add_expenses = 'div[class="item-group"] button'
text_on_expenses_pg = 'p[class="h3 panel-empty_message"]'
text_link = 'p[class="h3 panel-empty_message"] a'
instructions_btn = 'a[routerlink="instructions"]'
text_on_instructions_pg = 'div[class^="panel-page_heading"] h1'
dropdown_brand = '#brandSelectDropdown'
dropdown_model = '#modelSelectDropdown'
search_btn = 'button[class^="instructions-search-controls_search"]'
logout_btn = 'a[class="btn btn-link text-danger btn-sidebar sidebar_btn"]'
