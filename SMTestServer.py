import socket
ServerIP = input("Please enter desired host IP address")
ServerPort = int(input("Please enter desired host port"))

suggestPosts = ["post 1", "post 2", "post 3"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind((ServerIP, ServerPort))
    mySocket.listen()
    conn, addr = mySocket.accept()
    with conn:
        print('Connected to: ' , addr)
        while True:
            data = conn.recv(1024)
            requestedNum = int.from_bytes(data, 'little', signed = False)
            print(requestedNum)
            conn.sendall(suggestPosts[requestedNum].encode('utf-8'))
