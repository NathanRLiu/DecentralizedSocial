import socket
ServerIP = input("Please enter desired host IP address")
#ServerPort = int(input("Please enter desired host port"))
#ServerIP = "localhost"
ServerPort = 3000

suggestPosts = []
knownNodes = []

yesOrNo = {
        "y":True,
        "n":False}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind((ServerIP, ServerPort))
    mySocket.listen()
    conn, addr = mySocket.accept()#need to add multithreading here
    with conn:
        print('Connected to: ' , addr)
        knownNodes.append(addr)
        while True:
            data = conn.recv(1024)
            payload = data.decode('utf-8')
            if (payload[0] == "a"):
                myIndex = int(payload[1:])
                if (myIndex <= len(knownNodes)):
                    print(knownNodes[myIndex])
                    conn.sendall(knownNodes[myIndex][0].encode('utf-8'))
                else:
                    conn.sendall(('Known Nodes Index is out of bounds!').encode('utf-8'))
            elif (payload[0] == "b"):
                print("detected b")
                requestedNum = int.from_bytes(data, 'little', signed = False)
                print(requestedNum)
                conn.sendall(suggestPosts[requestedNum].encode('utf-8'))
            elif (payload[0] == "c"):
                userContent = payload[1:]
                print("New Post: " + userContent)
                if (yesOrNo[input("Pass it on? (y/n)")]):
                    suggestPosts.append(userContent)
