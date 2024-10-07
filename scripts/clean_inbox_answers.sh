#!/bin/bash

# Set start and end dates (adjust as needed)
start_date="2024-10-06"
end_date="2024-11-01"

# Get today's date
today=$(date +"%Y-%m-%d")

# Compare dates and exit if today is outside the range
if [[ "$today" < "$start_date" || "$today" > "$end_date" ]]; then
    exit 0
fi

# Your job logic here
python3 clean_inbox_answers.py
