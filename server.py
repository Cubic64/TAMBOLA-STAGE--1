import socket
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000

def setup():
    print("\n\t\t\t\t\t*** Welcome To Tombola Game ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind({IP_ADDRESS,PORT})

    SERVER.listen(10)

    print("\t\t\tSERVER IS WAITING FOR CONNECTIONS....\n")

def acceptConnections():
    global CLIENT
    global SERVER
    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENT.keys()) == 0):
            CLIENT[player_name] = {'player_type' : 'player1'}
        else:
            CLIENT[player_name] = {'player_type' : 'player2'}
        
        CLIENT[player_name]["player_socket"] = player_socket
        CLIENT[player_name]["address"] = addr
        CLIENT[player_name]["player_name"] = player_name
        CLIENT[player_name]["turn"] = False
        
        print(f"Connection established with {player_name} : {addr}")