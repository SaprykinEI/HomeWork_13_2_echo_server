import socket

HOST = '127.0.0.1'
PORT = 50432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Ошибка: сервер недоступен")
        exit(0)  # Корректное завершение

    while True:
        data_to_send = input("Message to send: ").strip()
        if not data_to_send:
            print("Сообщение не может быть пустым!")
            continue

        try:
            sock.sendall(data_to_send.encode())

            if data_to_send.lower() in ["exit", "shutdown"]:  # Если exit или shutdown
                response = sock.recv(1024).decode()
                print("Сервер ответил:", response)
                print("Отключение от сервера")
                break  # Выходим из цикла

            data_received = sock.recv(1024).decode()
            print("Received:", data_received)

        except ConnectionResetError:
            print("Соединение с сервером потеряно.")
            break  # Выходим из цикла
        except ConnectionAbortedError:
            print("Сервер закрыл соединение.")
            break  # Выходим из цикла

    print("Process finished with exit code 0")
