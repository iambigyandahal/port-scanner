#Very basic and simple port scanner
import socket, sys

open_ports = []

def print_open_ports():
	for i in open_ports:
	    print("Port {} is open".format(i), end="")
	    print(f"{' ': <5} ")

try:
	start = int(sys.argv[1])
	total_ports = int(sys.argv[2]) #You can change ports range here
	decending = int(sys.argv[4])
	host = str(sys.argv[3])
	timeout = float(sys.argv[6])
	host = socket.gethostbyname(host) #You can also check ports on your own device

	if decending == 0:
	    step = -1
	else:
	    step = 1

	for port in range(start, total_ports, step):
	    if int(sys.argv[5]) == 0:
	        print("Scanning port {}".format(port), end="\r")
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    sock.settimeout(timeout)
	    check = sock.connect_ex((host, port))
	    if check==0:
	        open_ports.append(port)
	    sock.close()

	print_open_ports()

except KeyboardInterrupt:
	print("\nExiting!")
	print_open_ports()
	sys.exit(0)
except socket.gaierror:
	print("\nHostname could not be resolved!") 
	sys.exit(0)
except socket.error:
	print("\nServer fault!")
	sys.exit(0)
except:
	print("\nCommand: python3 port-scanner.py <port-start> <port-end> <host> <decending> <verbose> <timeout>")
	print("\ndecending: 0 for true, 1 for false")
	print("\nverbose: 0 for true, 1 for false")
	print("\ntimeout in seconds")
	sys.exit(0)

sys.exit(0)