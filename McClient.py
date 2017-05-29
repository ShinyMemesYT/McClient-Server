import socket
import time

host = '127.0.0.1'
port = 0
order_id = 1

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quitting = False
while not quitting:
    print('\nORDER ID: {}\nSend anything to start a new order.'.format(order_id))
    msg = input('--> ')
    msg = str(order_id)
    s.sendto(msg.encode(), server)
    data, addr = s.recvfrom(1024)
    print('\nOrder with ID: {} is ready!'.format(order_id))
    order_id += 1

    
