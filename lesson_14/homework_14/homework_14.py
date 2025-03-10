class SiteUser:
    def __init__(self, name, email, access_level):
        self.__name = name
        self.__email = email
        self.__access_level = access_level
        self.__logcount = 0

    def __str__(self):
        return f"SiteUser: {self.__name}, mailbox: {self.__email}, access level: {self.__access_level}"

    def __eq__(self, other):
        if isinstance(other, SiteUser):
            return self.__access_level == other.__access_level
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def access_level(self):
        return self.__access_level

    @access_level.setter
    def access_level(self, value):
        self.__access_level = value

    @property
    def logcount(self):
        return self.__logcount

    def increment_logcount(self):
        self.__logcount += 1

