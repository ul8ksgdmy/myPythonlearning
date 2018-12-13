from py1811.sungJuk import SungjukService

sjsrv = SungjukService.SungJukService()
std3 = sjsrv.readSungJuk()
print(std3)
sjsrv.computeSungJuk(std3)
print(std3)
