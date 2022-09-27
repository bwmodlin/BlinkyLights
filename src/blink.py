import pigpio

def nic_send(bits):
    pi1 = pigpio.pi()
    port1_xmit_status = bits[0]
    port2_xmit_status = bits[1]
    port3_xmit_status = bits[2]
    port4_xmit_status = bits[3]

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
    # Port 1 Input/Recv
    port1_status = str(pi2.read(26))
    if port1_status =="1":
        port1_status = "0"
    elif port1_status == "0":
        port1_status = "1"
    # Port 2 Input/Recv
    port2_status = str(pi2.read(24))
    if port2_status == "1":
        port2_status = "0"
    elif port2_status == "0":
        port2_status = "1"
    # Port 3 Input/Recv
    port3_status = str(pi2.read(22))
    if port3_status == "1":
        port3_status = "0"
    elif port3_status == "0":
        port3_status = "1"
    # Port 4 Input/Recv
    port4_status = str(pi2.read(20))
    if port4_status == "1":
        port4_status = "0"
    elif port4_status == "0":
        port4_status = "1"
    binary_string = port1_status + port2_status + port3_status + port4_status
    return binary_string

