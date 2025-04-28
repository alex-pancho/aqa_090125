import requests
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

# username = "guest"
# passwd = "welcome2qauto"
# url = f"https://{username}:{passwd}@qauto2.forstudy.space"
#
# ebutton_1 = "//div[]"


# XPath for GARAGE PAGE URL: https://qauto2.forstudy.space/panel/garage

# 1. 'Add car' button
'//button[@class="btn btn-primary" and text()="Add car"]'

# 4. Text label 'Garage' on 'Car list page'
'//div[@class="panel-page"]//h1[text()="Garage"]'

# 26. Empty garage text message block
'//div[@class="panel-page_content"]//p/text()'

# 27. Array of car logo in the garage
'//div[@class="panel-page_content"]//img[@class="car-logo_img"]'

# 28. Get 'edit car' button if we have multiple cars.
'//ul[@class="car-list"]/li[1]//span[@class="icon icon-edit"]'

# 29. Get 'Add fuel expense' button
'//ul[@class="car-list"]/li[1]//button[contains(@class, "car_add-expense")]'

# 36. Tachometer object on the car details page
'//div[@class="panel-page_content"]//li[1]//span[@class="update-mileage-form_icon icon icon-tachometer"]'

# 37. Update mileage for car
'//div[@class="panel-page_content"]//li[1]//input'

# 38. Car name on the car details page
'//div[@class="panel-page_content"]//li[1]//p[contains(@class, "car_name"]'

# 39. 'Update' button on the car details page
'//div[@class="panel-page_content"]//li[1]//button[contains(@class, "update-mileage-form_submit")]'


# XPath for MAIN PAGE.

# 2. <a> object Header Logo
'//a[@class="header_logo"]'

# 3. User photo near 'Profile' menu
'//img[@class="icon-btn" and @alt="User photo"]'

# 5. 'Log out' object in the left sidebar menu
'//a[contains(@class, "sidebar_btn") and span[@class="icon icon-logout"]]'

# 6. 'Instructions' object in the left sidebar menu
'//a[contains(@class, "sidebar_btn") and span[@class="icon icon-instructions"]]'

# 7. 'Fuel expenses' object in the left sidebar menu
'//a[contains(@class, "sidebar_btn") and span[@class="icon icon-fuel"]]'

# 8. 'Garage' object in the left sidebar menu
'//a[contains(@class, "sidebar_btn") and span[@class="icon icon-garage"]]'

# 9. 'Logo' in the footer
'//a[@class="footer_logo"]'

# 10. <p> Text object 'Hillel' description text in the footer
'//footer//div[@class="col-7 d-flex flex-column justify-content-center footer_item -left"]/p[2]'

# 11. <p> Text object with copyright info in the footer
'//footer//div[@class="col-7 d-flex flex-column justify-content-center footer_item -left"]/p[1]'

# 14. 'Garage' object in the header nav menu
'//nav[contains(@class, "header_nav")]/a[@href="/panel/garage"]'

# 15. 'Fuel expenses' object in the header nav menu
'//nav[contains(@class, "header_nav")]/a[@href="/panel/expenses"]'

# 16. 'Instruction' object in the header nav menu
'//nav[contains(@class, "header_nav")]/a[@href="/panel/instructions"]'

# 17. 'Garage' object in the header Profile dropdown menu
'//nav[contains(@class, "user-nav_menu dropdown-menu")]/a[text()="Garage"]'

# 18. 'Fuel expenses' object in the header Profile dropdown menu
'//nav[contains(@class, "user-nav_menu dropdown-menu")]/a[text()="Fuel expenses"]'

# 19. 'Instructions' object in the header Profile dropdown menu
'//nav[contains(@class, "user-nav_menu dropdown-menu")]/a[text()="Instructions"]'

# 20. 'Logout' object in the header Profile dropdown menu
'//nav[contains(@class, "user-nav_menu dropdown-menu")]/button[text()="Logout"]'

# 21. 'Profile' button
'//button[@id="userNavDropdown"]'


# XPath for FUEL EXPENSES PAGE URL: https://qauto2.forstudy.space/panel/expenses

# 12. 'Add expenses' button
'//button[@class="btn btn-primary" and text()="Add an expense"]'

# 13. Text label 'Fuel expenses' on 'Fuel expenses page'
'//div[@class="panel-page"]//h1[text()="Fuel expenses"]'

# 32. Get 1st row of expenses table (depends on date)
'(//table[@class="table expenses_table"]//tr[td[text()="28.04.2025"]])[1]'

# 33. Get 'Trash' object in expenses row
'(//table[@class="table expenses_table"]//tr[td[text()="28.04.2025"]])[1]/td/button[@class="btn btn-delete"]'

# 34. Select car field
'//button[@id="carSelectDropdown"]'

# 35. Get 'Edit' object in expenses row
'(//table[@class="table expenses_table"]//tr[td[text()="28.04.2025"]])[1]/td/button[@class="btn btn-edit"]'

# 40. Mileage for trip for selected date
'(//table[@class="table expenses_table"]//tr[td[text()="28.04.2025"]])[1]/td[2]/text()'

# 41. Total cost of fuel for trip for selected date
'(//table[@class="table expenses_table"]//tr[td[text()="28.04.2025"]])[1]/td[4]/text()'


# XPath for INSTRUCTIONS PAGE URL: https://qauto2.forstudy.space/panel/instructions

# 22. 'Search' button
'//div[@class="instructions"]//button[text()="Search"]'

# 23. Text label 'Instructions' on 'Instructions page'
'//div[@class="panel-page"]//h1[text()="Instructions"]'

# 24. Car 'Brand' choosing button
'//div[@class="instructions"]//button[@id="brandSelectDropdown"]'

# 25. Car 'Model' choosing button
'//div[@class="instructions"]//button[@id="modelSelectDropdown"]'

# 30. Instruction block #1
'//li[@class="instruction-list_item"][1]/a'

# 31. 'Download' link in instruction block #1
'//li[@class="instruction-list_item"][1]/a/a[@class="instruction-link_download"]'

