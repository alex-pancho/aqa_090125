import pytest
from homework_27 import TrackingNovaPoshta

# Тестові дані: [номер накладної, очікуваний статус]
test_data = [
    ("20400447176194", "Відправлення отримано. Грошовий переказ видано одержувачу."),
    ("20451155377071", "Отримана"),
]

@pytest.mark.parametrize("tracking_number,expected_status", test_data)
def test_tracking_status(browser, tracking_number, expected_status):
    url = "https://tracking.novaposhta.ua/#/uk"
    tracker = TrackingNovaPoshta(browser)

    # Відкриття сторінки трекінгу
    tracker.open_tracking_page(url)

    # Взаємодія з номером накладної
    tracker.enter_tracking_number(tracking_number)
    tracker.click_search_button()

    # Отримання статусу
    status = tracker.get_tracking_status()

    # Перевірка
    assert expected_status in status, f"Очікувано: {expected_status}, отримано: {status}"
