import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()


bcd=int(input('Enter bookcode : '))
curs.execute("select bookcode,booknm,category,author,publication,edition,year,price from books where bookcode=%d" %bcd)
rec=curs.fetchone()

nwprc=int(input("Enter price : "))
curs.execute=("Update books set price=%d" %(nwprc))
con.commit()

try:
    print("bookcode : %d" %rec[0])
    print("bookname : %s" %rec[1])
    print("Category : %s" %rec[2])
    print("Author : %s" %rec[3])
    print("Publication : %s" %rec[4])
    print("Edition : %d" %rec[5])
    print("Year : %d" %rec[6])
    print("Price : %d" %rec[7]) 
    print('Book details found sucessfully...')
except :
    print('book not found')

con.close()