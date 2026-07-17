#!/usr/bin/env python3

import socket

try:
    target_port = int(input("Type Target Port: "))
  target_host = input("Type Target Host: ")

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  sock.connect((target_host, target_port))

  sock.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

  res = sock.recv(4096)

  print(res.decode())

  sock.close()
except:
  print("Something went wrong")
