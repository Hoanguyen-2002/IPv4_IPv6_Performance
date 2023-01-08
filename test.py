import socket
import time

# Set the target host and port
HOST = "google.com"
PORT = 80

# Test the performance of IPv4
start_time = time.time()

# Create a socket using IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

end_time = time.time()
ipv4_time = end_time - start_time
print("IPv4 start-time: "+ str(start_time))
print("Ipv4 end-time: "+ str(end_time))
print(f"IPv4 connection established in {ipv4_time:.2f} seconds")

# Test the performance of IPv6
start_time = time.time()

# Create a socket using IPv6
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

end_time = time.time()
ipv6_time = end_time - start_time
print("IPv6 start-time: "+ str(start_time))
print("Ipv6 end-time: "+ str(end_time))
print(f"IPv6 connection established in {ipv6_time:.2f} seconds")

# Compare the performance of IPv4 and IPv6
if ipv4_time < ipv6_time:
    print("IPv4 is faster than IPv6")
elif ipv4_time > ipv6_time:
    print("IPv6 is faster than IPv4")
else:
    print("IPv4 and IPv6 have the same performance")
