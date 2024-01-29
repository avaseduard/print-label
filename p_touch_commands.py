import pyautogui
import time
# 
def limit_string(input_string):
    # If string is shorther than 75 chars, return as it is
    if len(input_string) <= 74:
        return input_string
    # If the last character is a space, cut there
    if input_string[74] == ' ':
        return input_string[0:74]
    # If the last character isn't a space, find the last space and cut there
    last_space_index = input_string.rfind(' ', 0, 74)
    if last_space_index != -1:
        return input_string[:last_space_index]
    # If no space is found before 75 characters, simply truncate to 75 characters
    return input_string[0:74]

def send_to_printer(item_number, item_name, label_number=''):
    if label_number == '':
        label_number = '1'
    print('Send to printer triggered')
    # Click A (edit button)
    pyautogui.click(x=1240, y=133)
    # Click on the 'Cod' label field and select all
    pyautogui.click(x=1723, y=515)
    pyautogui.hotkey('ctrl', 'a')
    # Input the item's code
    pyautogui.write('#'+item_number[0:13]) # max 14 char
    # Click on the 'Name' label field and select all
    pyautogui.click(x=1723, y=334)
    pyautogui.hotkey('ctrl', 'a')
    # Input the item's name
    pyautogui.write(limit_string(item_name)) # max 75 char
    # Print dialog box
    pyautogui.hotkey('ctrl', 'p')
    # Input the number of labels
    pyautogui.press('b')
    pyautogui.write(label_number)
    # Print the label
    pyautogui.press('enter')

    # For development purposes
    # pyautogui.displayMousePosition()