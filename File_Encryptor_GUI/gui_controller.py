import tkinter as GUI
import unicodedata
from tkinter import filedialog
from UI.gui_filebrowse import File_Browse_Page
from UI.gui_password import Password_Page

class Controller_Gui(GUI.Tk):
    def __init__(self):
        print("Constructing the GUI Controller...")
        super().__init__()
        print("The GUI Controller now is read!")
        self.title("File Encryption")
        self.geometry("400x200")

        # Initializing the main frame
        self.frames_container = GUI.Frame(self)
        self.frames_container.pack(side="top", fill="both", expand=True)
        self.frames_container.grid_rowconfigure(0, weight=1)
        self.frames_container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create instances of both pages to display and utilize them later
        for Page in (File_Browse_Page, Password_Page):
            frame = Page(parent=self.frames_container, gui_controller=self)
            self.frames[Page.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            print(f'Created {Page.__name__} Page successfully!')

        self.show_page(File_Browse_Page)

    # Display initilized frames to the screen
    def show_page(self, page_class):
        frame = self.frames[page_class.__name__]
        print(f'displaying {page_class.__name__} to screen...')
        frame.tkraise()
    
    # Render a file dialog frame to browse files
    def file_browse_dialog(self):
        print('Displaying file dialog to browse files...')
        #Create a FileDialog to browse for files
        file_path = filedialog.askopenfilename(title="Select a File to Protect from Unauthorized Access.", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("Excel Files", "*.xlsx")))
        return file_path
    
    # Select a file from the dialog and then luanch the password page
    def file_on_click(self):
        file_selected_path = self.file_browse_dialog()
        if file_selected_path:
            print(f'Selected File Path: {file_selected_path}')
            self.show_page(Password_Page)

    # Toggle Password visibility
    def toggle_password_visibility(self):
        # Check the password visibility status
        is_visible = self.frames['Password_Page'].show_variable.get()
        
        # Update the password visibility accordingly
        self.frames['Password_Page'].set_password_visibility(is_visible)
    
     # Calculating the entered password length and updating the Lable in realtime 
    def update_length(self):
        entered_password = self.frames['Password_Page'].password_entry.get()
        self.frames['Password_Page'].pass_length.set(f'Password Length is "{len(entered_password)}"')
        self.arabic_entry_check(self.frames['Password_Page'].password_entry.get())
        self.frames_container.after(100, self.update_length)

    # Check for Arabic input to alert user
    def arabic_entry_check(self, entered_pass):
        has_arabic = False
        for character in entered_pass:
            try:
                if "ARABIC" in unicodedata.name(character):
                    has_arabic= True
                    break
            
            except ValueError:
                pass
        
        # Update the password language alert message accordingly 
        self.frames['Password_Page'].set_password_lang_message(has_arabic)