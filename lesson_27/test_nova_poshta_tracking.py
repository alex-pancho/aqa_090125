import pytest
from nova_post_page_objects import NovaPoshtaTrackingPage


def test_track_parcel_status(firefox_browser):
    """Тест для перевірки статусу посилки на сайті Нової Пошти."""
    url = "https://tracking.novaposhta.ua/#/uk"
    tracking_number = "20451153569328"
    expected_status = "Відправлення отримано. Грошовий переказ видано одержувачу."

    tracking_page = NovaPoshtaTrackingPage(firefox_browser)
    tracking_page.open_tracking_page(url)
    tracking_page.enter_tracking_number(tracking_number)
    tracking_page.click_track_button()
    actual_status = tracking_page.get_parcel_status()
    assert actual_status == expected_status, f"Очікуваний статус: '{expected_status}', Фактичний статус: '{actual_status}'"