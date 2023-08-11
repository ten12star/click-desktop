import pyautogui
import time

# set the interval in 6 seconds
interval = 15
count = 0
# move the mouse cursor to a specific position (x, y)
pyautogui.moveTo(90, 60)

# perform multiple clicks with the specified interval
for i in range(99999):
    pyautogui.click()
    count = count + 1
    # print(count, "clicked!")
    time.sleep(interval)
 