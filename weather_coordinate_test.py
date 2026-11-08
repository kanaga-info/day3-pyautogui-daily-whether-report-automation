
import pyautogui
import time
from datetime import datetime

# ==========================================
# INITIAL SETTINGS
# ==========================================

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# Get today's date and time
today = datetime.now()

date_time = today.strftime("%Y-%m-%d %H:%M:%S")
date_filename = today.strftime("%Y-%m-%d")

# Screen information
screen_width, screen_height = pyautogui.size()

print("Screen Width:", screen_width)
print("Screen Height:", screen_height)

print("\nDaily Weather Report Automation Started")


# ==========================================
# STEP 1: OPEN CHROME
# ==========================================

print("\nStep 1: Opening Google Chrome")

pyautogui.hotkey('command', 'space')

time.sleep(1)

pyautogui.write('chrome', interval=0.1)
time.sleep(1)

pyautogui.press('enter')
time.sleep(5)

# Open new tab
pyautogui.hotkey('command', 't')
time.sleep(1)

# Open AccuWeather
pyautogui.write(
    'https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671',
    interval=0.02
)

pyautogui.press('enter')

# Wait for website to load
time.sleep(12)


# ==========================================
# STEP 2: COPY WEATHER USING MOUSE
# ==========================================

print("\nStep 2: Copying Chennai Weather Information")

print("Make sure the Chennai temperature is visible.")

input("Press ENTER when the weather information is ready...")

# Previously captured coordinates from your MacBook
start_x = 555
start_y = 216

end_x = 724
end_y = 213

# Select the horizontal weather text
pyautogui.moveTo(
    start_x,
    start_y,
    duration=1
)

pyautogui.mouseDown()

pyautogui.moveTo(
    end_x,
    end_y,
    duration=2
)

pyautogui.mouseUp()

time.sleep(1)

# Copy selected weather information
pyautogui.hotkey('command', 'c')

time.sleep(2)

print("Weather information copied!")


# ==========================================
# STEP 3: OPEN MICROSOFT EXCEL
# ==========================================

print("\nStep 3: Opening Microsoft Excel")

pyautogui.hotkey('command', 'space')
time.sleep(1)

pyautogui.write('Microsoft Excel', interval=0.1)
time.sleep(2)

pyautogui.press('enter')
time.sleep(8)

# Create a new workbook
pyautogui.hotkey('command', 'n')
time.sleep(5)


# ==========================================
# STEP 4: CREATE EXCEL HEADERS
# ==========================================

print("\nStep 4: Creating Excel Report")

# Enter first column heading
pyautogui.write('Date & Time')

pyautogui.press('tab')

# Enter second column heading
pyautogui.write('Fetched Data')

pyautogui.press('tab')

# Enter third column heading
pyautogui.write('Comment')

# Move to next row, first column
pyautogui.press('enter')

# ==========================================
# STEP 5: INSERT DATE AND TIME
# ==========================================

print("\nStep 5: Entering Date and Time")

pyautogui.write(date_time, interval=0.05)

# Move to second column
pyautogui.press('tab')


# ==========================================
# STEP 6: PASTE FETCHED WEATHER DATA
# ==========================================

print("\nStep 6: Pasting Weather Information")

# Paste previously copied weather text
pyautogui.hotkey('command', 'v')

time.sleep(2)

# Move to third column
pyautogui.press('tab')


# ==========================================
# STEP 7: ENTER SHORT COMMENT
# ==========================================

print("\nStep 7: Entering Weather Comment")

pyautogui.write(
    'Warm weather in Chennai. Stay hydrated.',
    interval=0.05
)


# ==========================================
# STEP 8: FORMAT EXCEL SHEET
# ==========================================

print("\nStep 8: Formatting Excel Sheet")

# Select all used cells
pyautogui.hotkey('command', 'a')

# Auto-fit columns using Excel shortcut
pyautogui.hotkey('option', 'h')
pyautogui.press('o')
pyautogui.press('i')

time.sleep(2)


# ==========================================
# STEP 9: SAVE EXCEL FILE
# ==========================================

print("\nStep 9: Saving Excel Report")

file_name = f"daily_report_{date_filename}.xlsx"

pyautogui.hotkey('command', 's')

time.sleep(3)

# Enter the filename in the Save dialog
pyautogui.write(file_name, interval=0.05)

time.sleep(1)

pyautogui.press('enter')

time.sleep(4)

print("Excel file save command completed.")
print("File name:", file_name)


# ==========================================
# STEP 10: TAKE SCREENSHOT
# ==========================================

print("\nStep 10: Taking Screenshot of Excel")

# Make sure Excel is visible
pyautogui.hotkey('command', 'tab')

time.sleep(3)

# macOS native full-screen screenshot
# Screenshot will be saved to Desktop

pyautogui.hotkey('command', 'shift', '3')

time.sleep(3)

print("Screenshot captured!")
print("Check your Mac Desktop for the screenshot.")


# ==========================================
# AUTOMATION COMPLETED
# ==========================================

print("\n======================================")
print("DAILY WEATHER REPORT COMPLETED")
print("======================================")

print("Date and Time:", date_time)
print("Weather Data: Chennai temperature")
print("Excel File:", file_name)
print("Screenshot: Saved on Desktop")

print("\nAutomation Successfully Completed!")
