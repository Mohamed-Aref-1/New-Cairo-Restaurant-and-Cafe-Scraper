#Calculating the cordinates
import pandas as pd
import re
from google.colab import files

def extract_coordinates(url):
    # Regular expression to match the coordinates in the URL
    pattern = r'@(-?\d+\.\d+),(-?\d+\.\d+)'
    match = re.search(pattern, url)

    if match:
        lat, lon = match.groups()
        return float(lat), float(lon)
    else:
        # Fallback pattern for URLs that use "3d" and "4d"
        pattern_fallback = r'3d(-?\d+\.\d+)!4d(-?\d+\.\d+)'
        match_fallback = re.search(pattern_fallback, url)

        if match_fallback:
            lat, lon = match_fallback.groups()
            return float(lat), float(lon)
        else:
            return None

def add_coordinates_to_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Extract coordinates and create a new column
    df['Coordinates'] = df['URL'].apply(lambda x: extract_coordinates(x) if pd.notnull(x) else None)

    # Save the updated CSV
    df.to_csv(file_path, index=False)
    # Download the updated file
    files.download(file_path)

# Example usage
uploaded = files.upload()
file_path = next(iter(uploaded))
add_coordinates_to_csv(file_path)