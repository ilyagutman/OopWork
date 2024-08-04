class Person:
    # first_name = ""
    # last_name = ""
    # age = 0
    # social_security = ""

    def __init__(self, fn: str, ln: str, ag: int, ss: str):
        self.__first_name = fn
        self.__last_name = ln
        self.__age = ag
        self.__social_security = ss

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: str):
        self.__age = value

    @property
    def social_security(self):
        return self.__social_security

    @social_security.setter
    def social_security(self, value: str):
        self.__social_security = value

    def to_string(self):
        string = f"First name={self.first_name} Last name={self.last_name} Age={self.age} Social Security={self.social_security}"
        return string

