import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket
import writeMySQL
import threading
import time

sensor_value = [0,0,0,0,0,0]
sockBroad = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockBroad.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

class UdpServer(object):

	#def udpServer(self):
	def udpServer(self,arr):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(('',25122))	#bind the same domain all machine

		timer = threading.Timer(3, self.SendBroadCast)
		timer.start()

		while True:
			recvData, (remoteHost, remotePort) = sock.recvfrom(1024)
			print("[%s:%s] connect" % (remoteHost, remotePort)) #receive the client's ip and port

			#sendDataLen = sock.sendto(str(arr),(remoteHost, remotePort))

			print "recvData:%d",recvData
			#print "sendDataLen: ",sendDataLen
			self.MBICommandProcess(recvData)


		sock.close()
	def MBICommandProcess(self,arr):
		#for i in arr:
		#	print (hex(ord(i)))
		try:
			CmdCode = ord(arr[37])
			if CmdCode == 22:
				global sensor_value
				TempValue = ord(arr[229])<<8 | ord(arr[230])
				HumValue = ord(arr[231])<<8 | ord(arr[232])
				#PM1Value = ord(arr[])<<8 | ord(arr[])
				PM1Value = 1.0
				PM25Value = ord(arr[235])<<8 | ord(arr[236])
				#PM10Value = ord(arr[])<<8 | ord(arr[])
				PM10Value = 10.0
				#SmokeValue = ord(arr[237])<<8 | ord(arr[238])
				Co2Value = ord(arr[239])<<8 | ord(arr[240])

				sensor_value[0] = TempValue
				sensor_value[1] = HumValue
				sensor_value[2] = Co2Value
				sensor_value[3] = PM1Value
				sensor_value[4] = PM25Value
				sensor_value[5] = PM10Value

				writemysql = writeMySQL.writeMySQL()
				writemysql.WriteLocalDB(sensor_value)

				try:
					writemysql.WriteMySQL(sensor_value)
				except:
					print"Check internet connection!"

				print "Into Cmd16 procedure"
				#print ("%d" % TempValue)
			else:
				print "%d",arr
				#print (hex(ord(arr[37])))
		except:
			print "Packacket length not enough"

	def SendBroadCast(self):
		global sockBroad
		while True:
			Cmd15 = bytearray([0x4D,0x42,0x49,0x2D,0x4E,0x65,0x74,0x01,
        			0x8F,0x1C,0x00,0x00,0x00,0x30,0xAB,0x4C,
			        0x01,0x00,0x00,0x00,0x0D,0x00,0x00,0x00,
			        0x00,0x00,0x00,0x00,0x0E,0x00,0x00,0x00,
			        0x00,0x00,0x00,0x00,0x00,0x15,0x00,0x00,
			        0x00,0x0C,0x00,0xBB,0x00,0x00,0x00,0x9A])
			#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			#sock.sendto(str(Cmd15),('<broadcast>',25122))
			#sock.close()
			sockBroad.sendto(str(Cmd15),('<broadcast>',25122))
			time.sleep(3)

if __name__ == "__main__":
	udpServer = UDPServer()
	udpServer.udpServer()
