import socket

#get hostname
hostname = socket.gethostname()
#get ip adress
ip = socket.gethostbyname(hostname)
#print ip adress
print(f"Your ip adress:{ip}")
