import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

bcd=int(input('Enter bookcode :'))
curs.execute("select * from books where bookcode=%d" %(bcd))
rec=curs.fetchone()

rw=input('give your review : ')
curs.execute("Update review from books where review=%s" %rw)
con.commit()

try:
   print('Reviews updated successfully')

except:
    print('Invalid input...')


