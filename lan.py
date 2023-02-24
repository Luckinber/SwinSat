import network
import time

def init_LAN():
	nic = network.LAN(0)
	nic.active(True)
	while not nic.isconnected():
		print("Connection failed...\nRetrying...")
		time.sleep(1)
	time.sleep(2)
	print(nic.ifconfig())
	return nic.ifconfig()[0]

def main():
	print(init_LAN())

if __name__ == "__main__":
	main()