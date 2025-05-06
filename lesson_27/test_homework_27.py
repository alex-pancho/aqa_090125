import pytest
from homework_27 import TrackingNovaPoshta

def test_tracking_status(browser):
    url = "https://tracking.novaposhta.ua/#/uk"
    tracking_number = "20451154620489"
    expected_status = "Отримана"

    tracker = TrackingNovaPoshta(browser)
    tracker.tracking_page(url)
    tracker.enter_track_number(tracking_number)
    tracker.click_button()
    status = tracker.get_status()

    assert status == expected_status