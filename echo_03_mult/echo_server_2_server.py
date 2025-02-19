import socket
import threading


HOST = '127.0.0.1'
PORT = 50432


server_running = True

def handle_connection(sock, addr):
    global server_running
    with sock:
        print("Подключение по", addr)
        while True:
            try:
                data = sock.recv(1024).decode().strip()
                if not data:
                    print(f"Клиент {addr} разорвал соединение")
                    break

                if data.lower() == "exit":
                    print(f"Клиент {addr} отключился по своей команде")
                    sock.sendall("Server closing connection".encode())
                    break

                if data.lower() == "shutdown":
                    print("Команда shutdown получена. Завершаем сервер...")
                    sock.sendall("Server shutting down".encode())
                    server_running = False
                    break

                print(f"Получено: {data}, от {addr}")
                response = data.upper()
                sock.sendall(response.encode())

            except ConnectionError:
                print(f"Клиент {addr} внезапно отключился")
                break

        print(f"Соединение с {addr} закрыто")

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(1)

        while server_running:
            print("Waiting for connection...")
            try:
                sock, addr = serv_sock.accept()
            except OSError:
                break
            t = threading.Thread(target=handle_connection, args=(sock, addr))
            t.start()

        print("Сервер завершил свою работу.")
