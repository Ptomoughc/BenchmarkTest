from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

# Initialize a Selenium webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # You can change this to the appropriate driver for your browser
driver.get('https://humanbenchmark.com/tests/number-memory')

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
pyautogui.moveTo(865, 759)  # click on the test
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(951, 620)  # start the test
pyautogui.leftClick()

# Load the webpage
for i in range(1, 1000):
    # Get the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Get the number on the screen
    incomplete_elements1 = soup.find_all(class_='big-number')
    incomplete_elements2 = soup.find_all(class_='big-number ')

    elements = []

    # add the number to the array
    for element in incomplete_elements1:
        if element.text is not None:
            elements.append(element.text)

    for element in incomplete_elements2:
        if element.text is not None:
            elements.append(element.text)

    # wait for the number to disappear
    time.sleep((.8*i)+0.8)

    # type the number
    textToType = ''.join(elements)
    pyautogui.typewrite(textToType)
    pyautogui.moveTo(963, 555)  # click submit
    pyautogui.leftClick()
    time.sleep(1.5)
    pyautogui.moveTo(963, 609)  # click next
    pyautogui.leftClick()

time.sleep(1000)
