import sys

def create_connection(ip):
    print(ip)


def initiateAttack(ip):
    #TODO make the attack doggie
    create_connection(ip)

def main():
    ip = sys.argv[1]
    initiateAttack(ip)

if __name__ == "__main__":
    main()