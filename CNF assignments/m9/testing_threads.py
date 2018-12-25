import socket
import threading
import random
from _thread import *
def clientthread(conn, addr):
    welcome_note = '$ welcome to Guess game $ guess a number between 1 and 50'
    high = 'guess is greater than value!'
    low = 'guess is lesser than value!'
    conn.send(welcome_note.encode())
    x = random.randint(1, 51)
    data = conn.recv(1024)
    print('user -->' + str(addr) + ' : ' + str(data.decode()))
    conn.send('')
    while True:
        answer = conn.recv(1024)
        print('Guess :  ' + answer.decode())
        if (int(answer.decode()) > x):
            conn.send(high.encode())
        elif (int(answer.decode()) < x):
            conn.send(low.encode())
        else:
            conn.send('guess is correct'.encode())
    conn.close()


host = '10.10.9.59'
port  = 8011
s = socket.socket()
s.bind((host, port))
s.listen(5)
print('socket is ready')
while True:
    conn, addr = s.accept()
    print('connected from  ' + str(addr))
    start_new_thread(clientthread, (conn, addr))
s.close()
