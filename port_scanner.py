# port_scanner.py

import socket

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = scanner.connect_ex((ip, port))
    scanner.close()
    return result == 0

def main():
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

if __name__ == "__main__":
    main()
