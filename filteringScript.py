import csv

# --- CONFIG ---
INPUT_CSV = "file.csv"      # <-- your input file
OUTPUT_CSV = "filtered_file.csv" # <-- output file you want

TARGET_ID = 0x000

# --- PROCESS ---
with open(INPUT_CSV, 'r') as infile, open(OUTPUT_CSV, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

    writer.writeheader()  # Copy the header to the output CSV

    for row in reader:
        try:
            can_id = int(row['address'], 16)
        except ValueError:
            continue  # Skip invalid rows

        if can_id == TARGET_ID:
            writer.writerow(row)

print(f"Saved all frames with ID 0x30A to {OUTPUT_CSV}")
