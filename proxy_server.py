
import socket
import time

def main():
    
    host = 'www.google.com'
    port = 8001
    buffer = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))

        s.listen(2)

        while True:
            conn, addr = s.accept()

            # Part 4: Print what is connected to server socket
            print(f"Connected to IP {addr[0]} on port {addr[1]}")

            data = conn.recv(buffer)
            print(f"Data received by server: {data}")

            time.sleep(0.5)
            conn.sendall(data)
            conn.close()

if __name__ == '__main__':
    main()