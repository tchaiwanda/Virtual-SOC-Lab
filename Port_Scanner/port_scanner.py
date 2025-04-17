import socket
import nmap

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Set timeout for connection attempt
    try:
        result = sock.connect_ex((host, port))  # Attempt to connect
        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED on {host}")
    finally:
        sock.close()  # Ensure the socket is closed even if there is an error

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

def advanced_scan(host):
    nm = nmap.PortScanner()
    nm.scan(host, '1-1024')  # Scan ports 1-1024
    # Add a protocol (e.g., 'tcp')
    protocol = 'tcp'
    print(f"Protocol: {protocol}")
    lport = list(nm[host][protocol].keys())  # Convert to a list for compatibility
    for port in lport:
        print(f"Port {port} is {nm[host][protocol][port]['state']}")

if __name__ == "__main__":
    target_host = input("Enter the target IP or domain: ")

    scan_type = input("Choose scan type: (1) Basic scan, (2) Nmap scan: ")

    if scan_type == "1":
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        scan_ports(target_host, start_port, end_port)
    elif scan_type == "2":
        advanced_scan(target_host)
    else:
        print("Invalid option. Exiting.")

