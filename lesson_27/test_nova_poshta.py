
from lesson_27.tracking_novaposhta_page import TrackingNovaposhtaPage

NOVAPOSHT_URL = 'https://tracking.novaposhta.ua/#/uk'
PACKAGE_NUMBER = "20400450781079"


class TestNovaPoshta:

    def test_nova_poshta(self, chrome_browser):
        page = TrackingNovaposhtaPage(chrome_browser)
        page.open_page(NOVAPOSHT_URL)

        page.fill_input(page.package_number_input, PACKAGE_NUMBER)
        chrome_browser.execute_script("localStorage.setItem('alreadyVisited', 'true');")
        page.click_element(page.search_button)

        package_status = page.find_element(page.package_status_text)
        assert package_status.text == "Отримана"
