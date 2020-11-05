import pymysql
def getconn():
    db = pymysql.connect("localhost","root","root")
    return db
def addtab(tablename,db):
    cur=db.cursor()
    print("start to enter infomations.")
    id = input("enter id:")
    name = input("enter member's name:")
    sex = input("enter sex in Chinese (男 or 女)")
    boda = input("enter when is this member born(for example 2016.11.5):")
    others = input("enter others:")
    val = (id,name,sex,boda,others)
    sql1="insert into `"+tabname+"` values"+str(val)
