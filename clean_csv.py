#!/usr/bin/env python3
import csv

# Read the CSV file and filter out rows where Transaction type is 'WITH'
input_file = 'source/IG-DividendTransactionHistory.csv'
output_file = 'source/IG-DividendTransactionHistory.csv'

# Read all rows first
rows_to_keep = []
with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header
    rows_to_keep.append(header)

    deleted_count = 0
    for row in reader:
        # Check if the Transaction type column (index 5) is 'WITH'
        if len(row) > 5 and row[5] == 'WITH':
            deleted_count += 1
            print(f"Deleting row: {row[0]} - {row[1]} - {row[5]}")
        else:
            rows_to_keep.append(row)

# Write the filtered data back to the file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows_to_keep)

print(f"\nDeleted {deleted_count} rows with Transaction type 'WITH'")
print(f"Remaining rows: {len(rows_to_keep) - 1}")  # -1 for header