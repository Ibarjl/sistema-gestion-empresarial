#!/usr/bin/env python3
import csv
import subprocess
import sys

def create_issue(title, body, labels):
    """Create a GitHub issue using gh CLI"""
    cmd = [
        'gh', 'issue', 'create',
        '--title', title,
        '--body', body,
        '--label', labels
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Created: {title}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {title} - {e.stderr}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python import_issues.py github_issues.csv")
        sys.exit(1)

    csv_file = sys.argv[1]
    success_count = 0
    total_count = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_count += 1
            title = row['title'].strip('"')
            body = row['body'].strip('"')
            labels = row['labels'].strip('"')

            if create_issue(title, body, labels):
                success_count += 1

    print(f"\n📊 Summary: {success_count}/{total_count} issues created successfully")

if __name__ == "__main__":
    main()