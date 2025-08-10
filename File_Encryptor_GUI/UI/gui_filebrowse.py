import tkinter as GUI
from .gui_page import Gui_Page

class File_Browse_Page(Gui_Page):
    def __init__(self, parent, gui_controller):
        super().__init__(parent, gui_controller)
        
        # Create Button for browsing files
        file_browse_button = GUI.Button(self, text="Browse Files", command=self.gui_controller.file_on_click)
        file_browse_button.pack()

