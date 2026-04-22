# Import Selenium's main webdriver module to control the browser
from selenium import webdriver

# Import 'By' so we can locate elements using ID, XPATH, CLASS_NAME, etc.
from selenium.webdriver.common.by import By

# Import Service to manage how ChromeDriver will run
from selenium.webdriver.chrome.service import Service

# Import ChromeDriverManager to automatically download/update ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager


# Create a Service object using the ChromeDriver downloaded by ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Launch the Chrome browser using the service object
driver = webdriver.Chrome(service=service)
driver.get("https://www.wikipedia.org/")


# Type text in search box
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Selenium (software)")

input("Search text entered! Open Chrome and SEE the text. Press Enter to continue...")

# Click search button AFTER you see it
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

print("New Page Title:", driver.title)

# Close browser

