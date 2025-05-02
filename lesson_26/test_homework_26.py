import pytest

from lesson_26.frame_page import FramePage

FRAME_1_SECRET_TEXT = "Frame1_Secret"
FRAME_2_SECRET_TEXT = "Frame2_Secret"

ALERT_TEXT = "Верифікація пройшла успішно!"

FRAME_DATA = {
    "frame_1": {
        "frame_block": "frame_1_block",
        "frame_input": "frame_1_input",
        "verify_button": "frame_1_verify_button",
        "secret_text": FRAME_1_SECRET_TEXT,
    },
    "frame_2": {
        "frame_block": "frame_2_block",
        "frame_input": "frame_2_input",
        "verify_button": "frame_2_verify_button",
        "secret_text": FRAME_2_SECRET_TEXT,
    }
}


class TestFrames:

    @pytest.mark.parametrize("frame", FRAME_DATA.values(), ids=FRAME_DATA.keys())
    def test_frame(self, driver, frame):
        page = FramePage(driver)
        page.open_page()

        page.switch_to_frame(getattr(page, frame["frame_block"]))
        page.fill_field(frame["secret_text"], getattr(page, frame["frame_input"]))
        page.click_verify_button(getattr(page, frame["verify_button"]))

        page.verify_alert_text_and_close(ALERT_TEXT)
