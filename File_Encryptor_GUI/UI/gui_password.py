import tkinter as GUI
from .gui_page import Gui_Page


class Password_Page(Gui_Page):
    def __init__(self, parent, gui_controller):
        super().__init__(parent, gui_controller)

        # Create Password Lable widget and add it into the main window through pack method which is a layout manager.
        password_lable = GUI.Label(self, font=('Segoe UI', 14), text="Password:")
        password_lable.pack()

        # Create Passord Text Field widget and add it into the main window
        self.password_entry = GUI.Entry(self, justify='center', width=64, show='*')
        self.password_entry.pack()

        # Create Password Information Frame to group related widgets together
        pass_frame = GUI.Frame(self)
        pass_frame.pack(pady=5)

        # Create Checkbox to show or hide password
        self.show_variable = GUI.BooleanVar()
        self.password_checkbox = GUI.Checkbutton(pass_frame, text='Show Password', variable=self.show_variable, command=self.gui_controller.toggle_password_visibility)
        self.password_checkbox.pack(side=GUI.RIGHT)

        # Create Password Language Warning message 
        self.password_lang_warning = GUI.Label(self, font=('Segoe UI', 10), text='message here!')
        self.password_lang_warning.pack()

        # Create Password Length Indicator Label and add it into the main window
        self.pass_length = GUI.StringVar()
        self.pass_length.set(f'Password Length is "0"')
        password_counter = GUI.Label(pass_frame, font=('Segoe UI', 10), textvariable=self.pass_length)
        password_counter.pack(side=GUI.LEFT)
    
    def set_password_visibility(self, is_visable):
        if is_visable:
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def set_password_lang_message(self, has_arabic):
        if has_arabic:
            self.password_lang_warning.config(text='You have entered Arabic characters!\nPress on Alt+Sheft to change language into English.', fg="red")
        else: 
            self.password_lang_warning.config(text='')
