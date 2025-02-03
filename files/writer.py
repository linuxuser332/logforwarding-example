import socket
import time
# Define the path to the Unix socket
SOCKET_PATH = '/var/log/log_socket'
# Create a Unix stream socket (SOCK_STREAM)
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# Connect to the Unix socket
sock.connect(SOCKET_PATH)
# Function to generate and send log data
def generate_log_data():
    log_messages = [
        "INFO: System started successfully.",
        "ERROR: Unable to open file '/path/to/file'.",
        "WARNING: Disk space running low.",
        "INFO: User 'john' logged in.",
        "DEBUG: Connection established to server 192.168.1.1."
    ]
    for message in log_messages:
        yield message
# Send log data to the socket
try:
    for log_message in generate_log_data():
        # Write log data to the socket
        sock.sendall(log_message.encode('utf-8'))
        print(f"Sent: {log_message}")  # Optional: print the message for debugging
        time.sleep(2)  # Simulate some time between log messages
finally:
    # Close the socket connection after sending data
    sock.close()
