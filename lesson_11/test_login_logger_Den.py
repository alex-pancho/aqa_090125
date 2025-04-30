import pytest
import logging
from login_logger_Den import log_event


def test_log_success(caplog):
    """Тестирует логирование статуса success на уровне INFO"""
    with caplog.at_level(logging.INFO):
        log_event("TestUser", "success")

    assert "Login event - Username: TestUser, Status: success" in caplog.text


def test_log_expired(caplog):
    """Тестирует логирование статуса expired на уровне WARNING"""
    with caplog.at_level(logging.WARNING):
        log_event("TestUser", "expired")

    assert "Login event - Username: TestUser, Status: expired" in caplog.text


def test_log_failed(caplog):
    """Тестирует логирование статуса failed на уровне ERROR"""
    with caplog.at_level(logging.ERROR):
        log_event("TestUser", "failed")

    assert "Login event - Username: TestUser, Status: failed" in caplog.text


def test_log_unknown_status(caplog):
    """Тестирует логирование статуса unknown на уровне ERROR"""
    with caplog.at_level(logging.ERROR):
        log_event("TestUser", "unknown")

    assert "Login event - Username: TestUser, Status: unknown" in caplog.text


def test_log_epty_username(caplog):
    """Тестирует логирование пустого имя пользователя на уровне ERROR"""
    with caplog.at_level(logging.ERROR):
        log_event("", "failed")

    assert "Login event - Username: , Status: failed" in caplog.text


def test_log_invalid_username_type(caplog):
    """Тестирует логирование невалидного типа данных имя пользователя на уровне ERROR"""
    with pytest.raises(TypeError):
        log_event(None, "unknown")

    assert TypeError in caplog.text



