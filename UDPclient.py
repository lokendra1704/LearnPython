import socket as s
client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
serveraddress = (s.gethostname(), 9999)
msg = bytes(input('Enter message'),'utf-8')
client_socket.sendto(msg, serveraddress)
modifiedmsg, server_info = client_socket.recvfrom(2048)
print(modifiedmsg)
client_socket.close()
