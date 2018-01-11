import datetime
import threading
import time

def foo1(string):
	next_call = time.time()
	while True:
		print datetime.datetime.now()
		next_call = next_call + 1
		time.sleep(next_call - time.time())
		print string


def foo2(list):
	next_call = time.time()
	while True:
		print datetime.datetime.now()
		next_call = next_call + 2
		time.sleep(next_call - time.time())
		for x in list:
			print x


def main():
	dPara = "Hello"
	timerThread1 = threading.Thread(target=foo1, args=[dPara])
	timerThread1.start()
	list = range(31)
	timerThread2 = threading.Thread(target=foo2, args=[list])
	timerThread2.start()


if __name__ == "__main__":
	main()
