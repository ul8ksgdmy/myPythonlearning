class Staff:
    def __init__(self, empid, name, deptname, gender, tech, age):
        self.__empid = empid
        self.__name = name
        self.__deptname = deptname
        self.__gender = gender
        self.__tech = tech
        self.__age = age

    @property
    def empid(self):
        return self.__empid

    @empid.setter
    def empid(self, value):
        self.__empid = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def deptname(self):
        return self.__deptname

    @deptname.setter
    def deptname(self, value):
        self.__deptname = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def tech(self):
        return self.__tech

    @tech.setter
    def tech(self, value):
        self.__tech = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        msg = '%s %s %s %s %s %s' % (self.__empid, self.__name, self.__deptname, self.__gender, self.__tech, self.__age)

    def printbio(self):
        if self.__gender == 'M':
            print('%s 직원은 나이가 %s이고, 성별은 남자입니다' % (self.__name, self.age))
        else:
            print('%s 직원은 나이가 %s이고, 성별은 여자입니다' % (self.__name, self.age))

e = Staff('3', 'Ernie', 'Sales', 'M', 'UNIX, Perl', '23')
e.printbio()
