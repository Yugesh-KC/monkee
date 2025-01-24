#RUN THE CODE AND SWITCH TO THE MONKEY TYPE TAB 
#IT IS RECOMMENDED TO CHANGE THE CARRET STYLE TO NONE SO THAT THE CURSOR WON'T INTERFERE WITH THE OCR
#PRESS ESC TO EXIT AFTER COMPLETION

from typer import type_keystrokes
from capture_text import ocr_from_screenshot
import time

REGION_INITIAL = (145, 415, 1596, 60)    #change this to the coordinates and width/height  of the monkeytype typing region
REGION_MIDDLE =  (145,480,1596,60)      #change this to the coordinates and width/height of the middle line only
INITIAL_DELAY = 5                     #for navigating to the website
counter = 0 

time.sleep(INITIAL_DELAY)     
text = ocr_from_screenshot(REGION_INITIAL)
not_exit=type_keystrokes(text)
print('typed initail',text)
    
while not_exit:
    counter+=1
    type_keystrokes(' ') 
    new_text = ocr_from_screenshot(REGION_MIDDLE)
    print('typed space')
    print('new text',new_text)
    
    continue_loop= type_keystrokes(new_text)
    if not continue_loop:
        break

   
