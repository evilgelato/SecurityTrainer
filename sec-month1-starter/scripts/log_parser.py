#!/usr/bin/env python3
import csv
import argparse
from collections import Counter, defaultdict

def parse_csv(path):
    totals = 0
    src_ip_counts = Counter()
    status_counts = Counter()
    path_counts = Counter()
    by_date = defaultdict(int)
    with open(path, newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            totals += 1
            src = row.get('src_ip') or row.get('source') or row.get('ip')
            status = row.get('status') or row.get('status_code') or 'unknown'
            path = row.get('path') or row.get('url') or row.get('request')
            ts = row.get('timestamp') or row.get('time') or ''
            if src:
                src_ip_counts[src] += 1
            if status:
                status_counts[status] += 1
            if path:
                path_counts[path] += 1
            if ts:
                date = ts.split('T')[0] if 'T' in ts else ts.split(' ')[0]
                by_date[date] += 1

    return {
        'total': totals,
        'src_ip_counts': src_ip_counts,
        'status_counts': status_counts,
        'path_counts': path_counts,
        'by_date': by_date
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument('csvfile', help='CSV log file path')
    p.add_argument('--top', type=int, default=5, help='top N items to show')
    args = p.parse_args()

    stats = parse_csv(args.csvfile)
    print(f"Total log lines: {stats['total']}\n")
    print("Top source IPs:")
    for ip, cnt in stats['src_ip_counts'].most_common(args.top):
        print(f"  {ip:>15}  {cnt}")
    print("\nStatus codes:")
    for s, cnt in stats['status_counts'].most_common():
        print(f"  {s:>6}  {cnt}")
    print("\nTop requested paths:")
    for path, cnt in stats['path_counts'].most_common(args.top):
        print(f"  {path:>30}  {cnt}")
    print("\nCounts by date:")
    for d, cnt in sorted(stats['by_date'].items()):
        print(f"  {d} : {cnt}")

if __name__ == '__main__':
    main()
