import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 8080))

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received: {data.decode('utf-8')}")

# Få bytevärdet som en lista av heltal
byte_values = list(data)
print("Bytevärden:", byte_values)

# Close the client socket
client_socket.close()