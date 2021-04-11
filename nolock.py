import pyautogui
import time


def no_lock(button):
    try:
        print("Press CTRL+C to stop.")
        while True:
            pyautogui.press(button)  # Key pressed
            time.sleep(2)
            pyautogui.press(button)  # Key released
            time.sleep(3)

    except Exception as ex:
        print({"no_lock": ex})