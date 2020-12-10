class Person:
    def __init__(self):
        self._first_name = str()
        self._last_name = str()
        self._day = int()
        self._month = int()
        self._year = int()

    def set_name(self, forename, surname):
        self._first_name = forename
        self._last_name = surname

    def get_name(self):
        return self._first_name + " " + self._last_name

    def set_dob(self, d, m, y):
        if self._is_valid_date(d, m):
            self._day = int(d)
            self._month = int(m)
            self._year = int(y)
        else:
            return "Invalid date entered."

    def get_dob(self):
        return "{0}-{1}-{2}".format(self._day, self._month, self._year)

    def get_age_at(self, d, m, y):
        age = -1
        if self._is_valid_date(d, m) and self._is_after_dob(d, m, y):
            age = y - self._year
            if (m < self._month) or (m == self._month and d < self._day):
                age -= 1
        return age

    def get_details(self):
        return "{0}, {1}".format(self.get_name(), self.get_dob())

    def _is_valid_date(self, d, m):
        return 0 < d <= 31 and 0 < m <= 12

    def _is_after_dob(self, d, m, y):
        return (y > self._year) or\
               (y == self._year and m > self._month) or\
               (y == self._year and m == self._month and d > self._day)


john = Person()  # create the new Person, john
john.set_name("John", "Lennon")  # set john Person objects name
john.set_dob(8, 10, 1940)  # set john Person objects date of birth
print(john.get_name())  # print john's name
print(john.get_dob())  # print john's dob
print("-------------")
paul = Person()
paul.set_name("Paul", "McCartney")
paul.set_dob(18, 6, 1942)
print(paul.get_name())
print(paul.get_dob())
print("-------------")
george = Person()
george.set_name("George", "Harrison")
george.set_dob(25, 2, 1943)
print(george.get_name())
print(george.get_dob())
print("-------------")
ringo = Person()
ringo.set_name("Ringo", "Starr")
ringo.set_dob(7, 7, 1940)
print(ringo.get_name())
print(ringo.get_dob())

