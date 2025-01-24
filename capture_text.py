import pyautogui
import pytesseract
from PIL import Image
import time

def ocr_from_screenshot(region=None,path=None):
    try:
        screenshot = pyautogui.screenshot(region=region)
        if path:
            screenshot.save(path)

        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(screenshot)

        return extracted_text
    except Exception as e:
        return f"Error occurred: {e}"
    

# print(ocr_from_screenshot(REGION_MIDDLE))





    