#remove ROWS WITH Missing valueS from THE CSV
import pandas as pd
from google.colab import files

def remove_missing_values(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print the first few rows to manually inspect the data
    print("First few rows of the CSV file:")
    print(df.head())

    # Print the column names to understand the structure
    print("Columns available:", df.columns)

    # Drop rows with any missing values
    df_cleaned = df.dropna()

    # Check if any rows were removed
    rows_removed = len(df) - len(df_cleaned)
    if rows_removed > 0:
        print(f"Removed {rows_removed} rows with missing values.")
    else:
        print("No rows with missing values found.")

    # Save the cleaned CSV file
    cleaned_file_path = 'cleaned_' + file_path
    df_cleaned.to_csv(cleaned_file_path, index=False)

    # Download the cleaned file
    files.download(cleaned_file_path)

# Example usage
uploaded = files.upload()
file_path = next(iter(uploaded.keys()))
remove_missing_values(file_path)
