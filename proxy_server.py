# Lab 2 
# Matthew Sheydwasser - 1641028
#
# Referenced the sample code given on eclass and the
# old lab video demonstrations

import socket
from multiprocessing import Process


HOST = ''
PORT = 8001
BUFFER = 4096

def get_ip(host):

    # get the IP address of the given host

    print(f'Getting IP of {host}')
    ip = socket.gethostbyname(host)

    return ip

def handle_proxy(addr, conn, proxy):

    send_data = conn.recv(BUFFER)
    print(f"Proxy server received {send_data} from {addr}. Sending . . .")
    proxy.sendall(send_data)

    proxy.shutdown(socket.SHUT_WR)

    end_data = proxy.recv(BUFFER)
    print(f'Sending recieved data to client at {addr}')
    conn.send(end_data)

def main():
    
    host = 'www.google.com'
    port = 80

    # acts as server to client
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:

        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        proxy_start.bind((HOST, PORT))

        proxy_start.listen(2)

        while True:
            conn, addr = proxy_start.accept()

            # Part 4: Print what is connected to server socket
            print(f"Connected to IP {addr[0]} on port {addr[1]}")

            # acts as client to real server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:

                ip = get_ip(host)

                # .connect only used on clients, shows how it is acting as client
                proxy_end.connect((ip, port))

                # start a Process daemon to handle multiple connections
                proc = Process(target=handle_proxy, args= (addr, conn, proxy_end))
                proc.daemon = True
                proc.start()

            conn.close()

if __name__ == '__main__':
    main()