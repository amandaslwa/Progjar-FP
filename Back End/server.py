import threading
import socket

class Message():
    TYPE_GROUP = 1
    TYPE_PRIVATE = 1
    TYPE_JOIN_LEAVE = 1
    def __init__(self, message, client_name, message_type):
        self.client_name = client_name
        self.message = message
        self.message_type = message_type


class Group():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.members = []
        self.messages = []

    def broadcast(self, message, user_name, message_type):
        for member in self.members:
            member.send(message)
            new_message = Message(message, user_name, message_type)
            self.messages.append(new_message)
    
    def remove_member(self, client):
        for member in self.members:
            member.remove(client)


class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 32)
        self.socket_address = ('127.0.0.1', 60000)
        self.clients = []
        self.users = {}
        self.groups = []

    def run(self):
        self.socket.bind(self.socket_address)
        print(f'Socket is binding with address {self.socket_address}')
        self.socket.listen(1)
        print(f'Socket is listening...')

        while True:
            client, address = self.socket.accept()
            print(f'Connection incoming from {address}...')
            print('Waiting for request..')
            self.clients.append(client)

            t = threading.Thread(target=self.handle_receive, args=(client,))
            t.start()
            
    
    def create_group(self, group_name):
        length = len(self.groups)
        group = Group(length + 1, group_name)
        self.groups.append(group)

    def get_group_list(self):
        group_list = 'Group list: \n'
        list = '\n'.join([f'- {group.name}' for group in self.groups])
        group_list += list
        return group_list

    def join_group(self, group_name, client):
        for group in self.groups:
            if group.name == group_name:
                group.members.append(client)
                return 'found'
        
        return 'not found'

    def remove_from_grup(self, group_name, client):
        for group in self.groups:
            if group.name == group_name:
                group.members.remove(client)

    def register(self, name, username, password):
        self.users[username] = {'name': name, 'password': password, 'message': {}}

    def signin(self, username, password):
        if self.users[username]:
            user = self.users[username]
            return user['name'] if user['password'] == password else 'kosong' 
    
    def handle_receive(self, client):
        while True:
            try:
                data = client.recv(2048).decode()
                print(data)
                print(f'Request received: {data}')
                d = data.split(' ')

                if d[0] == 'group':
                    if d[1] == 'create':
                        group_name = d[2]

                        self.create_group(group_name)
                        client.send(f'Group with name of {group_name} has been created successfully'.encode())
                    elif d[1] == 'list':
                        group_list = self.get_group_list()
                        client.send(f'{group_list}'.encode())
                    elif d[1] == 'join':
                        group_name = d[2]
                        res = self.join_group(group_name, client)
                        client.send(f'{res}'.encode())
                    elif d[1] == 'broadcast':
                        group_name = d[2].strip()
                        name = d[3].split('<>')[0]

                        message = data.split('<>')[1]
                        to_send = ''
                        if name == 'join' or name == 'leave':
                            to_send = f'{message}'
                            if name == 'leave':
                                self.remove_from_grup(group_name, client)
                        else:
                            to_send = f'{name}: {message}'

                        for group in self.groups:
                            if group.name == group_name:
                                group.broadcast(to_send.encode(), name, Message.TYPE_GROUP)
                elif d[0] == 'register':
                    name = d[1]
                    username = d[2]
                    password = d[3]
                    self.register(name, username, password)
                    client.send(f'{username} account has been created successfully'.encode())
                elif d[0] == 'signin':
                    username = d[1]
                    password = d[2]
                    name = self.signin(username, password)
                    client.send(f'{name} has been logged in successfully'.encode())
                elif d[0] == 'private':
                    print('Test')
            except:
                break


def main():
    server = Server()
    server.start()

if __name__ == '__main__':
    main()




