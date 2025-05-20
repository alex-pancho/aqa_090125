def test_user_can_register(fill_registration_form, garage_page):
    """Тест реєстрації користувача і перевірки перенаправлення в Garage."""
    fill_registration_form()
    heading = garage_page.get_heading_text()
    assert "garage" in heading.lower(), "Користувача не перенаправлено в Garage"
