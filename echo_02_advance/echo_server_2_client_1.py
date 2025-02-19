import socket

HOST = '127.0.0.1'
PORT = 50432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        data_to_send = input("Message to send: ")
        if not data_to_send:
            print("Сообщение не может быть пустым. Попробуйте снова")
            continue

        data_bytes_send = data_to_send.encode()
        sock.sendall(data_bytes_send)
        data_bytes_receive = sock.recv(1024)
        data_received = data_bytes_receive.decode()
        print("Received:", data_received)