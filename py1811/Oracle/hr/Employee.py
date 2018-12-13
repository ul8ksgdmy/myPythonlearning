
class Employee_VO:
    def __init__(self, empid, fnmae, lname, email, phone, hdate, jobid, sal, comm, mgrid, dpid):
        self.__empid = empid
        self.__fname = fnmae
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__sal = sal
        self.__comm = comm
        self.__mgrid = mgrid
        self.__dpid = dpid

    @property
    def empid(self):
        return self.__empid

    @empid.setter
    def empid(self, value):
        self.__empid = value

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, value):
        self .__fname = value

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, value):
        self.__lname = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def hdate(self):
        return self.__hdate

    @hdate.setter
    def hdate(self, value):
        self.__hdate = value

    @property
    def jobid(self):
        return self.__jobid

    @jobid.setter
    def jobid(self, value):
        self.__jobid = value

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, value):
        self.__sal = value

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, value):
        self.__comm = value

    @property
    def mgrid(self):
        return self.__mgrid

    @mgrid.setter
    def mgrid(self, value):
        self.__mgrid

    @property
    def dpid(self):
        return self.__dpid

    @dpid.setter
    def dpid(self, value):
        self.__dpid = value

    def __str__(self):
        msg = '%d %s %s %s %s %s %s %d %.2f %d %d' \
              % (self.__empid, self.__fname, self.__lname, self.__email, self.__phone, self.__hdate, self.__jobid, self.__sal, self.__comm, self.__mgrid, self.__dpid)
        return msg
