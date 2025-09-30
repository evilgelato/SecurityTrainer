# Convenience tasks
.PHONY: help test scan-local

help:
	@echo "Targets:"
	@echo "  test         Run log parser on sample_logs.csv"
	@echo "  scan-local   Run the local port scanner on localhost"

test:
	python3 scripts/log_parser.py sample_logs.csv --top 5

scan-local:
	python3 scripts/local_port_scanner.py
