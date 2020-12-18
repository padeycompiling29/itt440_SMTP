import socket

#padeyfadhil10@mail.com

mailowner='padeyfadhil10@mail.com'
clientsock=socket.socket()
host='192.168.43.200'		#serveraddress
port=25				#serverport

print('Waiting for server acknowledgement!')
try:
		clientsock.connect((host,port))
except socket.error as e:
		print(str(e))

Response=clientsock.recv(1024)
print(Response)

while True:
#Sent message
#		message= input('Say something: ')
#		clientsock.send(message.encode('utf-8'))

#Receive message
#		response=clientsock.recv(2048)
#		print(response.decode('utf-8'))

#====================================================================#
#Mail input
#1)Send
		recipient=input('Recipient: ')
		clientsock.send(recipient.encode('utf-8'))

		mailtitle= input('Mail title: ')
		clientsock.send(mailtitle.encode('utf-8'))

		mailcontent= input('Mail message: ')
		clientsock.send(mailcontent.encode('utf-8'))

#2)Receive(From,to,title,message)

		sender=clientsock.recv(2048)
		senderR=sender.decode('utf-8')

		sendertitle=clientsock.recv(2048)
		titleR=sendertitle.decode('utf-8')

		sendermessage=clientsock.recv(2048)
		messageR=sendermessage.decode('utf-8')

		print('#From :'+ senderR)
		print('#To :'+ mailowner)
		print('#Mail title :'+titleR)
		print('#Mail message :'+messageR)

clientsock.close()
