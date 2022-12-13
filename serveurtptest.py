
"""while msgclient != 'kill':
#ouverture socket

while msgclient != 'kill' and msgclient != 'reset' :
#accept

while msgclient != "disconnect" and msgclient != "kill" and msgclient != "rest":
#reception
if msgclient !=  "disconnect":
#envoi
else: #envoi de disconnect

fermeture client

fermeture serveur"""

import socket
import threading

msgclient =''
message =""
while message != "deco-server":

    host = "0.0.0.0" # "", "127.0.0.1
    port = 10000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    while message != 'deco-server' :

        print('En attente du client')
        conn, address = server_socket.accept()
        print(f'Client connecté {address}')

        while message != "deco-server" :

            # Réception du message du client
            msgclient = conn.recv(1024) # message en by
            message = msgclient.decode()
            print(f"Message du client : {message}")

            reply = "ok "
            conn.send(reply.encode())
            print(f"Message {reply} envoyé")

            #else:

            #reply = "disconect"
            #conn.send(reply.encode())


        # Fermeture
        conn.close()
        print("Fermeture de la socket client")
        if message == "disconnect":
            message = ""
    server_socket.close()
    print("Fermeture de la socket serveur")
    if message == "reset":
        print("rebooting")
        message = ""
