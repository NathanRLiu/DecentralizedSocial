import socket

desiredIP = input("Please enter node IP")
#desiredIP = "localhost"
desiredPort = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((desiredIP, desiredPort))
    counter = 0
    while (True):
        counter = 0
        userChoice = input("Go to next post (n), previous post(p), or save(s), or TESTCASE(t)")
        if (userChoice == "n"):
            counter += 1
            mySocket.sendall((counter).to_bytes(1,'little'))
        elif (userChoice == "p"):
            counter -= 1
            mySocket.sendall((counter).to_bytes(1,'little'))
        elif (userChoice == "s"):
            #save the current post
            pass
        elif (userChoice == "t"):
            mySocket.sendall(("a34").encode('utf-8'))
        else:
            mySocket.sendall(userChoice.encode('utf-8'))
        data = mySocket.recv(1024)
        print("Received: " + data.decode("utf-8"))
