import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.discogs.com/search/?ev=em_rs&type=label"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(url)

# Wait for the page to load completely
sleep(5)  # Adjust the sleep time as needed

# Find song titles and artist names
# songs = driver.find_elements(By.CLASS_NAME, 'card-release-title')
# artists = driver.find_elements(By.CLASS_NAME, 'card-artist-name')
artist = driver.find_elements(By.CLASS_NAME, 'search_result_title')

# Prepare CSV file
with open('discogs_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Song', 'Artist'])  # Write headers

    # Write song titles and artist names to the CSV file
    # for i in range(len(songs)):
    #     writer.writerow([songs[i].text, artists[i].text])
    for i in range(len(artist)):
        writer.writerow([artist[i].text])

# Close the browser
driver.quit()


