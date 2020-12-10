class Person:
    def __init__(self):
        self._first_name = str()
        self._last_name = str()
        self._day = int()
        self._month = int()
        self._year = int()
        self._height = int()  # height private variable

    def set_name(self, forename, surname):
        self._first_name = forename
        self._last_name = surname

    def set_surname(self, surname):
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
        return (y > self._year) or \
               (y == self._year and m > self._month) or \
               (y == self._year and m == self._month and d > self._day)

    def set_height(self, height_in_inches):  # take in the height as a parameter, and set private height varaible
        self._height = height_in_inches

    def get_height(self):  # convert height varaible to feet and inches
        total_inches = self._height  # height in inches
        feet = self._height // 12  # convert total to feet (12 inches in a foot) // always gives a full int
        inches = self._height % 12  # get the sum remainder, and place into inches
        return "{} feet {} inches".format(feet, inches)

    def print_person(self):
        print("{}, {}, age on 7th November 2012: {}, {}"\
            .format(self.get_name(), self.get_dob(), self.get_age_at(7, 11, 2012), self.get_height()))


mum = Person()  # create the new Person, john
mum.set_name("Juliet", "Capulet")  # set john Person objects name
mum.set_dob(7, 11, 1987)  # set john Person objects date of birth
mum.set_height(68)
mum.print_person()
print("-------------")
dad = Person()  # create the new Person, john
dad.set_name("Romeo", "Montague")  # set john Person objects name
dad.set_dob(21, 2, 1983)  # set john Person objects date of birth
dad.set_height(73)
dad.print_person()
print("-------------")
son = Person()  # create the new Person, john
son.set_name("Triolus", "Montague")  # set john Person objects name
son.set_dob(12, 4, 2009)  # set john Person objects date of birth
son.set_height(33)
son.print_person()
print("-------------")
daughter = Person()  # create the new Person, john
daughter.set_name("Cressida", "Montague")  # set john Person objects name
daughter.set_dob(13, 10, 2007)  # set john Person objects date of birth
daughter.set_height(40)
daughter.print_person()