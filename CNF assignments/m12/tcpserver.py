import socket
from _thread import *
import threading
import csv

filename = "data.csv"
rows = []

with open(filename, "rt") as csvfile:

    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
Roll_Numbers = []
Secret_Questions = []
Secret_Answers = []
for i in range(len(rows)):
    Roll_Numbers.append(rows[i][0])
    Secret_Questions.append(rows[i][1])
    Secret_Answers.append(rows[i][2])
    
print("Welcome to the attendance portal")

def threaded(c):

    while True:
        data = c.recv(2048)
        data = data.decode()
        if not data:
            break
        elif data in Roll_Numbers:
            indice = Roll_Numbers.index(data)
            c.send(str.encode("Roll Number found and please answer the Question."))
            data = Secret_Questions[indice]
            c.send(str.encode(data))
            data = c.recv(2048)
            data = data.decode()
            if data in Secret_Answers:
                c.send(str.encode("Attendance Success."))
                break
            else:
                c.send(str.encode("Attendance Failure."))
        else:
            c.send(str.encode("Roll Number not Found."))
    c.close()

def main():

    host = '127.0.0.1'
    port = 9000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))

    server.listen()

    while True:

        c, addr = server.accept()
        print("Connected to:" + str(addr))
        start_new_thread(threaded, (c, ))
    server.close()

if __name__ == '__main__':
    main()