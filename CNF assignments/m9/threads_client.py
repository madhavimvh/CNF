import socket
def main():
	host = '10.10.9.47'
	port  = 1244
	s = socket.socket()
	s.connect((host, port))
	message = input('user-->')
	while message != 'x':
		s.send(message.encode())
		data = s.recv(1024)
		print('received from server ' + str(data.decode()))
		message = input('user-->')
	s.close()
if __name__ == '__main__':
	main()