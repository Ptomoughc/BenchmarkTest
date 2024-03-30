from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

# remove speed limit of pyautogui
pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0

# Initialize a Selenium webdriver
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/verbal-memory')

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
pyautogui.moveTo(864, 700)  # click on the test
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(951, 620)  # start the test
pyautogui.leftClick()

array = []

# Load the webpage
for i in range(1, 1000000):
    # Get the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    incomplete_elements1 = soup.find_all(class_='word')

    try:
        element = incomplete_elements1[0].text
    except:
        # gives you time to explore the page once it has finished running
        time.sleep(10000)

    # if the word has already been found
    if element in array:
        pyautogui.moveTo(910, 538)  # press seen
        pyautogui.leftClick()
    else:
        pyautogui.moveTo(1035, 538)  # press new
        pyautogui.leftClick()
        array.append(element)  # add the new word to the array
