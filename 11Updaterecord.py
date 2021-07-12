import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

bkcd=int(input('Enter bookcode : '))
curs.execute("select * from books where bookcode=%d" %bkcd)
rec=curs.fetchone()

rw=input("give your review : ")
curs.execute("Update books SET review='%s' "%(rw))
con.commit()

try:
   print('Review updated sucessfully...')
except :
   print('book not found')

con.close()