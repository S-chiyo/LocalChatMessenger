import socket
import os

# add new path
import sys
sys.path.append('/home/chiyo/venv_python/lib/python3.11/site-packages')

# import faker
from faker import Faker
fake = Faker()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            data_str = data.decode('utf-8')
            print('Received ' + data_str)

            if data:
                # response = 'Server received the message: ' + data_str
                response = 'message from server!!\n' + fake.text()
                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print('Closing current connection')
        connection.close()