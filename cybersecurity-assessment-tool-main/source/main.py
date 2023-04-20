
""" HERE IS THE MAIN PART OF THE APP HANDLING THE SIZE OF THE WINDOW, THE FIRST FRAME TO DISPLAY AND THE MAIN LOOP """

import layout.layout_login as login

import tkinter as tk
from tkinter import messagebox
import os
from tkmacosx import Button

#Frame
bg_frame = '#F2EBE9'                #Color of the background of each frame

#Button
bg_button = '#8E6248'               #Color of the background of each button
activebg_button = '#DDD0C8'         #Color of the active background of each button (when it's clicked)
fg_button = 'white'                 #Color of the active foreground of each button
cursor_button = 'hand2'             #Hand cursor for each button

#Text entry field
bg_entry = 'white'                  #Color of the background of each text entry field
fg_entry = 'black'                  #Color of the foreground of each text entry field
insertbackground_entry = 'black'    #Color of the insertbackground of each text entry field
cursor_entry = 'xterm'              #Xterm cursor (text cursor) for each text entry field

#Label
bg_label = bg_frame                 #Color of the background of each label which is the same of the bg_frame to make the colors harmonious
fg_label = '#24150E'                #Color of the active foreground of each button

bg_menu = '#DDD0C8'                 #Color of the menu, the top_frame and the bottom_frame



class Main_App(tk.Tk):
    #region
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        try:
            if os.name == 'nt':  # Windows
                self.iconbitmap('resources/cyber.ico')
            elif os.name == 'posix':  # macOS or Linux
                self.iconbitmap('resources/cyber2.icns')
        except tk.TclError:
            pass
        
        # set window size and starting position
        self.attributes('-fullscreen', True)
        self.protocol("WM_DELETE_WINDOW", lambda: Main_App.on_closing(self)) # add confirmation popup for exiting with X

        self.minsize(1280, 768)                # window minimum size
        self.switch_frame(login.Login_Page)    # display login page when first launched

    # destroys current frame and replaces it with a new one
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    # displays a confirmation popup and destroys the frame if the user clicks ok
    def on_closing(frame):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit ? Unsaved changes will be lost"):
            frame.destroy()
    
    # set the label : function to standardize the labels and lighten the program
    def set_label(self, set_text, set_font):
        return tk.Label(self, text=set_text, font=set_font, bg=bg_label, fg=fg_label)
    
    # set the button : function to standardize the buttons and lighten the program
    def set_button(self, set_text, set_font, set_anchor, set_width, set_command):
        return Button(self, text=set_text, width=set_width, font=set_font, anchor=set_anchor, relief='raised', borderwidth=4, bg=bg_button, 
                      activebackground=activebg_button, fg=fg_button, cursor=cursor_button, command=set_command)
    
    
    #endregion


if __name__ == "__main__":
    app = Main_App()
    app.mainloop()
    
    



    
    
    
    
    
    
    
    
    
    