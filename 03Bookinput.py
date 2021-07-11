import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()
try :

    bcd=int(input('Enter bookcode :'))
    bknm=input('Enter book name : ')
    ctg=input('Enter book category : ')
    author=input('Enter author name : ')
    pb=input('Enter book publication name : ')
    ed=int(input('Enter book edition : '))
    yr=int(input('Enter year : '))
    prc=int(input('Enter price : '))
    
    curs.execute("insert into books values(%d,'%s','%s','%s','%s',%d,%d,%d)"%(bcd,bknm,ctg,author,pb,ed,prc,yr))
    print('data enter sucessfully.....')
    con.commit()
except :
     print('data not enter....')

            
con.close()
