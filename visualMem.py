from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

# Initialize a Selenium webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # You can change this to the appropriate driver for your browser
driver.get('https://humanbenchmark.com/tests/memory')

# remove speed limit of pyautogui
pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0

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
pyautogui.moveTo(950, 581)  # submit
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(858, 816)  # click on the test
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(951, 573)  # click start
pyautogui.leftClick()
time.sleep(1)

unrounded = 0
length = 0
arraySplit = []
width = 0
# Load the webpage
try:
    for i in range(0, 1000):
        buttonsToPress = []  # order of buttons to press

        # get the page source and the div where the buttons are
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        array = soup.find_all(class_='css-hvbk5q eut2yre0')

        try:
            arraySplit = str(array[0]).split("><")  # split up the divs
        except:
            time.sleep(10000)

        # get the size of the box in pixels
        box1 = arraySplit[2].split(" ")
        for j in range(0, len(box1)):
            if box1[j][0:-3].isdigit():
                # getting the number of boxes in a row
                unrounded = 395 / int(box1[j][0:-3])
                length = round(395 / int(box1[j][0:-3]))
                break

        # dealing with rounding error
        if length > 13:
            length -= 1

        if 16 < unrounded < 17:
            length += 1

        arrayCounter = 0
        for item in arraySplit:
            if arrayCounter == 0:
                temp = []
            if "active css-lxtdud eut2yre1" in item:  # if the box is lit up, append a 1
                temp.append(1)
                arrayCounter += 1
            elif "css-lxtdud eut2yre1" in item:  # if not, append a 0
                temp.append(0)
                arrayCounter += 1

            if arrayCounter == length:
                buttonsToPress.append(temp)  # add the items to numberOrder
                arrayCounter = 0

        midpoint = 390 / (length * 2)  # midpoint of the squares
        time.sleep(1.5)

        # go through the array, if there is a 1, press the corresponding button
        for j in range(0, length):
            for k in range(0, length):
                if buttonsToPress[j][k] == 1:
                    pyautogui.leftClick(755 + midpoint + k * 395 / (length * 1.013),
                                        275 + midpoint + j * 395 / (length * 1.013))

        time.sleep(2)
except:
    time.sleep(10000)
time.sleep(10000)



