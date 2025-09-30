#!/usr/bin/env python3
import socket
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(ip, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            res = s.connect_ex((ip, port))
            if res == 0:
                return port, True
            return port, False
    except Exception:
        return port, False

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--ip', default='127.0.0.1', help='Target IP (default 127.0.0.1)')
    p.add_argument('--start', type=int, default=1, help='Start port')
    p.add_argument('--end', type=int, default=1024, help='End port')
    p.add_argument('--timeout', type=float, default=0.5, help='Socket timeout seconds')
    p.add_argument('--workers', type=int, default=100, help='Threadpool size')
    args = p.parse_args()

    if args.ip != '127.0.0.1':
        print("WARNING: Non-local IP specified. Ensure this is a lab target you own and is isolated.")
    ports = range(args.start, args.end + 1)
    open_ports = []
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(scan_port, args.ip, p, args.timeout): p for p in ports}
        for fut in as_completed(futures):
            port, is_open = fut.result()
            if is_open:
                print(f"[+] {args.ip}:{port} OPEN")
                open_ports.append(port)
    elapsed = time.time() - start_time
    print(f"\nScan complete: {len(open_ports)} open ports found in {elapsed:.2f}s")
    if open_ports:
        print("Open ports:", open_ports)

if __name__ == '__main__':
    main()
