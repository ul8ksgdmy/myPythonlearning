#department class
class Department_VO:
    # 생성자
    def __init__(self, dpid, dpname, mgrid, locid ):
        self.__dpid = dpid
        self.__dpname = dpname
        self.__mgrid = mgrid
        self.__locid = locid

    @property
    def dpid(self):
        return self.__dpid

    @dpid.setter
    def dpid(self, value):
        self.__dpid = value

    @property
    def dpname(self):
        return self.__dpname

    @dpname.setter
    def dpname(self, value):
        self.__dpname = value

    @property
    def mgrid(self):
        return self.__mgrid

    @mgrid.setter
    def mgrid(self, value):
        self.__mgrid = value

    @property
    def locid(self):
        return self.__locid

    @locid.setter
    def locid(self, value):
        self.__locid = value

    def __str__(self):
        msg = '%d %s %d %d' % (self.__dpid, self.__dpname, self.__mgrid, self.__locid)
        return msg

