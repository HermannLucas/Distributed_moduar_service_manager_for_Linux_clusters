import socket
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        self.server.clients[data] = self.client_address
        response = bytes(self.server.name, 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    clients ={}
    
    def send(self, client, order):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((client))
            sock.sendall(order)

class Client:
    def __init__(self, mod_man):
        self.mod_man = mod_man
    
    def connect(self, ip, port, name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(bytes(name, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Connected to : {}".format(response))
            return sock.getsockname()

    def listen(self, ip, port):
        with socketserver.TCPServer((ip, port),  Client_TCP_handler) as server:
            print(self)
            server.client = self
            server.serve_forever()
    
class Client_TCP_handler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = self.request.recv(1024)
        print(self.server)
        print("Got contacted from {}.".format(self.client_address[0]))
        self.server.client.mod_man.execute_order(data)
