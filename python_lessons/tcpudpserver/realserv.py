import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 12345))
s.listen(10)
s.settimeout(10)
socks = [s]
threaddict = {}
print('Start Server')


def sending(serv, client, msg):
    for sock in socks:
        if sock != serv and sock != client:
            try:
                sock.send(msg.encode('utf-8'))
            except:
                sock.close()
                if sock in socks:
                    print('remove2', sock)
                    socks.remove(sock)
                    threaddict.pop(sock)


def waiting(sock):
    sock.settimeout(3)
    while sock in socks:
        try:
            print('w8 msg from' + str(sock.getpeername()))
            data = sock.recv(1024)
            if data:
                sending(s, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data.decode('utf-8'))
                time.sleep(0.25)
            else:
                if sock in socks:
                    print('remove', socket)
                    socks.remove(sock)
                    threaddict.pop(sock)
        except:
            time.sleep(0.25)


def mainthread():
    while True:
        for socket in socks:                                # Ожидание новых пользователей
            if socket == s:
                print("w8 for new users")
                try:
                    sockclient, addr = s.accept()
                except:
                    continue
                print(addr, 'connected to the server')
                socks.append(sockclient)                    # "регистрация" новых пользователей
                sending(s, sockclient, str(addr) + ' ' + 'connected to the server\n')
                threaddict[sockclient] = threading.Thread(target=waiting, args=(sockclient,))
                threaddict[sockclient].start()              # запуск потока, который ожидает и пересылает
            else:                                           # полученные сообщения
                time.sleep(0.25)
                continue


chat = threading.Thread(target=mainthread())
chat.start()