import machine, os

sd = machine.SDCard()
fs = os.VfsFat(sd)
os.mount(fs, "/sd")
os.listdir('/sd')
os.umount('/sd')