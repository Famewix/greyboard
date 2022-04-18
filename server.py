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
        self.help_message = """
    *a -> presses a key
    *abcd -> presses abcd keys
    *alt+tab -> presses following shortcut
    *abc/shortcut{{*2}}*cba/shortcut -> presses abc and waits for 2 seconds and presses cba

    * -- means changable with same kind of key
"""

    def run(self):
        while True:
            key = input("KEY>> ")
            if key == "help":
                print(self.help_message)
            else:
                self.conn.send(key.encode())
                message = self.conn.recv(3048).decode()
                print(message)



listener = Listener(socket.gethostbyname(socket.gethostname()), 6969)
listener.run()