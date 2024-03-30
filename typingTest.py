from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

# remove speed limit of pyautogui
pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0

# Initialize a Selenium webdriver
driver = webdriver.Chrome()

# Load the webpage
driver.get('https://humanbenchmark.com/tests/typing')

time.sleep(2)
pyautogui.moveTo(882, 27)  # full-screen
pyautogui.leftClick()
time.sleep(0.5)
pyautogui.moveTo(1080, 800)  # close cookie tabs
pyautogui.leftClick()
time.sleep(0.5)
pyautogui.moveTo(1400, 146)  # press login
pyautogui.leftClick()
time.sleep(0.5)
pyautogui.moveTo(818, 440)  # press username
pyautogui.leftClick()
pyautogui.typewrite("username")  # enter username
time.sleep(0.5)
pyautogui.moveTo(818, 520)  # press password
pyautogui.leftClick()
pyautogui.typewrite("password")  # enter password
pyautogui.moveTo(818, 585)  # submit
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(865, 644)  # click on the test
pyautogui.leftClick()
time.sleep(1)

# Get the page source after it's fully loaded (including dynamically generated content)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Get all the characters
incomplete_elements = soup.find_all(class_='incomplete')

elements = []

# add the characters to the array
for element in incomplete_elements:
    if element.text is not None:
        elements.append(element.text)

# type out the text
textToType = ''.join(elements)
time.sleep(0.1)
pyautogui.typewrite(textToType)

time.sleep(500)
driver.quit()
