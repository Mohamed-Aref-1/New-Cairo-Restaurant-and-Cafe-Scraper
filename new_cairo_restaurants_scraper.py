import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to Google Maps New Cairo
driver.get("https://www.google.com/maps")

# Search for Restaurants and Cafes in New Cairo
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys("Restaurants and Cafes in New Cairo")
search_box.send_keys(Keys.ENTER)

# Wait for results to load
time.sleep(5)

# Scroll to load more results
for _ in range(20):  # Increase range if you need more data
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

# Extract restaurant data
restaurants = driver.find_elements(By.CSS_SELECTOR, ".Nv2PK")

data = []

for restaurant in restaurants:
    try:
        name = restaurant.find_element(By.CSS_SELECTOR, ".qBF1Pd span").text
    except:
        name = "N/A"

    try:
        rating = restaurant.find_element(By.CSS_SELECTOR, ".MW4etd").text
    except:
        rating = "N/A"

    try:
        reviews = restaurant.find_element(By.CSS_SELECTOR, ".UY7F9").text
    except:
        reviews = "N/A"

    try:
        location = restaurant.find_element(By.CSS_SELECTOR, ".AiV6rd").get_attribute("data-url")
        location = location.split("!3d")[1].split("!4d")
        latitude = location[0]
        longitude = location[1]
    except:
        latitude, longitude = "N/A", "N/A"

    try:
        url = restaurant.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    except:
        url = "N/A"

    data.append([name, rating, reviews, latitude, longitude, url])

# Close the WebDriver
driver.quit()

# Save data to CSV
csv_file = "new_cairo_restaurants_and_cafes.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Restaurant Name", "Star Rating", "Reviews Count", "Latitude", "Longitude", "URL"])
    writer.writerows(data)

print(f"Data saved to {csv_file}")
