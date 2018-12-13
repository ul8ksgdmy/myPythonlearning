from py1811.Oracle.hr.Employee import Employee_VO
from py1811.Oracle.hr.Department import Department_VO

class HRService:
    def readEmp(self):
        empid = int(input('사번은? : '))
        fname = input('이름은? : ')
        lname = input('성은? : ')

        return Employee_VO(empid, fname, lname, '', '', '', '', 0, 0.0, 0, 0)

    def readDept(self):
        dpid = int(input('부서번호는? : '))
        fname = input('부서이름은? : ')

        return Department_VO(dpid, fname, 0, 0)

    @staticmethod
    def readEmp2():
        print('이엠피')

    @staticmethod
    def readDept2():
        print('디프')