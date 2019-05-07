import socket

#Run me on a separate computer to simulate dongle
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

while True:
    try:
        message, address = server_socket.recvfrom(1024)
        message = "[12, 12, 3, 4]"

        server_socket.sendto(message, address)
    except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)
