import pytest
from homework_14 import SiteUser

def test_siteuser_initialization():
    user = SiteUser("John Doe", "john.doe@example.com", "user")
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"
    assert user.level_access == "user"
    assert user.logcount == 0

def test_track_logcount():
    user = SiteUser("John Show", "john.show@example.com", "admin")
    user.track_logcount()
    assert user.logcount == 1
    user.track_logcount()
    assert user.logcount == 2

def test_siteuser_str():
    user = SiteUser("Clara Osvin Osvald", "osvin.osvald@example.com", "user")
    assert str(user) == "SiteUser: Clara Osvin Osvald, email: osvin.osvald@example.com, access level: user, logcount: 0"

def test_siteuser_eq_true():
    user1 = SiteUser("Rose Tyler", "rose.tyler@example.com", "admin")
    user2 = SiteUser("Amelia Pond", "amelia.pond@example.com", "admin")
    assert user1 == user2

def test_siteuser_eq_false():
    user1 = SiteUser("Rory Wiliams", "rory.wiliams@example.com", "user")
    user2 = SiteUser("River Song", "river.song@example.com", "admin")
    assert user1 != user2