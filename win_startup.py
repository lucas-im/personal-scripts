import win32gui, pyautogui, time, win32con

time.sleep(2)
window = win32gui.FindWindow(None, 'Inbox - lucas.1m@icloud.com - Outlook')
win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
time.sleep(6)
win32gui.ShowWindow(window, win32con.SW_NORMAL)
win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
#pyautogui.keyDown('winleft')
#pyautogui.press('space')
#pyautogui.keyUp('winleft')