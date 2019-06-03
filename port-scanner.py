#Very basic and simple port scanner
import socket

total_ports = 1023 #You can change ports range here
host = socket.gethostbyname("twitter.com") #You can also check ports on your own device

for port in range(1, total_ports):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	check = sock.connect_ex((host, port))
	if check==0:
		print("Port "+format(port)+" is open")
sock.close()
