# GPT generated and modified by yours truly-- Don't hate the player, hate the game.
import socket

# Set up the socket
HOST = '127.0.0.1'  # Listen on all available network interfaces
PORT = 12345  # Port to listen on

# with context is optional, it is best-practice but to a new programmer
# it might be a little confusing.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    address = (HOST, PORT)

    # address in this case is a data type called a 'tuple'. It's similar to a list,
    # but in the same way kinda different.
    s.bind(address)

    # server will not be able to connect without this call. This is what starts the server.
    s.listen()

    # message printed to terminal that program has successfully begun listening.
    print(f"Listening on port {PORT}...")

    # Wait for a connection. the s.accept() call actually returns a 'tuple' like I mentioned earlier,
    # and they can be assigned to individual variables like so.
    conn, addr = s.accept()
    with conn:
        # print IP address of client
        print(f"Connected by {addr}")

        # Receive and print data until the connection is closed
        while True:
            data = conn.recv(1024)
            print(f"Received data: {data.decode()}")

            # to send a message back (the same message...)
            # conn.send(bytes("henlo friend", "utf-8"))

            # to make this a little more dynamic, we can prompt the user for input on what to send
            # to the client, like so.
            user_input = input(f"Please enter a message to send to {addr}: ")

            # this is a TCP socket, so you have to send computer language (bytes)
            # so we can easily convert the user input string to hex and send it over the wire.
            conn.send(bytes(user_input, 'utf-8'))

            # if connection fails, breaks while loop.
            if not data:
                break
