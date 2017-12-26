import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class UdpClient(object):
	def udpClient(self):
		clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		sendDataLen = clientSock.sendto("this is send data from client",('localhost',25122))
		#array = []
		#for i in arr:
		#	array.append(i)
		#	print i
		#sendDataLen = clientSock.sendto("array",('localhost',25122))
		recvData = clientSock.recvfrom(1024)
		print 'sendDataLen: ', sendDataLen
		print 'recvData: ', recvData
		
		clientSock.close()

if __name__ == "__main__":
	udpClient = UdpClient()
	udpClient.udpClient()
