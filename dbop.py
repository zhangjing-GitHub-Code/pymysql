import pymysql
def getconn():
    db = pymysql.connect("localhost","root","root")
    return db
def addtab(tablename,db):
    cur=db.cursor()
    sql1="insert into `"+tabname+"` values"+str(val)
