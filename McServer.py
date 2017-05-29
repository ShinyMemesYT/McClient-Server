import socket

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

clients = []

quitting = False
print("Server Started.")
while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        print('\nNEW ORDER\nORDER_ID: {}\nReply with anything to confirm the order is ready.'.format(data.decode()))
        reply = input('--> ')
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            s.sendto(reply.encode(), client)
    except:
        pass

s.close()
quit()
