import socket

#121advisor@mail.com

mailowner='121advisor@mail.com'
clientsock=socket.socket()
serversmtp='192.168.43.200'
port=25

print('CONNECTING TO SMTP SERVER')
try:
		clientsock.connect((serversmtp,port))
except socket.error as e:
		print(str(e))

Response=clientsock.recv(1024)
responseread=Response.decode('utf-8')
print('########'+ responseread +'#########')



#receive
receive=socket.socket()
try:
	receive.connect((serversmtp,port))
except socket.error as e:
	print(str(e)+'--INNER')

while True:
	sendername=receive.recv(2048)
	sendertitle=receive.recv(2048)
	sendermessage=receive.recv(2048)

	print('#From : '+ sendername.decode('utf-8'))
	print('#To :'+ mailowner)
	print('#Mail Title :'+sendertitle.decode('utf-8'))
	print('#Mail message : '+sendermessage.decode('utf-8'))

clientsock.close()
