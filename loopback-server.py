from lan import init_LAN
import socket

def server_loop(ip): 
	s = socket.socket()
	s.bind((ip, 5000))
	s.listen(5)

	print("Loopback server Open!")
	conn, addr = s.accept()
	print("Connect to:", addr) 
	while True:
		data = conn.recv(2048)
		if data.decode('utf-8') == 'stop':
			break
		print(data.decode('utf-8'))
		if data != 'NULL':
			conn.send(data)

def main():
	server_loop(init_LAN())

if __name__ == "__main__":
	main()