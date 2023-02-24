from machine import Pin
import time

led = Pin('LED', Pin.OUT)
sleep_time = 50

while True:
    time.sleep_ms(sleep_time)
    led.on()
    time.sleep_ms(sleep_time)
    led.off()