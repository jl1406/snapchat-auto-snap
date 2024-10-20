import os
import cv2
import pyautogui
import time
import schedule
import sys

# Global variable to count the number of runs
run_count = 0

def find_image(image_path, screenshot_path):
    os.makedirs(screenshot_path, exist_ok=True)

    screenshot_file = os.path.join(screenshot_path, 'screenshot.png')
    
    pyautogui.screenshot(screenshot_file)
    screenshot = cv2.imread(screenshot_file)

    template = cv2.imread(image_path)
    template_height, template_width, _ = template.shape

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    return max_loc, template_width, template_height

def move_mouse_to_center_and_click(image_location, template_width, template_height):
    center_x = image_location[0] + (template_width // 2)
    center_y = image_location[1] + (template_height // 2)
    
    pyautogui.moveTo(center_x, center_y)
    time.sleep(1)  # Wait for 1 second
    pyautogui.click()  # Click the left mouse button
    time.sleep(2)  # Wait for 2 seconds

def job():
    global run_count
    screenshot_path = r"D:\Users\new\Desktop\snapchat\screenshots"  # Change this to your desired path
    
    image_paths = [
         r"D:\Users\new\Desktop\snapchat\camer.png",
         r"D:\Users\new\Desktop\snapchat\pic_button.png",
         r"D:\Users\new\Desktop\snapchat\sendto.png",
         r"D:\Users\new\Desktop\snapchat\myai.png",
         # r"D:\Users\new\Desktop\snapchat\me.png",  # Uncomment this line
         # r"D:\Users\new\Desktop\snapchat\sent.png",
    ]
    for image_path in image_paths:
        image_location, template_width, template_height = find_image(image_path, screenshot_path)

        if image_location:
            print(f"Image found at X: {image_location[0]}, Y: {image_location[1]}")
            move_mouse_to_center_and_click(image_location, template_width, template_height)
        else:
            print(f"Image '{image_path}' not found on the screen.")
            pyautogui.moveTo(0, 0)

    run_count += 1
    print(f"Run Count: {run_count}")
    
    if run_count >= 3:
        # Exit the script after 3 runs
        sys.exit()

# Run the job immediately and then wait for 10 seconds before running it again
while True:
    job()
    time.sleep(30)  # Sleep for 10 seconds before the next run