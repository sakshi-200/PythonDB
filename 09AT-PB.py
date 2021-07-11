import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

author=input('Enter author name : ')
curs.execute("select * from books where author='%s'" %(author))
rec=curs.fetchone()

pb=input('Enter publication name : ')
curs.execute("select * from books where publication='%s'" %(pb))
rec=curs.fetchone()

print('List of books are :')

if rec :
       print(rec[1])
else :
    print('Books not found...')
con.close()

