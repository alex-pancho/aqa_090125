def test_user_can_register(fill_registration_form, check_redirect_to_garage):
    fill_registration_form()
    heading = check_redirect_to_garage()
    assert "garage" in heading.lower(), "Користувача не перенаправлено в Garage" 