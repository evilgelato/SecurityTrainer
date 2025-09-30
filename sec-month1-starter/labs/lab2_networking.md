# Lab 2 — Networking & TCP Handshake
1) On target VM: `nc -l 4444`
2) On Kali: `sudo tcpdump -i any -n tcp port 4444 -w syn_handshake.pcap`, then `nc 192.168.56.20 4444` and type a message.
3) Inspect the pcap and identify SYN / SYN-ACK / ACK.
4) Deliverable: one-paragraph explanation + screenshot of the three packets.
