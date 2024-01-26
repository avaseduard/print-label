import pyautogui

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

def send_to_printer(number, name):
    # Click A (edit button)
    pyautogui.click(x=1240, y=133)
    # Click on the 'Cod' label field and select all
    pyautogui.click(x=1723, y=515)
    pyautogui.hotkey('ctrl', 'a')
    # Input the item's code
    pyautogui.write('#'+number[0:13]) # max 15 char
    # Click on the 'Name' label field and select all
    pyautogui.click(x=1723, y=334)
    pyautogui.hotkey('ctrl', 'a')
    # Input the item's name
    pyautogui.write(limit_string(name)) # max 90 char
    # Print the label
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.press('enter')

    # For development purposes
    # pyautogui.displayMousePosition()