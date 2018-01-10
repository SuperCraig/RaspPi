#import a database connection
import MySQLdb
import sys

#open a database connection
#be sure to change the host IP address, username, password and database name
# to match your own
connection = MySQLdb.connect("" , "" , "" , "street_light_para" )

#prepare a cursor object using cursor() method
cursor = connection.cursor()

#execute the SQL query using execute() method
cursor.execute("select * from street_light_para.light_config")

#fetch all of the rows from the query
data = cursor.fetchall()

#print the rows
for row in data:
	print row[0], row[1], row[2], row[3]

#close the cursor object
cursor.close()

#close the connection
cursor.close()

#exit the program
sys.exit()

