# Month 1 — Security Foundations (Linux, Networking, Python)
This repo scaffolds your Month 1 training pack and a **target Ubuntu VM** via Vagrant.

## Contents
- `scripts/` — deliverable Python scripts (log parser, local port scanner)
- `labs/` — lab guides for Linux basics, networking/TCP handshake, safe local scanning, and CSV log parsing
- `target-ubuntu/` — **Vagrantfile** + provisioning script to spin up a clean Ubuntu VM as your target (private network)
- `docs/` — extra notes
- `sample_logs.csv` — example CSV to test the log parser
- `Makefile` — convenience tasks
- `.gitignore` — standard Python ignores

## Quick start
1. Install **VirtualBox** and **Vagrant** on the host.
2. Start the target VM:
   ```bash
   cd target-ubuntu
   vagrant up
   # SSH in if needed:
   vagrant ssh
   ```
   The target uses a private IP: **192.168.56.20**.
3. On your Kali (or host), run the scripts (examples below).

## Scripts (safe/lab-only)
- `scripts/log_parser.py` — CSV → summary.
- `scripts/local_port_scanner.py` — TCP connect-style scanner. Defaults to `127.0.0.1`. **Only use on lab targets you own**.

## Examples
```bash
# On Kali or host (inside repo root)
python3 scripts/log_parser.py sample_logs.csv --top 3

# Localhost (safe default)
python3 scripts/local_port_scanner.py

# Scan the target VM (lab-only, safe range)
python3 scripts/local_port_scanner.py --ip 192.168.56.20 --start 1 --end 200 --timeout 0.3
```

## Safety
- Operate **only** inside your isolated lab.
- Do not scan, probe, or test any system you do not own or lack explicit written permission to test.
- The provided Vagrant target is for your private network only.

## License
MIT
