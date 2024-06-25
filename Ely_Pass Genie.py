import string, random, keyboard, os, pyfiglet

banner = pyfiglet.figlet_format("Ely_Pass Genie", font="epic")
menu = "Hello, I can help you out with password generation!\n\n1)Press the key 'ENTER' to generate new password.\n2)Press the key '+' to increase the password's length.\n3)Press the key '-' to decrease the password's length.\n4)Press the key 'M' to display this menu.\n5)Press the key 'ESC' to exit."
#The default length for a password
password_length = 12
output = """The password length <{}>
 
-║    {}    ║+
"""
#This function clears the console based on the operating system
def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)
#this function displays the banner & menu
def show_info():
    clear_console()
    print(banner, menu)

#This function updates the password's length
def increase_length():
    global password_length, output
    password_length+=1
    if password_length > 64:
        password_length = 64

    clear_console()
    print(output.format(password_length, "Please press 'ENTER'"), "\n\nPress the key 'M' to display the menu.")

#This function updates the password's length
def decrease_length():
    global password_length, output
    password_length-=1
    if password_length < 6:
        password_length = 6
    
    clear_console()
    print(output.format(password_length, "Please press 'ENTER'"), "\n\nPress the key 'M' to display the menu.")

#This function generates a new password based on the length
def generate_password(password_length):
    alpha = string.ascii_letters + string.digits + "!@#$%^&*-_=+/"
    password = ""

    while(password_length > 0):
        password+= alpha[random.randint(0,len(alpha)-1)]
        password_length-=1
    return password

#This functon handles key presses
def handle_key_press(key_pressed):
    if key_pressed.name == "+":
        increase_length()
    elif key_pressed.name == "-":
        decrease_length()
    elif key_pressed.name == "enter":
        password= generate_password(password_length)
        clear_console()
        print(output.format(password_length, password), "\n\nPress the key 'M' to display the menu.")
    elif key_pressed.name == "m":
        show_info()

show_info()
# Register the callback function for relevant keys
keyboard.on_press_key('+', handle_key_press)
keyboard.on_press_key('-', handle_key_press)
keyboard.on_press_key('enter', handle_key_press)
keyboard.on_press_key('m', handle_key_press)

# Keep the program running
keyboard.wait('esc')  # Press 'Esc' to exit