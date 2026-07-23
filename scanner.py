import socket

target = input("Enter IP address to scan: ")
print("Scanning " + target + "...")
print("-" * 40)

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print("Port " +str(port) + " is OPEN")
        sock.close()

print("-" * 40)
print("Scan complete.")

