import socket

HOST = socket.gethostname()                 # Symbolic name meaning all available interfaces
PORT = 5550             # Arbitrary non-privileged port
hostSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hotSocket.bind((HOST, PORT))
hostSocket.listen(1)
while 1:
    try:
        connectionSocket, addr = s.accept()
        print addr
        while 1:
            data = conn.recv(1024)
            print data
    except KeyboardInterrupt:
        conn.close()
        s.close()
