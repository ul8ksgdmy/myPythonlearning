#파이썬으로 오라클 다루기
#파이썬용 오라클 라이브러리 cx_Oracle
#oracle instant client libarary

import cx_Oracle
conn = cx_Oracle.connect('my','123456', '13.125.178.188/xe')
conn.close()
