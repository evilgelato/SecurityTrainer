# Lab 3 — Safe Enumeration (Local + Target)
1) On target VM:
   - `python3 -m http.server 8000` (serves current directory)
   - `nc -l 9001` (listener)
2) Verify listeners: `ss -tuln`
3) On Kali: compare `nmap -sT -p 1-1024 192.168.56.20` with `python3 scripts/local_port_scanner.py --ip 192.168.56.20 --start 1 --end 1024`
4) Deliverable: both outputs + brief comparison.
