import pytest
from homework_27 import NovaPoshtaTracker

test_data = [
    ("20400447176194", "Відправлення отримано. Грошовий переказ видано одержувачу."),
    ("20451155377071", "Отримана")
    ]

@pytest.mark.parametrize("tracking_number,expected_status", test_data)
def test_nova_poshta_status(browser, tracking_number, expected_status):
    tracker = NovaPoshtaTracker(browser)
    actual_status = tracker.get_parcel_status(tracking_number)
    assert expected_status in actual_status