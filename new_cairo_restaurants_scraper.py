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

try:
    # Navigate to Google Maps
    driver.get("https://www.google.com/maps")

    # Wait for the search box to load and perform the search
    time.sleep(3)  # Simple wait for elements to load
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
        name = restaurant.find_element(By.CSS_SELECTOR, ".qBF1Pd span").text if restaurant.find_elements(By.CSS_SELECTOR, ".qBF1Pd span") else "N/A"
        rating = restaurant.find_element(By.CSS_SELECTOR, ".MW4etd").text if restaurant.find_elements(By.CSS_SELECTOR, ".MW4etd") else "N/A"
        reviews = restaurant.find_element(By.CSS_SELECTOR, ".UY7F9").text if restaurant.find_elements(By.CSS_SELECTOR, ".UY7F9") else "N/A"
        url = restaurant.find_element(By.CSS_SELECTOR, "a").get_attribute("href") if restaurant.find_elements(By.CSS_SELECTOR, "a") else "N/A"

        # Location might not always be in a consistent format
        location_data = restaurant.find_element(By.CSS_SELECTOR, ".AiV6rd").get_attribute("data-url") if restaurant.find_elements(By.CSS_SELECTOR, ".AiV6rd") else None
        if location_data:
            location_parts = location_data.split("!3d")
            if len(location_parts) > 1:
                lat_lon = location_parts[1].split("!4d")
                latitude = lat_lon[0] if len(lat_lon) > 0 else "N/A"
                longitude = lat_lon[1] if len(lat_lon) > 1 else "N/A"
            else:
                latitude, longitude = "N/A", "N/A"
        else:
            latitude, longitude = "N/A", "N/A"

        data.append([name, rating, reviews, latitude, longitude, url])

finally:
    # Close the WebDriver
    driver.quit()

# Save data to CSV
csv_file = "new_cairo_restaurants_and_cafes.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Restaurant Name", "Star Rating", "Reviews Count", "Latitude", "Longitude", "URL"])
    writer.writerows(data)

print(f"Data saved to {csv_file}")


