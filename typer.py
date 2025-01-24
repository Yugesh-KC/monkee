import pyautogui
import keyboard

def type_keystrokes(input_string, typing_speed=0):       
    ''' this function types the input string and returns true but if esc is prssed it breaks and returns false'''
    
    for char in input_string:
        
        if keyboard.is_pressed('Esc'):
            print('breaking')
            return False
        pyautogui.typewrite(char)

    return True