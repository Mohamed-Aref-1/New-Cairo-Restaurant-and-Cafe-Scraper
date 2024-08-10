# New-Cairo-Restaurant-and-Cafe-Scraper

## Overview

This project includes a collection of scripts for web scraping, data extraction, and cleaning. The main functionalities are to scrape restaurant and cafe data from Google Maps, clean CSV files by removing non-Latin characters and missing values, and process reviews count columns.

## Project Components

### Web Scraping

- **`new_cairo_restaurants_scraper.py`**:
  - Scrapes restaurant and cafe data from Google Maps for New Cairo.
  - Extracts restaurant names, ratings, reviews count, and coordinates.
  - Saves the extracted data to a CSV file.

### Data Cleaning

- **`remove_non_latin_characters.py`**:
  - Filters out rows with non-Latin characters from a specified column in a CSV file.
  - Allows user to specify the column to be cleaned.

- **`remove_missing_values.py`**:
  - Removes rows with missing values from a CSV file.
  - Saves and downloads the cleaned CSV file.

- **`add_coordinates_to_csv.py`**:
  - Extracts latitude and longitude from URLs in a CSV file and adds them as new columns.
  - Saves and downloads the updated CSV file.

- **`remove_negative_sign_reviews.py`**:
  - Removes the '-' sign from the reviews count column in a CSV file and converts values to integers.
  - Saves and downloads the cleaned CSV file.

## Installation

### Clone the Repository

```sh
git clone https://github.com/your-username/web-scraping-data-cleaning.git
```
### Set Up the Environment

1. Ensure you have Python installed on your system.
2. Install the required Python libraries:
    ```sh
    pip install pandas selenium webdriver-manager google-colab
    ```

### Web Scraping

- To run the web scraping script:
    ```sh
    python new_cairo_restaurants_scraper.py
    ```

### Data Cleaning

- To clean CSV files using the data cleaning scripts, upload your CSV file when prompted.

## Usage

### Web Scraping

- Run `new_cairo_restaurants_scraper.py` to scrape data and save it to a CSV file.

### Data Cleaning

- **Remove Non-Latin Characters**: Use `remove_non_latin_characters.py` to clean rows with non-Latin characters.
- **Remove Missing Values**: Use `remove_missing_values.py` to remove rows with missing values.
- **Add Coordinates**: Use `add_coordinates_to_csv.py` to add latitude and longitude to your CSV.
- **Remove Negative Signs**: Use `remove_negative_sign_reviews.py` to clean the reviews count column.

## Files

- **`new_cairo_restaurants_scraper.py`**:
  - Scrapes data from Google Maps and saves it to a CSV file.
  
- **`remove_non_latin_characters.py`**:
  - Cleans rows with non-Latin characters from a specified column in a CSV file.
  
- **`remove_missing_values.py`**:
  - Removes rows with missing values from a CSV file.
  
- **`add_coordinates_to_csv.py`**:
  - Extracts and adds coordinates to a CSV file based on URLs.
  
- **`remove_negative_sign_reviews.py`**:
  - Processes the reviews count column by removing '-' signs and converting values to integers.
 
## Requirements
    ```sh pandas
selenium
webdriver-manager
google-colab    ```

## Contributing

Feel free to contribute by submitting issues or pull requests. Ensure that your changes are well-tested and adhere to the project's coding guidelines.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).


