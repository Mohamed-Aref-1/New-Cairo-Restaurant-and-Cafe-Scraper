#Handling non latin letters
import pandas as pd
import re # regular expression operations.
from google.colab import files # to upload

def contains_non_latin(text):
    # Regular expression to detect non-Latin characters
    pattern = re.compile(r'[^\x00-\x7F]+')
    return bool(pattern.search(text))

def clean_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print the first few rows to manually inspect the data
    print("First few rows of the CSV file:")
    print(df.head())

    # Print the column names to understand the structure
    print("Columns available:", df.columns)

    # Prompt user to manually specify the column that contains restaurant names
    name_column = input("Please enter the column name that contains restaurant names: ")

    if name_column not in df.columns:
        print(f"Column '{name_column}' not found in the CSV file.")
        return

    # Filter out rows with non-Latin characters in the restaurant name
    df_cleaned = df[~df[name_column].apply(lambda x: contains_non_latin(str(x)))]

    # Check if any rows were removed
    rows_removed = len(df) - len(df_cleaned)
    if rows_removed > 0:
        print(f"Removed {rows_removed} rows with non-Latin characters.")
    else:
        print("No rows with non-Latin characters found.")

    # Save the cleaned CSV
    cleaned_file_path = 'cleaned_' + file_path
    df_cleaned.to_csv(cleaned_file_path, index=False)

    # Download the cleaned file
    files.download(cleaned_file_path)

# Example usage
uploaded = files.upload()
file_path = next(iter(uploaded.keys()))
clean_csv(file_path)
