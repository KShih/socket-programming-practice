import socket
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080
msg = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.sendall(bytes(msg, "UTF-8"))
    print(f"Sent: {msg}")
    data = str(s.recv(1024), 'UTF-8')

print(f"Received: {data}")

# python3 echo_tcp_client.py sfdsd Ted is cool23432
# python3 echo_tcp_client.py Ted is SECRET cool
# python3 echo_tcp_client.py 123Ted 32is 343SECRET cool