import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (make sure to specify the path to your WebDriver if it's not in your PATH)
driver = webdriver.Firefox()

# List to store the quotes
quotes_data = []

try:
    # Navigate to the quotes website
    driver.get('http://quotes.toscrape.com/js/')
    
    # Wait until the quotes are loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'quote'))
    )
    
    # Extract the quotes
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]
        
        # Append the quote data to the list
        quotes_data.append({
            'text': text,
            'author': author,
            'tags': tags
        })

finally:
    # Close the browser
    driver.quit()

# Write the data to a JSON file
with open('quotes.json', 'w') as f:
    json.dump(quotes_data, f, indent=4)

print("Data saved to quotes.json")
