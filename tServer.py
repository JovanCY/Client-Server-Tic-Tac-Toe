from multiprocessing.connection import wait
import socket
import sys
from ttt import *


def main():

    # framework inspired by https://www.binarytides.com/python-socket-programming-tutorial/ by Silver Moon, Created on July 28 2020
    # and adapted for the purposes of the assignment by me, Jovan Clement Young

    HOST = 'localhost'  # Symbolic name meaning all available interfaces
    PORT = 3011  # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' +
              str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print('Socket bind complete')

    s.listen(10)
    print('Socket now listening on: ', HOST, ' on port: ', PORT)

    # wait to accept a connection - blocking call
    conn, addr = s.accept()

    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    game = Board()
    loop = 1
    game.printBoard()
    while loop == 1:
        # receive
        print("waiting for reply...")
        receiveData = conn.recv(2048)
        print(receiveData.decode())
        game.add(1, receiveData.decode())
        if "/q" in receiveData.decode():
            loop = 0
            break
        game.printBoard()
        if game.checkWinner():
            loop = 0
            break

        #send
        gameLoop = False
        while gameLoop is False:
            sendData = input(">")
            gameLoop = game.add(2,sendData)
        conn.sendall(sendData.encode())
        if '/q' in sendData:
            loop = 0
            break
        game.printBoard()
        if game.checkWinner():
            loop = 0
            break

    conn.close()
    s.close()


if __name__ == "__main__":
    main()
