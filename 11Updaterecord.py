import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()
try: 
    bcd=int(input("Enter bookcode :"))
    rw=input('Give your review : ')  
    curs.execute("Update books set review='%s'where bookcode=%d" %(rw,bcd))
    print("Update bookreview : ",rw)
    con.commit()
    
except:
    print('Book Not Found...')

con.close()
