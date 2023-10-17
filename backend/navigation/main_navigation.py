import pyautogui
import time
import subprocess
import pyperclip

def open_new_tab_with_url(url):
    pyautogui.hotkey('ctrl', 't')  # Open a new tab
    time.sleep(1)  # Wait for the new tab to open
    pyautogui.hotkey('alt', 'd')  # Focus on the address bar
    time.sleep(1)  # Wait a bit for the address bar to be focused
    pyautogui.write(url)  # Type the URL
    pyautogui.press('enter')  # Navigate to the URL
    
def scroll_to_next_job():
    screen_width, screen_height = pyautogui.size()
    # Move the mouse to the center of the screen
    mouse_position = [screen_width / 2 - 200,  (screen_height / 2) - 250 ]
    pyautogui.moveTo(mouse_position[0], mouse_position[1])
    pyautogui.scroll(-150) 

def handle_application_apply():
    button_location = pyautogui.locateOnScreen("C:/Users/erict/Documents/ai-actor/backend/navigation/linkedIn/easy_apply.PNG", confidence=0.7)  # Adjust confidence if necessary
    print(button_location)

def navigate_single_job_collection_page():
    handle_application_apply()
    scroll_to_next_job()


# Open Microsoft Edge
subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
time.sleep(5)  # Give Edge a few seconds to launch

# Navigate to the LinkedIn URL using pyautogui
pyautogui.hotkey('alt', 'd')  # This shortcut selects the address bar in most browsers
time.sleep(0.5)  # Small delay to ensure address bar is selected

pyautogui.write("https://www.linkedin.com/jobs/search/?distance=25&f_I=12%2C4&f_WT=2%2C3%2C1&geoId=90000084&keywords=frontend%20developer&origin=JOB_SEARCH_PAGE_KEYWORD_HISTORY&refresh=true")
time.sleep(0.5)  # Small delay to ensure full URL is typed

pyautogui.press('enter')  # Pressing enter to navigate to the URL
time.sleep(3)
# pyautogui.hotkey('alt', 'd')
# pyautogui.hotkey('ctrl', 'c')
# paste_data = pyperclip.paste()
# print(paste_data)
navigate_single_job_collection_page()
 # This will scroll up by approximately 10 "notches" or "lines".


# for i in range (1,10):
#     url = paste_data + f"&start={i * 24}"
#     open_new_tab_with_url(url)
#     time.sleep(3)