from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import binascii

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr
    def setHandle(self,ch1, ch2):
	self.handle1 = ch1.getHandle() + 1
	self.handle2 = ch2.getHandle() + 1
    def handleNotification(self, cHandle, data):
        print "call back"
	if(cHandle == self.handle1 or cHandle == self.handle2):
	    print "printing data"
            print (data,"123")

deleg = ScanDelegate()
##scanner = Scanner().withDelegate(deleg)
##devices = scanner.scan(10.0)
'''
n=0
for dev in devices:
    print "%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print " %s = %s" % (desc, value)
number = input('Enter your device number: ')
print('Device', number)
print(devices[number].addr)
'''
print "Connecting..."
dev = Peripheral('f0:f8:f2:d2:bc:70', 'public')
dev.setDelegate(deleg)

'''
print "Services..."
for svc in dev.services:
    print str(svc)
'''
LED_SERVICE = "f0001110-0451-4000-B000-000000000000"
LED1 = "f0001111-0451-4000-B000-000000000000"
LED2 = "f0001112-0451-4000-B000-000000000000"
BUT_SERVICE = "f0001120-0451-4000-B000-000000000000"
BUT1 = "f0001121-0451-4000-B000-000000000000"
BUT2 = "f0001122-0451-4000-B000-000000000000"

srv_l = dev.getServiceByUUID(LED_SERVICE)
srv_b = dev.getServiceByUUID(BUT_SERVICE)

'''
ch_led1 = dev.getCharacteristics(uuid=UUID(LED1))[0]
ch_led2 = dev.getCharacteristics(uuid=UUID(LED2))[0]
ch_but1 = dev.getCharacteristics(uuid=UUID(BUT1))[0]
ch_but2 = dev.getCharacteristics(uuid=UUID(BUT2))[0]
'''
ch_led1 = srv_l.getCharacteristics(LED1)[0]
ch_led2 = srv_l.getCharacteristics(LED2)[0]
ch_but1 = srv_b.getCharacteristics(BUT1)[0]
ch_but2 = srv_b.getCharacteristics(BUT2)[0]

deleg.setHandle(ch_but1, ch_but2)
dev.writeCharacteristic(deleg.handle1, '\x01\x00')
print deleg.handle1
dev.writeCharacteristic(deleg.handle2, '\x01\x00')
print deleg.handle2

try:
    if (ch_but1.supportsRead()):
        print int(ch_but1.read().encode('hex'), 16)
    if (ch_but2.supportsRead()):
        print int(ch_but2.read().encode('hex'), 16)
    ch_led1.write(b'\x01')
    ch_led2.write(b'\x01')

    while True:
	if dev.waitForNotifications(3.0):
            print "get notification"
	    continue
        else:
            print "no note detected"

finally:
    dev.disconnect()
