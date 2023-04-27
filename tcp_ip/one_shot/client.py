import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server

# Connect to the server. Notice the similarity to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    address = (HOST, PORT)

    # only connects to specified address.
    s.connect(address)

    while 1:
        # Send data to the server
        # message = "henlo freind I bring the bepsi with ice cuboids"

        message = input("Enter message to send to server: ")

        # notice how this also works to send data to the server.
        s.send(message.encode())

        # Receive data from the server
        data = s.recv(1024)
        print(f"Received data: {data.decode()}")

        # breaks if data is none
        if not data:
            break
