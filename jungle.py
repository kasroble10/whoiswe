import argparse
import argparse
import ipaddress
import socket
import threading
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

banner = rf"""
{Fore.RED}
 ██████╗ ██╗   ██╗ ██████╗ ██████╗ ██╗      █████╗ ██████╗ ███╗   ██╗
 ██╔════╝ ██║   ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██╔══██╗████╗  ██║
 ██║  ███╗██║   ██║██║   ██║██████╔╝██║     ███████║██████╔╝██╔██╗ ██║
 ██║   ██║██║   ██║██║   ██║██╔═══╝ ██║     ██╔══██║██╔═══╝ ██║╚██╗██║
 ╚██████╔╝╚██████╔╝╚██████╔╝██║     ███████╗██║  ██║██║     ██║ ╚████║
  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝

{Fore.LIGHTYELLOW_EX}        Created by Bellami Cyber Jungle ⚡
"""

def scan_host(ip, ports, stealth):
    open_ports = {}
    for port in ports:
        try:
            if stealth:
                time.sleep(random.uniform(0.2, 0.7))
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.8)
                result = sock.connect_ex((str(ip), port))
                if result == 0:
                    try:
                        sock.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
                        banner_data = sock.recv(1024).decode(errors="ignore").strip()
                    except:
                        banner_data = "No banner"
                    service = detect_service(port, banner_data)
                    open_ports[port] = (service, banner_data.splitlines()[0] if banner_data else "No banner")
        except Exception:
            continue
    return open_ports

def detect_service(port, banner):
    if "SSH" in banner or port == 22:
        return "SSH service detected"
    elif "HTTP" in banner or port in [80, 8080]:
        return "HTTP service"
    elif port == 443:
        return "HTTPS or TLS service"
    return "Unknown service"

def worker(ip, ports, stealth):
    results = scan_host(ip, ports, stealth)
    if results:
        print(f"{Fore.GREEN}[+] {ip} → Open ports and banners:")
        for port, (service, banner) in results.items():
            print(f"    Port {port}: {service} → {banner}")
    else:
        print(f"{Fore.RED}[-] {ip} → No open ports")

def main():
    print(banner)
    parser = argparse.ArgumentParser(description="🔍 JungleScan: Stealthy Red Team Port Scanner")
    parser.add_argument("--subnet", required=True, help="Target subnet in CIDR format (e.g., 192.168.1.0/24)")
    parser.add_argument("--ports", required=True, help="Comma-separated list of ports (e.g., 22,80,443)")
    parser.add_argument("--threads", type=int, default=20, help="Number of threads (default: 20)")
    parser.add_argument("--stealth", action="store_true", help="Enable stealth mode (slower, more evasive)")

    args = parser.parse_args()
    ports = [int(p.strip()) for p in args.ports.split(',')]
    subnet = list(ipaddress.IPv4Network(args.subnet).hosts())

    print(f"{Fore.CYAN}[+] Scanning {len(subnet)} hosts on ports {ports} with {args.threads} threads{' (stealth enabled)' if args.stealth else ''}...")

    thread_list = []
    for ip in subnet:
        while threading.active_count() > args.threads:
            time.sleep(0.1)
        t = threading.Thread(target=worker, args=(ip, ports, args.stealth))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    main()
