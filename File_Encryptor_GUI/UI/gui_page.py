import tkinter as GUI

class Gui_Page(GUI.Frame):
    def __init__(self, parent, gui_controller, **kwargs):
        super().__init__(parent, **kwargs)
        
        # This is where Gui_Page handles the controller
        self.gui_controller = gui_controller