import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

bcd=int(input('Enter bookcode :'))

curs.execute("select * from books where bookcode=%d" %bcd)
rec=curs.fetchone()


try:
    print("bookcode : %d" %rec[0])
    print("bookname : %s" %rec[1])
    print("Category : %s" %rec[2])
    print("Author : %s" %rec[3])
    print("Publication : %s" %rec[4])
    print("Edition : %d" %rec[5])
    print("Year : %d" %rec[6])
    print("Price : %d" %rec[7]) 

    curs.execute("delete from books where bookcode=%d" %bcd)
    bcd=input('Do you want to continue? (yes) ')
    while bcd.upper()=='YES':
     print('Book deleted successfully')
     con.commit()
except:
    print('Book does not exist')
