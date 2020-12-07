#Protected

import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = msg.decode('ascii')[5:]
                    broadcast(f'{name_to_kick} was kicked by an admin'.encode('ascii'))
                    kick_user(name_to_kick)
                    print(f'{name_to_kick} was kicked')
                else:
                    client.send('Command was refused'.encode('ascii'))
            elif msg.decode('ascii').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_ban = msg.decode('ascii')[4:]
                    broadcast(f'{name_to_ban} was banned by an admin'.encode('ascii'))
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}\n')
                    print(f'{name_to_ban} was banned')
                else:
                    client.send('Command was refused'.encode('ascii'))
            else:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat'.encode('ascii'))
                print(f'{nickname} left the server')
                nicknames.remove(nickname)
                break

def receive():
    while True:
        client, address = server.accept()
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if nickname+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        ## Admin
        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            if password != 'sherwin':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)
        print(f'{str(address)} {nickname} is Connected')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.close()
        nicknames.remove(name)

print("Server is listening...")
receive()

#End
