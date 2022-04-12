import errno
import socket

def get_secret_digit(data: str):
    secret_code = "SECRET"
    result_str, result_code = "", 0
    if data.find(secret_code) != -1:
        for c in data:
            if c.isdigit():
                result_str += c
    else:
        result_code = -1
    return result_str, result_code

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            result_str, result_code = get_secret_digit(str(data))
            msg = ""
            if result_code != -1:
                msg = f"Digits: {result_str} Count: {len(result_str)}"
            else:
                msg = "Secret code not found."
            try:
                conn.sendall(bytes(msg, 'UTF-8'))
            except socket.error as e:
                if isinstance(e.args, tuple) and e[0] == errno.EPIPE:
                    pass
                else:
                    print(f"error found in sending data: {e}")
