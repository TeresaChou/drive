#!/usr/bin/python
import smbus
import time
bus = smbus.SMBus(1)
address = 0x53
EARTH_GRAVITY_MS2 = 9.80665
SCALE_MULTIPLIER = 0.004
DATA_FORMAT = 0x31
number_prev = 0

# set bandwidth rate
bus.write_byte_data(address, 0x2C, 0x0C)
# set range
# value = bus.read_byte_data(address, DATA_FORMAT)
# value &= ~0x0F;
# value |= 0x00;
# value |= 0x08;
# bus.write_byte_data(address, DATA_FORMAT, value)
# enable measurement
# bus.write_byte_data(address, 0x2D, 0x08)

def readNumber():
    bytes = bus.read_i2c_block_data(address, 0x32, 6)

    x = bytes[0] | (bytes[1] << 8)
    if(x & (1 << 16 - 1)):
        x = x - (1<<16)

    y = bytes[2] | (bytes[3] << 8)
    if(y & (1 << 16 - 1)):
        y = y - (1<<16)

    z = bytes[4] | (bytes[5] << 8)
    if(z & (1 << 16 - 1)):
        z = z - (1<<16)

    x = x * SCALE_MULTIPLIER 
    y = y * SCALE_MULTIPLIER
    z = z * SCALE_MULTIPLIER

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)
    
    return {"x": x, "y": y, "z": z}

while True:
    time.sleep(1)
    number = readNumber()
    print number
    if number != number_prev:
        print "activity detected!"
    number_prev = number
