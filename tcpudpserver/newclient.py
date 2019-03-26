import socket
import sys

server = ('localhost', 12345)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(20)
socks = [sys.stdin, s]

try:
    s.connect(server)
except:
    print('Unable to connect')
    sys.exit()

print('Connected to the server')
while True:
    for sock in socks:                 # цикл поочередно
        if sock == s:                  # получает и отправляет
            try:                       # сообщения
                data = sock.recv(1024)
            except:
                print('No new msgs')
                continue
            print(data.decode('utf-8'))
        else:
            msg = input('Input: ')
            s.send(msg.encode('utf-8'))


