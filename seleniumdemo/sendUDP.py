# Python 3.7
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# addressing information of target
UDP_PORT = 5005
MESSAGE = '''test. Hello, World!test. Hello, World!test.Hello, World!test.Hello,World!test. Hello,
World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello,
World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello,
World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello,
World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello, World!test. Hello, World!'''
# SOCK_DGRAM specifies that this is UDP
for i in range(16, 31):
    time.sleep(1)
    for j in range(1, 50):
        for k in range(1, 255):
            UDP_IP = "172.{0}.{1}.{2}".format(i, j, k)
            print("IP:", UDP_IP)
            sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
# close the socket
sock.close()
