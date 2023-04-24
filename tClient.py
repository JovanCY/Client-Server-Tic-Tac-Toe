import socket
from ttt import *


# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
serverip = 'localhost'
serverport = 3011
s.connect((serverip, serverport))
print("Connected to: ", serverip,  "on port: ", serverport)

loop = 1
print("type /q to quit")
# print("Enter message to send...")

game = Board()
game.printBoard()
while loop == 1:   
    #send
    gameLoop = False
    while gameLoop is False:
        sendData = input(">")
        gameLoop = game.add(1,sendData)
    s.sendall(sendData.encode())
    if '/q' in sendData:
        loop = 0
        break
    game.printBoard()
    if game.checkWinner():
        loop = 0
        break

    #receive
    print("waiting for reply...")
    receiveData = s.recv(2048)
    print(receiveData.decode())
    game.add(2,receiveData.decode())
    if "/q" in receiveData.decode():
        loop = 0
        break
    game.printBoard()
    if game.checkWinner():
        loop = 0
        break

s.close()
