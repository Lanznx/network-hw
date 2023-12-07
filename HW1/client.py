import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pars = ('127.0.0.1', 8888) # server IP and server port
s.connect(pars)

while True:
    
    # let the client talk firt
    s.send(b'request')
    
    # then wait for server response
    data = s.recv(1024)
    if data:
        print("data from server:", data)

    # terminate
    s.send(b'close')
    break
    
# close directly
s.close()