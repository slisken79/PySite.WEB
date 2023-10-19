import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("127.0.0.1", 8080))

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening for connections...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Send data to the client
    message = b"Hello, client!"
    client_socket.send(message)

    # Skriv ut meddelandet som en sträng
    print("Skickade meddelande:", message.decode('utf-8'))

    # Få bytevärdet som en lista av heltal
    byte_values = list(message)
    print("Bytevärden:", byte_values)

    # Close the client socket
    client_socket.close()