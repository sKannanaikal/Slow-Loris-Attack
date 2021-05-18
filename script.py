import sys
import socket

PORT = 8000

def create_connection(ip):
    print(ip)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((ip, PORT))
        s.listen()
        connection, address = s.accept()
        with connection:
            print(address)
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                connection.sendall(data)


def initiateAttack(ip):
    #TODO make the attack doggie
    create_connection(ip)

def main():
    ip = sys.argv[1]
    
    initiateAttack(ip)

if __name__ == "__main__":
    main()