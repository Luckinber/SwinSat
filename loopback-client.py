from lan import init_LAN
import socket

def client_loop():
	s = socket.socket()
	s.connect(('192.168.4.39', 5000))
    
	print("Loopback client Connect!")
	while True:
		data = s.recv(2048)
		if data.decode('utf-8') == 'stop':
			break
		print(data.decode('utf-8'))
		if data != 'NULL':
			s.send(data)

def main():
	init_LAN()
	client_loop()

if __name__ == "__main__":
	main()