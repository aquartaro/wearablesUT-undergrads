import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

while True:
    message, address = server_socket.recvfrom(1024)
    message = "\x00\x00\x00\x00,ffff\x00\x00\x00\xc3\n\x92\x99A \xd8zA~\x9c\xc6AgU\xd3"

    server_socket.sendto(message, address)