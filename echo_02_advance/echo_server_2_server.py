import socket

HOST = '127.0.0.1'
PORT = 50432

if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_stock:
        serv_stock.bind((HOST, PORT))
        serv_stock.listen()

        while True:
            print("Ожидаю подключения...")
            sock, addr = serv_stock.accept()
            with sock:
                print("Подключение по", addr)
                while True:
                    try:
                        data = sock.recv(1024)
                    except ConnectionError:
                        print("Клиент внезапно отключился в процессе отправки данных на сервер")
                        break
                    print(f"Получено: {data}, from {addr}")
                    data = data.upper()

                    print(f"Sen: {data} to {addr}")
                    try:
                        sock.sendall(data)
                    except ConnectionError:
                        print(f"Клиент внезапно отключился не могу отправить данные")
                        break
                print("Отключению по", addr)