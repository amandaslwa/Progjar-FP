import threading
import socket
from protocol import *

class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = socket.socket()
        self.socket_address = ('127.0.0.1', 60000)
        self.protocol = Protocol(self.socket)

    def run(self):
        print(f'Connecting to the server...')
        self.socket.connect(self.socket_address)
        print(f'Connected to the server.')

        while True:
            command = input('''Enter your command:\t
1. group create <group_name> // For creating new group\t
2. group join <group_name> // For joining group\t
3. group list // For get group list // For get group list\t
4. private <receiver_name> <message> // For joining private chat\t
5. register <name> <username> <password> // For register\t
6. signin <username> <password> // For sign in\n''')

            resp = self.protocol.proses(command)
            if resp:
                print(resp)

def main():
    clt = Client()
    clt.start()

if __name__ == '__main__':
    main()
