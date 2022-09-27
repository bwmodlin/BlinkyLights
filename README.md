# BlinkyLights
<strong>Authors:</strong> Tyler Chang, Ben Modlin
<br />
<strong>Language:</strong> Python
<br />
<strong>Contents:</strong>
There are two Python files included in the src directory. "blink.py" contains the code for the API that works with all the ports simultaneously. This primarily consists of the nic_send() and nic_recv() functions. "drive.py" is a simple program that provides a command line interface for interactively sending and receiving with the "blink.py" library.
<br />
<strong>Instructions:</strong>
<br />
Run "drive.py" in the command line and it should prompt you with an option to enter "s"(send), "r"(receive), or "e"(exit). Inputting "s" would then result in prompt to enter the a 4 bit value with each bit referring to an individual transmitter. For this programs convention, the left most bit refers to the transmission at port 1, followed by the transmission at port 2, and so on. 1 stands for light on and 0 stands for light off. So for example, 1010 would mean turning the lights on for transmissions at ports 1 and 3 and turning the lights off for transmissions at ports 2 and 4.
<br />
Selecting the "r" option would return a 4 bit value in the terminal with each bit referring to an individual receiver. The same convention follows with the left most bit referring to the receiver at port 1, followed by the receiver at port 2, and so on. 0 means the light is off and 1 means the light is on. Selecting the "e" optiono would terminate the script.
