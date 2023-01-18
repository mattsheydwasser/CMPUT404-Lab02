# Lab 2 
# Matthew Sheydwasser - 1641028
#
# Referenced the sample code given on eclass and 
# this site to create server socket to listen to connections
# https://stackoverflow.com/questions/54408940/how-to-write-a-python-echo-server-that-doesnt-disconnect-after-first-echo
# Answer written by user "Please don't judge me", https://stackoverflow.com/users/9003282/please-dont-judge-me



import socket
import time

def main():
    
    host = '127.0.0.1'
    port = 8001
    buffer = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))

        s.listen(2)

        while True:
            conn, addr = s.accept()

            # Part 4: Print what is connected to server socket
            print(f"Connected to '{addr}'")

            data = conn.recv(buffer)
            time.sleep(0.5)
            conn.sendall(data)
            conn.close()

if __name__ == '__main__':
    main()