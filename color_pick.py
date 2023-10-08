import pyautogui

import time

# Define the coordinates of the pixel to check
x_coord = 541





y_coord = 362  # Replace with your desired y-coordinate


# Function to check the pixel color
def check_pixel_color(x, y):
    pixel_color = pyautogui.pixel(x, y)
    
    
    # Assuming golden color is (255, 215, 0) and green color is (0, 255, 0)
    if pixel_color == (29,180,10):
    
        print("Less than 100, pressed x and y 2 times")
    else:
        print("Greater than 100")
        pyautogui.press(['x', 'x', 'y', 'y'])

while True:
    check_pixel_color(x_coord, y_coord)
    time.sleep(1)
