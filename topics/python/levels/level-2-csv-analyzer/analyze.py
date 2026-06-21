#!/usr/bin/env python3
"""CSV Data Analyzer — reads employee data and produces a JSON report."""
import csv
import json
import sys
import os

def analyze(filepath):
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found.")
        sys.exit(1)

    departments = {}
    highest_paid = None
    total_employees = 0

    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Validate row
            try:
                name = row['name']
                department = row['department']
                salary = float(row['salary'])
                years = float(row['years_at_company'])
            except (KeyError, ValueError) as e:
                print(f"Warning: skipping malformed row: {row} ({e})")
                continue

            total_employees += 1

            # Track departments
            if department not in departments:
                departments[department] = {'total_salary': 0, 'count': 0}
            departments[department]['total_salary'] += salary
            departments[department]['count'] += 1

            # Track highest paid
            if highest_paid is None or salary > highest_paid['salary']:
                highest_paid = {'name': name, 'salary': int(salary)}

    # Build report
    dept_report = {}
    for dept, data in departments.items():
        dept_report[dept] = {
            'avg_salary': round(data['total_salary'] / data['count'], 2),
            'count': data['count']
        }

    report = {
        'departments': dept_report,
        'highest_paid': highest_paid if highest_paid else {},
        'total_employees': total_employees
    }

    with open('report.json', 'w') as f:
        json.dump(report, f, indent=2)

    print("Report written to report.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze.py <csv_file>")
        sys.exit(1)
    analyze(sys.argv[1])
