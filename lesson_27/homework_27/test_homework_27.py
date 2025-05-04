from tracking_page_class import TrackingPage


URL_NOVA_POSHTA = "https://tracking.novaposhta.ua/#/uk"
TRACKING_NUMBER = "20451154620489"


class TestTrackingNumber:

    def test(self, browser_chrome):
        tracking_page = TrackingPage(browser_chrome)
        tracking_page.open_page(URL_NOVA_POSHTA)

        tracking_page.fill_input('//div/input[@class="track__form-group-input"]', TRACKING_NUMBER) 
        tracking_page.click_button('//input[@class="track__form-group-btn green-active"]')
        package_status = tracking_page.find_element('//div[@class="header__status-text"]')
        
        assert package_status.text == "Отримана"
        