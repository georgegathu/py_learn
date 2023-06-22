# Install socket using: pip install socket
import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return True
    except Exception:
        return False

def main():
    host = input("Enter the host to scan: ")
    ports = input("Enter the ports to scan (comma-separated): ")
    ports = ports.split(",")

    for port in ports:
        open_port = scan_port(host, int(port))
        if open_port:
            print("Port {} is open".format(port))

if __name__ == "__main__":
    main()
