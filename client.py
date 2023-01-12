# Lab 2 
# Matthew Sheydwasser - 1641028
#
# Referenced the sample code given on eclass and 
# this site to create socket and connect to www.google.com:
# https://pythonprogramminglanguage.com/socket-client/


import socket

def create_socket():

    # initializes the socket

    print('Creating socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return sock

def get_ip(host):

    # get the IP address of the given host

    print(f'Getting IP of {host}')
    ip = socket.gethostbyname(host)

    return ip

def send_data(sock, req):

    # send a GET request for the specified host to the server

    print('Sending GET request')
    sock.sendall(req.encode())
    
def receive_data(sock, buffer):

    # prints the data retrieved from the server

    full_data = b''
    print("Recieved data:")

    # continues to retrieve data until none left
    while True:
        data = sock.recv(buffer)

        if not data:
            break

        full_data += data

    print(full_data) 

def connect_to_server(sock, host, port):

    # gets the IP of the host, connects on port 80

    ip = get_ip(host)

    sock.connect((ip, port))
    print(f'Socket connected to {host}')

def main():

    host = 'www.google.com'
    req = "GET / HTTP/1.0\r\n\r\n"
    port = 80
    buffer = 4096

    # create socket, and connect to server
    sock = create_socket()
    connect_to_server(sock, host, port)

    # send data to server  
    send_data(sock, req)
    sock.shutdown(socket.SHUT_WR) # stops further sending of requests

    # receive and print data
    receive_data(sock, buffer) 

    # close once done
    sock.close()

if __name__ == '__main__':
    main()