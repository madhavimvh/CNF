import socket
import threading
import os
import signal
def receive(s, username):
    while True:
        data = s.recv(1024).decode()
        if not data:
            continue
        print (str(data))

def main():
    host = '10.10.9.59'
    port = 2028
    s = socket.socket()
    s.connect((host, port))
    msg = s.recv(1024).decode()
    print(msg)
    print(s.recv(1028).decode())
    username = input()
    s.send(username.encode())
    threading.Thread(target = receive, args = (s, username)).start()
    message = ''
    while (message !=  username + ': q'):
        message = username + ': ' + input()
        s.send(message.encode())
        message = username + ': ' + input()
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
    s.close()
if __name__ == "__main__":
    main()