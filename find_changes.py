import pandas as pd
import re

# Function to extract date and time from the filename
def extract_datetime(filename):
    match = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', filename)
    if match:
        return match.group(0)
    else:
        return None

csv1 = "permhash_2024-02-28_12-53-28.csv"
csv2 = "permhash_2024-02-28_17-31-26.csv"

# Load data from the first CSV file
df1 = pd.read_csv(csv1)
# Load data from the second CSV file
df2 = pd.read_csv(csv2)

# Extract date and time from the filenames and add as the first column
df1_datetime = extract_datetime(csv1)
df2_datetime = extract_datetime(csv2)

# Compare the contents of both dataframes (CSV files) without the "Datetime" column
diff_df = pd.concat([df1, df2]).drop_duplicates(keep=False)

# Sort the indexes in the dataframe
diff_df = diff_df.sort_index()

# Display the differences in content between the two CSV files with sorted indexes
print("Differences between CSV files (sorted indexes):")
print(diff_df)

# Save the differences to a CSV file
csv_filename = "analysis_of_changes_" + df1_datetime + "_vs_" + df2_datetime + ".csv"
diff_df.to_csv(csv_filename, index=True)
print("Differences saved to:", csv_filename)

