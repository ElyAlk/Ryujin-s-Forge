from gui_controller import Controller_Gui



if __name__ == '__main__':
    print('Main is running and prepairing to initalize the controller!')
    #try:
    gui = Controller_Gui()
    gui.update_length()
    gui.mainloop()
    #except Exception as e:
     #   print(f'Error occured during execution: {e}')