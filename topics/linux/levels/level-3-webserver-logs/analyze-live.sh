#!/usr/bin/env bash

# Check if logfile argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./analyze-live.sh <logfile> [N]"
    exit 1
fi

LOGFILE="$1"
N="${2:-5}"

# Check if file exists
if [ ! -f "$LOGFILE" ]; then
    echo "Error: file '$LOGFILE' not found"
    exit 1
fi

# Top N IPs
echo "=== Top $N IPs ==="
awk '{print $1}' "$LOGFILE" | sort | uniq -c | sort -rn | head -"$N" | awk '{print $2"\t"$1}'

# Error breakdown
echo ""
echo "=== Errors ==="
echo "4xx errors: $(awk '$9 ~ /^4[0-9][0-9]$/' "$LOGFILE" | wc -l)"
echo "5xx errors: $(awk '$9 ~ /^5[0-9][0-9]$/' "$LOGFILE" | wc -l)"

# Busiest hour
echo ""
echo "=== Busiest hour ==="
BUSIEST=$(awk -F'[' '{print $2}' "$LOGFILE" | awk -F':' '{print $2}' | sort | uniq -c | sort -rn | head -1)
COUNT=$(echo "$BUSIEST" | awk '{print $1}')
HOUR=$(echo "$BUSIEST" | awk '{print $2}')
echo "${HOUR}:00 (count: $COUNT)"

# Total requests
echo ""
echo "=== Total ==="
echo "Total requests processed: $(wc -l < "$LOGFILE")"
