import socket

# The target is a legal test site provided by the Nmap project
target = "scanme.nmap.org" 
# We will test Port 22 (SSH) and Port 80 (Web)
ports = [22, 80, 443]

print(f"--- SCANNING {target} ---")

for port in ports:
    # Create a 'socket' (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a 2-second timeout (don't wait forever)
    s.settimeout(2)
    
    # connect_ex returns 0 if the connection is successful
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port}: [ OPEN ]")
    else:
        print(f"Port {port}: [ CLOSED ]")
    
    # Always close the socket
    s.close()

print("--- SCAN COMPLETE ---")

