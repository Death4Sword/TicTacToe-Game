import socket
from _thread import *
from board import Board
import pickle
import time

from pygame import GL_ACCUM_RED_SIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ""
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("[START] Waiting for a connection")

connected = set()
games = {}
idCount= 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encore(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

        except:
            break
    print("Lost connection")
    try:
        print("Closing Game", gameId)
    except:    
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to :", addr)

    idCount += 1
    p = 0
    
    if idCount == 2:
        print("Creating a new game...")
    else:
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))