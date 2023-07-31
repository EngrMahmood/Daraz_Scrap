import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL of the page you want to scrape
url = "https://www.daraz.pk/"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# Access the HTML content
html_content = response.text

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find the elements containing the grand item names
grand_item_elements = soup.find_all("li", class_="lzd-site-menu-grand-item")

# Extract the grand item names (excluding empty values)
grand_item_names = [element.text for element in grand_item_elements if element.text.strip()]

# Create a DataFrame with the grand item names
df = pd.DataFrame({"Grand Item": grand_item_names})

# Save the DataFrame to an Excel file
excel_file = "mahmood.xlsx"
df.to_excel(excel_file, index=False)

print(f"Table data saved to '{excel_file}' file.")
