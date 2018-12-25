import socket

def main():

	host = '127.0.0.1'
	port = 9000

	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.connect((host, port))

	# message = input("Type in the roll number with MARK ATTENDANCE: ")

	while True:
		message = input("Type in the roll number with MARK ATTENDANCE: ")
		c.send(str.encode(message))
		data = c.recv(1024)
		if data != str.encode("Roll Number not Found."):
			print(data.decode())
			data = c.recv(1024)
			print(data.decode())
			message1 = input()
			# data = c.recv(1024)

			c.send(str.encode(message1))
			data = c.recv(1024)
			print("Recieved from Server: " + data.decode())
			break
		else:
			# print("Reached")
			print(data)
			break
	c.close()

if __name__ == '__main__':
	main()