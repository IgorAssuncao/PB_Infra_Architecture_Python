import os
import sys
import socket

host, port = socket.gethostname(), 9901

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((host, port))
except Exception as error:
    print(error)
    sys.exit(1)
