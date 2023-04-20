#!usr/bin/python3
import socket
hostname=input("Enter domain name:")
addr=socket.gethostbyname(hostname)
print(f"The ip address of {hostname} is {addr}")
