import socket
  
def scan_ports(target, port_range=(1, 1024)):
    print(f"\n[+] Scanning target: {target}")
    open_ports = []
    
    for port in range(port_range[0], port_range[1] + 1):  # ✅ use 'port'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\n   [OPEN] Port {port}")  # ✅ 'print' instead of 'printf'
            open_ports.append(port)
        s.close()
        
    if not open_ports:
        print("\n    [!] No Open Ports Found.")
        
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP/domain: ")  # ✅ use 'input' instead of 'import'
    start = int(input("Enter starting port: "))
    end = int(input("Enter ending port: "))
    open_ports = scan_ports(target, (start, end))
