from blink import nic_send, nic_recv

while True:
    command = input("Send, receive, or exit? (s, r, e): ")
    if command == 's':
        pattern = input("Bit pattern to send? (1010): ")
        nic_send(pattern)
    elif command == 'r':
        print(nic_recv())
    elif command == 'e':
        break
