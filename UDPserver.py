import socket as s
server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
hostname = s.gethostname()
port = 9999
address = (hostname, port)
server_socket.bind(address)
while True:
    print('The server is ready to listen')
    message, client = server_socket.recvfrom(2048)
    if message == b'-1':
        print('Server Closing...')
        server_socket.sendto(b'You commanded Server to close', client)
        break
    print('Message:',message,'\n','Type of message',type(message))
    print('Client:',client,'\n','Type of client',type(client))
    modifiedmsg = message.upper()
    server_socket.sendto(modifiedmsg, client)
server_socket.close()
