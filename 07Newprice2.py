import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='APPLE',database='bookstoredb')
curs=con.cursor()

   
curs.execute("update books set price=300 where bookcode=1002")
print('Bookdata updated successfully')
con.close()

con.close()

