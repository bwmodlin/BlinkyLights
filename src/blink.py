import pigpio

def nic_send(bits):
    pi1 = pigpio.pi()

    # Extracting the bit values and storing them
    port1_xmit_status = bits[0]
    port2_xmit_status = bits[1]
    port3_xmit_status = bits[2]
    port4_xmit_status = bits[3]

    # Writing the bit values to the corresponding ports

    # Port 1 Output/Xmit
    pi1.write(27,int(port1_xmit_status))
    # Port 2 Output/Xmit
    pi1.write(25, int(port2_xmit_status))
    # Port 3 Output/Xmit
    pi1.write(23, int(port3_xmit_status))
    # Port 4 Output/Xmmit
    pi1.write(21, int(port4_xmit_status))

def nic_recv():
    pi2 = pigpio.pi()

    # Must flip the 1's and 0's because LEDs are incorrectly inverted
    # Port 1 Input/Recv
    port1_status = str(1 - pi2.read(26))

    # Port 2 Input/Recv
    port2_status = str(1 - pi2.read(24))

    # Port 3 Input/Recv
    port3_status = str(1 - pi2.read(22))

    # Port 4 Input/Recv
    port4_status = str(1 - pi2.read(20))

    binary_string = port1_status + port2_status + port3_status + port4_status
    return binary_string

