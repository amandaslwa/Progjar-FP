import threading

class Protocol():
    def __init__(self, socket):
        self.group_listener_condition = threading.Event()
        self.socket = socket
        self.logged_user = ''

    def proses(self, req: str):
        data = req.split(' ')
        type = data[0].strip()
        resp = ''
        
        if type == 'group':
            cmd = data[1].strip()
            if cmd == 'create':
                group_name = data[2].strip()
                resp = self.handle_create_group(group_name)
            elif cmd == 'list':
                resp = self.handle_get_group_list()
            elif cmd == 'join':
                group_name = data[2].strip()
                resp = self.handle_join_group(group_name)
        if type == 'private':
            receiver_name = data[1].strip()
            message = data[2].strip()
            resp = self.handle_private_chat(receiver_name, message)
        if type == 'register':
            name = data[1]
            username = data[2]
            password = data[3]
            resp = self.handle_register(name, username, password)
        if type == 'signin':
            username = data[1]
            password = data[2]
            resp = self.handle_signin(username, password)

            if resp == 'kosong':
                return 'User not found'
            
            self.logged_user = resp

        return resp 

    def handle_create_group(self, group_name: str):
        self.socket.send(f'group create {group_name}'.encode())
        data = self.socket.recv(1024)
        d = data.decode()
        return d

    def handle_get_group_list(self):
        self.socket.send('group list'.encode())
        data = self.socket.recv(1024)
        d = data.decode()
        return d

    def handle_register(self, name, username, password):
        self.socket.send(f'register {name} {username} {password}'.encode())
        data = self.socket.recv(1024)
        d = data.decode()
        return d

    def handle_signin(self, username, password):
        self.socket.send(f'signin {username} {password}'.encode())
        data = self.socket.recv(1024)
        d = data.decode()
        name = d.split(' ')[0]

        if name == 'kosong':
            return 'kosong'
        
        return d

    def handle_private_chat(self, receiver_name, message, name='Fayyadh'):
        self.socket.send(f'private {receiver_name}<>{message}'.encode())
        data = self.socket.recv(1024)
        d = data.decode()
        
        return d



    def handle_join_group(self, group_name):
        self.socket.send(f'group join {group_name}'.encode())
        response = self.socket.recv(1024).decode()

        if response == 'not found':
            return 'Group not found'
        
        t = threading.Thread(target=self.listen_group_messages)
        t.daemon = True
        t.start()
        
        print(f'Welcome to {group_name} group chat!')
        print('Enter q to quit')
        
        while True:
            try:
                message = input()
                if message.lower() == 'q':
                    stop_message = f'group broadcast {group_name} leave<>{self.logged_user} has leave the group'
                    self.socket.send(stop_message.encode())
                    break
                self.socket.send(f'group broadcast {group_name} {self.logged_user}<>{message}'.encode())
            except:
                break

        self.group_listener_condition.set()
        return 'You has leave the group'

    def listen_group_messages(self):
        while not self.group_listener_condition.is_set():
            message = self.socket.recv(1024).decode()
            print(message)
            