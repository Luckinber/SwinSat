from machine import UART

uart1 = UART(1, baudrate=115200)
uart1.write('hello')  # write 5 bytes
uart1.read(5)         # read up to 5 bytes