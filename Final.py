from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.common.exceptions import NoSuchElementException
from constants import *

def get_text_or_nan(xpath):
    try:
        return driver.find_element(By.XPATH,xpath).text
    except NoSuchElementException:
        return "Nan"
        
# Path to WebDriver
driver = webdriver.Chrome()

# Starting URL (first page)
base_url = "https://www.avito.ma/fr/maroc/immobilier"
page_links = []
annonce_links = []
driver.get(base_url)

#prendre tous les liens des annances
for page_number in range(1,3):
    url = f"{base_url}?o={page_number}"
    driver.get(url)

    apartment_elements = driver.find_elements(By.XPATH, "//a[@class='sc-1jge648-0 eTbzNs']")
    for annonce in apartment_elements:
        link = annonce.get_attribute('href')
        annonce_links.append(link)

with open('link.txt','w',encoding="utf-8") as f:
    for i in annonce_links:
        f.write(i + "\n")
print("Page links saved to 'link.txt'.")

#scarper tous les anonnaces from link.txt

with open("property_details.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Location", "Surface", "Rooms", "Bathrooms", "Floor", "Construction Year"])

        for property_link in annonce_links:
            driver.get(property_link)
            time.sleep(2)
            title = get_text_or_nan(TITRE_XPATH)
            price = get_text_or_nan(PRIX_XPATH)
            location = get_text_or_nan(LOCATION_XPATH)
                # Optional fields, handle missing elements with try/except
                
            surface = get_text_or_nan(SURFACE_XPATH)               
            rooms = get_text_or_nan(CHAMBRE_XPATH)   
            bathrooms = get_text_or_nan(TOILET_XPATH)   
            floor = get_text_or_nan(ETAGE_XPATH)   
            construction_year = get_text_or_nan(DATEDECONSTRUCTION_XPATH)
                    
            # Write data row
            writer.writerow([title, price, location, surface, rooms, bathrooms, floor, construction_year])
            print(f"Details saved for listing: {title}")