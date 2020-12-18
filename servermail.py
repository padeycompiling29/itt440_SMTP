import socket
import os
from _thread import *

Serversock=socket.socket()
host=''
port=25
ThreadCount=0

try:
		Serversock.bind((host,port))
except socket.error as e:
		print(str(e))

print('Waiting for a Client!')
Serversock.listen(5)

client1='padeyfadhil10@mail.com'
client2='abc'
def threaded_client(connection):
	connection.send(str.encode('Welcome to Padey Protocol-server \n'))
	while True:
#		data=connection.recv(2048)
#		reply= 'Server Says: '+data.decode('utf-8')
		username=connection.recv(2048)
		usernameread=username.decode('utf-8')
		mailtitle=connection.recv(2048)
		titleread=mailtitle.decode('utf-8')
		message=connection.recv(2048)
		messager=message.decode('utf-8')

#start func like database
		if usernameread == client1:
			address='192.168.43.94'
			transfersock.socket.socket()

			try:
				transfersock.connect((address,port))
			except socket.error as e:
				print(str(e))


			#sent data to receipent
			transfersock.send(usernameread.encode('utf-8'))
			transfersock.send(mailtitle.encode('utf-8'))
			transfersock.send(message.encode('utf-8'))

		elif usernameread == client2:
			print(usernameread)
			print(titleread)
			print(messager)

			transfersock=socket.socket()
			try:
				transfersock.bind(('192.168.43.121',25))
			except socket.error as e:
				print(str(e)+'--inner')

			transfersock.listen(5)

#			try:
#				Serversock.bind(('192.168.43.121',port))
#			except socket.error as e:
#				print(str(e)+'--INNER')

#			Serversock.listen(5)

			while True:
				take=transfersock.accept()
				take.send(usernameread.encode('utf-8'))
				take.send(titleread.encode('utf-8'))
				take.send(messager.encode('utf-8'))
			take.close()

		if not username:	#beware here
			break

	connection.close()

while True:
	Client,address=Serversock.accept()
	print('Connected to: '+address[0]+':'+str(address[1]))
	start_new_thread(threaded_client,(Client, ))
	ThreadCount+=1
	print('Thread Number:'+str(ThreadCount))
Serversock.close()

