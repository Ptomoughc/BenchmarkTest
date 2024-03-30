from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

# Initialize a Selenium webdriver
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/aim')

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
pyautogui.moveTo(818, 585)  # submit
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(865, 872)  # click on the test
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(951, 620)  # start the test
pyautogui.leftClick()
count = 0
interation1 = False

# color of the target
color = (149, 195, 232)

while True:
    # get page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    div_with_matrix3d = None
    for div in soup.find_all('div'):
        # coordinates of the target is in the style sheet of the target: get the coordinates
        if 'style' in div.attrs and 'matrix3d' in div['style']:
            count += 1
            pointer = str(div).split(", ")
            pyautogui.leftClick(float(pointer[12]) + 467, float(pointer[13]) + 225)  # press at those coordinates
            print(count)
            break

    if count == 31 or (count == 30 and interation1):  # after you press 30 targets
        interation1 = True
        # get page info
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        incomplete_elements1 = soup.find_all(class_='css-0')
        element = incomplete_elements1[0].text
        # if score is more than 10
        if int(element[:-2]) >= 9:
            pyautogui.moveTo(1040, 606)  # restart test
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(951, 438)  # start test
            pyautogui.leftClick()
        else:
            # save score
            pyautogui.moveTo(877, 623)
            pyautogui.leftClick()
            time.sleep(100000)
        count = 0
