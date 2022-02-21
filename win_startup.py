import win32gui, pyautogui, time, win32con

for i in range(3):
    window = win32gui.FindWindow(None, 'Inbox - <EMAIL> - Outlook')
    res = win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
    print(res)
    if res == 0:
        time.sleep(2.5)
    else:
        pyautogui.keyDown('winleft')
        pyautogui.press('space')
        pyautogui.keyUp('winleft')
        break
