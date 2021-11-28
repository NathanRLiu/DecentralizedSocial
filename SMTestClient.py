import socket

desiredIP = input("Please enter node IP")
desiredPort = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((desiredIP, desiredPort))
    mySocket.sendall((1).to_bytes(1,'little'))
    data = mySocket.recv(1024)
print("Received: " + data.decode("utf-8"))
