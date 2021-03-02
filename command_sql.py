from database import Database
code = input("Enter your SQL code:")
x = code.split()
if x[0] == "CREATE" and x[1] == "DATABASE":
    print("create_database")
    db_object = Database(x[2], load=False)
elif x[0] == "CREATE" and x[1] == "TABLE":
    name = input("Enter the name of db that you want to create the table")
    y = Database(name, load=True)
    tk = len(x[3])
    y.create_table(x[2], )
    print("create_table")
elif x[0] == "CREATE" and x[1] == "INDEX":
    nq = input("Enter the name of the database that you want to do the index")
    q = Database(nq, load=True)
    q.create_index(x[4], x[2])
elif x[0] == "DROP" and x[1] == "TABLE":
    '''print("drop_table")'''
    n = input("Enter the name of the database that you want to drop the table")
    ps = Database(n, load=True)
    ps.unlock_table(x[2])
    ps.drop_table(x[2])
elif x[0] == "INSERT" and x[1] == "INTO" and x[3] == "VALUES":
    named = input("Enter the name of the database that you want to insert into table")
    db = Database(named, load=True)
    db.unlock_table(x[2])
    x2 = x[2]
    x.pop(0)
    x.pop(1)
    x.pop(0)
    x.pop(0)
    db.insert(x2, x)
    db.show_table(x2)
    '''print("insert_into")'''
elif x[0] == "DELETE" and x[1] == "FROM" and x[3] == "WHERE":
    print(" 'the condition must be the type of 'column op value'")
    nam = input("Enter the name of the database that you want to delete from table")
    p = Database(nam, load=True)
    p.unlock_table(x[2])
    p.delete(x[2], x[4])
    '''print("delete_from")'''
elif x[0] == "UPDATE":
    na = input("Enter the name of the database that you want to update from table")
    st = Database(na, load=True)
    st.update(x[1], x[5], x[3], x[7])
    st.show_table(x[1])

elif x[0] == "SELECT" and x[4] == "WHERE":
    tr = input("Enter the name of the database that you want to select from table")
    km = Database(tr, load=True)
    km.unlock_table(x[3])
    if x[1] == '*':
        km.select(x[3], x[1], x[5])
    else:
        lix3 = x[3]
        lix5 = x[5]
        x.pop(0)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        x.pop(1)
        '''print(lix2)'''
        km.select(lix3, x, lix5)
elif x[0] == "SELECT" and x[5] == "JOIN":
    cv = input("Enter the name of the database that you want to select from table")
    xc = Database(cv, load=True)
    xc.inner_join(x[3], x[6], x[8])
else:
    print("wrong input,the sql code must be CAPITAL ")
