# pip install pandas
# pip install pandas openpyxl

import os
import pandas as pd

# Define the directory containing the Excel files
directory = r"C:/Users/nickt/Downloads"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an Excel file
    if filename.endswith(".xlsx"):
        # Construct full file path
        excel_file_path = os.path.join(directory, filename)
        # Construct the CSV file path by changing the file extension
        csv_file_path = os.path.join(directory, filename.replace(".xlsx", ".csv"))

        # Read the Excel file
        read_file = pd.read_excel(excel_file_path)

        # Save the file as CSV with UTF-8 encoding
        read_file.to_csv(csv_file_path, index=False, header=True, encoding='utf-8')

        print(f"Converted {filename} to CSV.")

print("All files have been converted.")
