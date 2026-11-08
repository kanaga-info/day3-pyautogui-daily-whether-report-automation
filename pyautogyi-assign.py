import pyautogui
import pyperclip
import time
import os
from datetime import datetime    

pyautogui.FAILSAFE=True
pyautogui.PAUSE=0.5

# Automatically generate current date and time
today = datetime.now()

date_time = today.strftime("%Y-%m-%d %H:%M:%S")
date_filename = today.strftime("%Y-%m-%d")

# File names
excel_filename = f"daily_report_{date_filename}.xlsx"

# Save files in Desktop
desktop_path = os.path.expanduser("~/Desktop")

desktop_path = os.path.expanduser("~/Desktop")

excel_path = os.path.join(desktop_path, excel_filename)

print("======================================")
print("DAILY WEATHER REPORT AUTOMATION")
print("======================================")

print("Screen Size:", pyautogui.size())
print("Date & Time:", date_time)

# Step1 : Open Chrome Browser

print ("Step1: Open the chrome browser")

pyautogui.hotkey('command','space',interval=0.1)
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('command','t',interval=0.1)
time.sleep(1)
pyautogui.write('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)


# Step2: Copy only today's weather information

print("Step2: Copy today's weather information")

# Your previously tested MacBook coordinates
start_x = 555
start_y = 216

end_x = 724
end_y = 213

# Select weather text using mouse
pyautogui.moveTo(start_x, start_y, duration=1)

pyautogui.mouseDown()

pyautogui.moveTo(end_x, end_y, duration=2)

pyautogui.mouseUp()

time.sleep(1)

# Copy selected information
pyautogui.hotkey('command', 'c')

time.sleep(2)

weather_report = pyperclip.paste()

if not weather_report.strip():
    print("ERROR: No weather information copied.")
    print("Check your mouse coordinates.")
    raise SystemExit

print("\nFetched Weather Information:")
print(weather_report)


#Step3: Open the excel Sheet
print("\nStep3:Open the excel sheet")
pyautogui.hotkey('command','space',interval=0.1)
time.sleep(1)
pyautogui.write('Microsoft Excel',interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)


# STEP4: Create a excel file

print("\nStep 4: Creating New Excel Workbook")

pyautogui.hotkey('command', 'n')
time.sleep(4)


#STEP5: CREATE COLUMN HEADINGS

print("\nStep 5: Creating Excel Headings")

pyautogui.write('Date & Time')
pyautogui.press('tab')

pyautogui.write('Fetched Data')
pyautogui.press('tab')

pyautogui.write('Comment')
pyautogui.press('enter')



#STEP6: Insert Automatic Date & Time , Fetched Whether and Comment

print("\n Inserting Current Date and Time")
pyautogui.write(date_time, interval=0.05)
pyautogui.press('tab')

print("\n: Inserting Weather Information")
pyautogui.hotkey('fn', 'f2')
pyautogui.hotkey('command', 'v')
time.sleep(2)
pyautogui.press('tab')

print("\n: Adding Weather Comment")
comment = "Warm weather in Chennai. Stay hydrated."
pyautogui.write(comment, interval=0.05)


#Step7: Save Excel

print("\nStep7: Saving Excel Workbook")
pyautogui.hotkey('command', 'shift', 's')
time.sleep(3)


# Enter complete save path

pyautogui.write("daily_report_2026", interval=0.02)
time.sleep(1)
pyautogui.press('enter')
time.sleep(4)

print("Excel file save requested:")
print(excel_path)


#Step10: TAKE SCREENSHOT

print("\n Taking screenshot")

pyautogui.hotkey('command', 'tab')
time.sleep(3)

#Save screenshot directly using macOS shortcut
pyautogui.hotkey('command', 'shift', '3')
time.sleep(3)
print("Screenshot captured on Desktop.")


# ==========================================
# FINAL STATUS
# ==========================================

print("\n======================================")
print("DAILY REPORT AUTOMATION COMPLETED")
print("======================================")

print("Date & Time:", date_time)
print("Weather Data:", weather_report)
print("Excel Filename:", excel_filename)
print("Excel Location:", excel_path)
print("Screenshot Location:", desktop_path)

print("\nAll automation steps completed!")
