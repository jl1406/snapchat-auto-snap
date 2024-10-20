
# Snapchat Automation Script

This project uses Python, OpenCV, and PyAutoGUI to automate interactions with Snapchat's desktop interface by locating specific elements on the screen and simulating mouse movements and clicks. The script captures screenshots, searches for predefined images on the screen, and interacts with them automatically.

Features
--------
- Image Recognition: Uses OpenCV to find specific UI elements on the screen.
- Automated Mouse Control: Moves the mouse to the identified element and clicks it.
- Scheduling: The script runs on a schedule and performs tasks at regular intervals.
- Customizable Image Paths: You can easily update the paths to the images you want to locate on the screen.
- Run Count Control: Automatically stops after a set number of runs (7 in the current setup).

Requirements
------------
Ensure you have the following Python packages installed:
```
pip install pyautogui opencv-python pillow pyscreeze mouseinfo pygetwindow schedule
```
Usage
-----
1. Clone the repository:

   ```
   git clone https://github.com/yourusername/snapchat-automation.git
   ```

2. Update the image paths in the script to match the location of the UI element images on your machine.

3. Run the script:
   ```
   python automation_script.py
   ```
The script will take screenshots, search for the specified images, and perform the corresponding actions.

Configuration
-------------
- Screenshot Path: Change the screenshot_path variable in the script to define where screenshots should be saved.
- Image Paths: Update the image_paths list with paths to the images you want to match.
- Run Interval: The current script is set to run every 23 hours. Adjust the time.sleep() duration in the while True loop to change the interval.

Limitations
-----------
- The script relies on static images to find UI elements. If the UI changes significantly, the script may fail to recognize elements.
- PyAutoGUI's mouse movement is screen resolution-dependent. Ensure you run this on the correct screen setup.

