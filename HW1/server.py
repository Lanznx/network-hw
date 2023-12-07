# 呂安 109305092 資管二

import socket
import threading

def handle_client(client_socket, client_address):
    request = client_socket.recv(1024).decode('utf-8')
    path = request.split(' ')[1]

    if path == '/good.html':
        response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><head><link href="style.css" rel="stylesheet" type="text/css"></head><body>My student ID: 109305092</body></html>'
    elif path == '/style.css':
        response = 'HTTP/1.1 200 OK\nContent-Type: text/css\n\nBody {color: red;}'
    elif path == '/redirect.html':
        response = 'HTTP/1.1 301 Moved Permanently\nLocation: /good.html\n\n'
    elif path == '/notfound.html':
        response = 'HTTP/1.1 404 Not Found\n\n'
    else:
        response = 'HTTP/1.1 404 Not Found\n\n'

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
