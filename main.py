import dbop
conn = dbop.getconn()
flag = input("enter action (1:quit,2:add,3:delete,4:modify")
if flag == 1:
    dbop.addtab("members",conn)
else :
    print("no this action : exiting")
    import sys
    sys.exit()
