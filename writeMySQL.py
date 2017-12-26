import MySQLdb
import time
import datetime

class writeMySQL(object):

	def WriteMySQL(self,list):
		#connect to db
		db = MySQLdb.connect("52.199.2.57","mbiuser","mbi16948543","wifi_sensor_value")

		#setup cursor
		cursor = db.cursor()

		dbRow = self.getDBRowCount()+1

		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		#insert to table
		try:
			cursor.execute(
			"""INSERT INTO wifi_sensor_value.sensor_value VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
			(dbRow, st, list[0], list[1], list[2], list[3], list[4], list[5]))
			db.commit()

			#cursor.execute("""insert into wifi_sensor_value.sensor_value values(2,"2017-11-23",23,67,923,1.12,2.2,10.43)""")
			#db.commit()

		except:
			db.rollback()

		#show table
		#cursor.execute("SELECT * FROM wifi_sensor_value.sensor_value;")
		#print cursor.fetchall()

		db.close()

	def WriteLocalDB(self,list):
		dblocal = MySQLdb.connect("localhost","pi","raspberry","wifi_sensor_value")

		cursorlocal = dblocal.cursor()
		localdbRow = self.getLocalDBRowCount()+1

		print localdbRow," row count"
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		try:
                        cursorlocal.execute(
                        """INSERT INTO wifi_sensor_value.sensor_value VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (localdbRow, st, list[0], list[1], list[2], list[3], list[4], list[5]))
                        dblocal.commit()
		except:
                        dblocal.rollback()


                cursorlocal.execute("select * from wifi_sensor_value.sensor_value;")
                print cursorlocal.fetchall()

		dblocal.close()


	def getDBRowCount(self):
		db = MySQLdb.connect("52.199.2.57","mbiuser","mbi16948543","wifi_sensor_value")
		cursor = db.cursor()
		cursor.execute("select count(*) from wifi_sensor_value.sensor_value")
		db.commit()
		row = cursor.fetchone()
		db.close()
		return row[0]


	def getLocalDBRowCount(self):
		db = MySQLdb.connect("localhost","pi","raspberry","wifi_sensor_value")
		cursor = db.cursor()
		cursor.execute("select count(*) from wifi_sensor_value.sensor_value")
		db.commit()
		row = cursor.fetchone()
		db.close()
		return row[0]




