import pigpio

def nic_send(bits):
    pi1 = pigpio.pi()
    port1_xmit_status = bits[0]
    port2_xmit_status = bits[1]
    port3_xmit_status = bits[2]
    port4_xmit_status = bits[3]

    # Port 1 Output/Xmit
    pi1.write(27, port1_xmit_status)
    # Port 2 Output/Xmit
    pi1.write(25, port2_xmit_status)
    # Port 3 Output/Xmit
    pi1.write(23, port3_xmit_status)
    # Port 4 Output/Xmmit
    pi1.write(21, port4_xmit_status)

def nic_recv():
    # Port 1 Input/Recv
    port1_status = str(pi1.read(26))
    # Port 2 Input/Recv
    port2_status = str(pi1.read(24))
    # Port 3 Input/Recv
    port3_status = str(pi1.read(22))
    # Port 4 Input/Recv
    port4_status = str(pi1.read(20))
    
    binary_string = port1_status + port2_status + port3_status + port4_status
    return binary_string

    

