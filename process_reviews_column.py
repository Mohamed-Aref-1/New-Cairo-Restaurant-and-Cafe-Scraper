#Removing the - sign from the reviews count column
import pandas as pd
import re
from google.colab import files


def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print the first few rows to manually inspect the data
    print("First few rows of the CSV file:")
    print(df.head())

    # Print the column names to understand the structure
    print("Columns available:", df.columns)

    # Prompt user to manually specify the column that contains the Reviews Count
    reviews_column = input("Please enter the column name that contains the Reviews Count: ")

    if reviews_column not in df.columns:
        print(f"Column '{reviews_column}' not found in the CSV file.")
        return

    # Remove parentheses and commas, then convert to integers
    df[reviews_column] = df[reviews_column].astype(str) \
        .str.replace(r'[(),]', '', regex=True) \
        .astype(int)


    # Save the cleaned and updated CSV
    cleaned_file_path = 'cleaned_' + file_path
    df.to_csv(cleaned_file_path, index=False)

    # Download the updated file
    files.download(cleaned_file_path)

# Example usage
uploaded = files.upload()
file_path = next(iter(uploaded))
process_csv(file_path)
