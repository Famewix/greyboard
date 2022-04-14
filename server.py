import socket



class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("\n[+] Waiting for Connection.")
        self.conn, addr =  listener.accept()
        print(f"\n[+] Got a Connection - {addr}")

    def run(self):
        while True:
            key = input("KEY>> ").encode()
            self.conn.send(key)
            message = self.conn.recv(3048).decode()
            print(message)



listener = Listener(socket.gethostbyname(socket.gethostname()), 6969)
listener.run()