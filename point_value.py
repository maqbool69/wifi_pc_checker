import pyautogui
from PIL import Image
import easyocr
import time
# Take a screenshot of the current screen
# screenshot = pyautogui.screenshot()
pyautogui.hotkey('win', '3')
time.sleep(3)
pyautogui.hotkey('win', '2')
# # Save the screenshot as an image file
# screenshot.save("screenshot.png")

# Use easyocr to extract text from the image
reader = easyocr.Reader(['en'])  # You can specify the language(s) you want to use
results = reader.readtext("screenshot.png")

# Function to extract integers from a string
def extract_integers(text):
    integers = []
    for word in text.split():
        try:
            integer = int(word)
            integers.append(integer)
        except ValueError:
            pass
    return integers

# Extract the first three integers
detected_text = ' '.join([result[1] for result in results])
integers = extract_integers(detected_text)[:5]

if len(integers) < 3:
    print("Value is: {first_value} \nNot enough integers detected in the screenshot.")
else:
    first_value = integers[3]
    if first_value >= 200:
        # Simulate key presses for "X" twice and "Y" twice
        pyautogui.press('x', presses=2)
        pyautogui.press('y', presses=2)
        print(f"Value is: {first_value} \nPressed 'X' twice and 'Y' twice because first value ({first_value}) is greater than or equal to 200.")
