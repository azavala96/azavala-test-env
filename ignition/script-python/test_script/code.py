import socket

HOST = "192.168.120.68"
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
	s.connect((HOST,PORT))
	s.sendall(b"Hello World")
