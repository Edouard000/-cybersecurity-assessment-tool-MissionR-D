""" Here is everything relating to the login and register pages including the layout and all the handlers """

import layout.layout_home as home
import db
import main

import tkinter as tk
from tkcalendar import DateEntry
from tkinter import  messagebox
from PIL import Image, ImageTk
import webbrowser
import bcrypt
import re
import os


""" This class handles the layout of the Login page (Grid Layout) """
class Login_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        master.title("Login")           # window title
        self.config(bg=main.bg_frame)   # frame background

        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        alpha_num_validation = self.register(only_alphanumeric) # register validation function

        user_label = main.Main_App.set_label(self, "Username", "Calibri 20")

        password_label = main.Main_App.set_label(self, "Password", "Calibri 20")

        user_entry = tk.Entry       (self, font="Calirbi 15", width=15, relief='groove', borderwidth=4, bg=main.bg_entry, 
                                     fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry,
                                     validate="key", validatecommand=(alpha_num_validation, '%S'))

        password_entry = tk.Entry   (self, font="Calirbi 15", width=15, relief='groove', borderwidth=4, bg=main.bg_entry, 
                                     fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show="*") 
        
        register_button = main.Main_App.set_button(self, "✍🏼 REGISTER", "Calibri 15", 'center', 120, lambda: master.switch_frame(Register_Page))
        
        login_button    = main.Main_App.set_button(self, "LOGIN ➡️", "Calibri 15", 'center', 120, lambda: verify_login(master, user_entry.get(), password_entry.get()))



        # Configure the empty rows and columns on each corner to make them scalable when the window is resized
        # Keeps all the widgets in the middle of the screen

        # rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, minsize=100)
        self.rowconfigure(5, weight=1)

        # columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, minsize=300)
        self.columnconfigure(2, minsize=300)
        self.columnconfigure(3, weight=1)
        

        user_label.grid         (row=2, column=1, padx=40, pady=20, sticky='e') 
        password_label.grid     (row=3, column=1, padx=40, pady=20, sticky='e')

        user_entry.grid         (row=2, column=2, pady=20, sticky='w')
        password_entry.grid     (row=3, column=2, pady=20, sticky='w')

        register_button.grid    (row=4, column=1, padx=20, pady=30, sticky='e')
        login_button.grid       (row=4, column=2, padx=20, pady=30, sticky='w')


        # bind enter key to the verify_login function === Login button pressed
        self.bind_all('<Return>', lambda e: verify_login(master, user_entry.get(), password_entry.get()))
        
        user_entry.focus() # Set the focus to the username entry

        # Add the IMT logo to the login page
        image = Image.open(os.path.join("resources","imt.png"))
        photo_image = ImageTk.PhotoImage(image)     
        image_label = tk.Label(self, image=photo_image) 
        image_label.image = photo_image
        image_label.place(relx=0.5, rely=0.2, anchor='center')

        # About label containing information about the app and a link to the repository
        about_label = tk.Label(self, text='About', font="Calibri 15 underline", bg=main.bg_label, fg='blue')
        about_label.place(relx=0.5, rely=0.9, anchor='center')
        about_label.bind("<Button-1>", lambda e: top_level(self, about_label))
    #endregion


""" This class handles the layout of the Registration page (Grid Layout) """
class Register_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Register")        # window title
        self.config(bg=main.bg_frame)   # frame background

        # Bind enter key to the registration function === Submit button pressed
        self.bind_all('<Return>', lambda e: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                        firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), dob_entry.get_date()))

        # limit entry to alphabetical characters only
        def only_alpha(char):
            return char.isalpha()

        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        # register validation functions
        alpha_validation = self.register(only_alpha)
        alpha_num_validation = self.register(only_alphanumeric)
        
        
        #Labels
        username_label         = main.Main_App.set_label(self, "Username", "Calibri 12")
        password_label         = main.Main_App.set_label(self, "Password", "Calibri 12")
        confirm_password_label = main.Main_App.set_label(self, "Confirm Password", "Calibri 12")        
        firstname_label        = main.Main_App.set_label(self, "First Name", "Calibri 12")
        lastname_label         = main.Main_App.set_label(self, "Last Name", "Calibri 12")
        email_label            = main.Main_App.set_label(self, "Email", "Calibri 12")
        company_label          = main.Main_App.set_label(self, "Company", "Calibri 12")
        dob_label              = main.Main_App.set_label(self, "Date of Birth", "Calibri 12")
        
        
        #Text entry fields
        username_entry         = tk.Entry    (self, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, validate="key", validatecommand=(alpha_num_validation, '%S'))

        password_entry         = tk.Entry    (self, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show='*')

        confirm_password_entry = tk.Entry    (self, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show='*')

        firstname_entry        = tk.Entry    (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, validate="key", validatecommand=(alpha_validation, '%S'))

        lastname_entry         = tk.Entry    (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, validate="key", validatecommand=(alpha_validation, '%S'))

        email_entry            = tk.Entry    (self, width=25, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry)

        company_entry          = tk.Entry    (self, font="Calirbi 11 bold", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry)

        dob_entry              = DateEntry   (self, width=17, font="Calirbi 11", relief='groove', borderwidth=4, bg=main.bg_entry,
                                             fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry)
        
        #Buttons
        cancel_button   = main.Main_App.set_button(self, "CANCEL", "Calibri 14", None, 100, lambda: master.switch_frame(Login_Page))
        register_button = main.Main_App.set_button(self, "REGISTER", "Calibri 14", None, 100, lambda: registration(master, username_entry.get(), password_entry.get(), confirm_password_entry.get(), 
                                                  firstname_entry.get(), lastname_entry.get(), email_entry.get(), company_entry.get(), dob_entry.get_date()))
        
        
        
        # Display a tooltip when hovering over the password entry field
        ToolTip(widget=password_entry, text="Password must be at least 9 characters long, with 1+ uppercase, 1+ numeric and 1+ special characters ($,@,#,%)")

        # Configure empty rows and columns in every corner as well as in the middle making the widgets scalable when the window is resized
        # Keeps all the widgets relatively centered 

        # rows
        self.rowconfigure(0, weight=2)
        self.rowconfigure(4, minsize=25)
        self.rowconfigure(6, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        # columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, minsize=25)
        self.columnconfigure(6, minsize=15)
        self.columnconfigure(9, weight=1)

        username_label.grid             (row=1, column=1, padx=10, pady=20)
        password_label.grid             (row=2, column=1, padx=10, pady=20)
        confirm_password_label.grid     (row=3, column=1, padx=10, pady=20)
        firstname_label.grid            (row=1, column=4, padx=10, pady=20)
        lastname_label.grid             (row=2, column=4, padx=10, pady=20)
        email_label.grid                (row=3, column=4, padx=10, pady=20)
        company_label.grid              (row=1, column=7, padx=10, pady=20)
        dob_label.grid                  (row=2, column=7, padx=10, pady=20)

        username_entry.grid             (row=1, column=2, padx=10, pady=20)
        password_entry.grid             (row=2, column=2, padx=10, pady=20)
        confirm_password_entry.grid     (row=3, column=2, padx=10, pady=20)
        firstname_entry.grid            (row=1, column=5, padx=10, pady=20)
        lastname_entry.grid             (row=2, column=5, padx=10, pady=20)
        email_entry.grid                (row=3, column=5, padx=10, pady=20)
        company_entry.grid              (row=1, column=8, padx=10, pady=20)
        dob_entry.grid                  (row=2, column=8, padx=10, pady=20)
        
        cancel_button.grid              (row=5, column=7)
        register_button.grid            (row=5, column=8)
    #endregion


""" This class handles the display of the tooltip """
class ToolTip(object):
    #region
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx()-10, self.widget.winfo_rooty()-15))
        label = tk.Label(tw, text = self.text, background = "#ffffe0", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        if tw is not None:
            tw.destroy()
        self.tooltipwindow = None
    #endregion


""" This function handles the display of the Toplevel frame that is shown when the About label is pressed
    @arg frame - parent frame
    @arg widget - defines the widget to attach this frame to """
def top_level(frame, widget):
    top = tk.Toplevel(frame, background = "#ffffe0", relief = 'solid')
    top.geometry("+{}+{}".format(widget.winfo_rootx()-250, widget.winfo_rooty()-50))
    top.wm_overrideredirect(1)

    info_label = tk.Label(top, background = "#ffffe0", font='Calibri 10', text='This project is powered by python.\nIt was made for the university of IMT Mines Ales and is completely open-source at their request.\nFeel free to contribute to the project via its github repository below.\nIf you have any concerns, requests or recommendations, you can reach me at miles.muollas@gmail.com')
    git_label = tk.Label(top, background = "#ffffe0", fg='blue', font='Calibri 10 underline', text="https://github.com/zarathus-tra/cybersecurity-assessment-tool")
    
    git_label.bind('<Button-1>', lambda e: open_url("https://github.com/zarathustre/cybersecurity-assessment-tool"))

    info_label.pack()
    git_label.pack()
    top.focus()

    top.bind('<Escape>', lambda e: hide())
    top.bind('<FocusOut>', lambda e: hide())

    def hide():
        top.destroy()


""" This function handles the registration of the user when the Register button is pressed
    @arg frame - represents the parent frame (master) to be switched
    @args - the remaining arguments represent all the entries in the registration page that the user can fill """    
def registration(frame, user_name, password, confirm_password, first_name, last_name, email, company, dob):

    SpecialChar = ['$', '@', '#', '%']  # special characters allowed
    user_name = user_name.lower()       # convert to lower case string
    email = email.lower()               # convert to lower case string

    # Generate salt and a hash code from the user's entered password
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)

    # Get username query
    get_username_query = """ SELECT username FROM users WHERE username=%s; """
    u_value = [user_name]
    db_con = db.create_db_connection("localhost", "root", db.rp, "CSA")
    username = db.read_query_data(db_con, get_username_query, u_value)
    db_con.close()

    # Insert into DB query
    insert_users_query = """ 
    INSERT INTO users (first_name, last_name, date_of_birth, email, company, username, password, salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); 
    """
    values = [first_name, last_name, dob, email, company, user_name, hashed, salt]

    # if there's an empty field
    if (user_name == "") or (password == "") or (confirm_password == "") or (first_name == "") or (last_name == "") or (email == "") or (company == ""):
        messagebox.showwarning("Warning", "All fields must be filled")
    # Check if username exists
    elif username:
        messagebox.showwarning("Warning", "Username already exists")
    # if passwords do not match
    elif (password != confirm_password):
        messagebox.showwarning("Warning", "Password mismatch")
    # if password does not conform to the required format
    elif (len(password) < 9 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char in SpecialChar for char in password)):
        messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
    # check if email is valid
    elif (not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)):
        messagebox.showwarning("Warning", "Invalid email")
    else:
        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")    # open db connection
        db.execute_query_data(db_connection, insert_users_query, values)                       # insert values into db
        db_connection.close()                                                                  # close connection
        frame.switch_frame(Login_Page)                                                         # switch frame to Login page


""" This function handles the verification of the username and password when the user presses Login
    @arg frame - represents the parent frame (master) to be switched 
    @args - username and password """
def verify_login(frame, user_name, password):

    # get from db queries
    get_username_query = """ SELECT username FROM users WHERE username=%s; """
    get_password_query = """ SELECT password FROM users WHERE username=%s; """
    u_value = [user_name]

    db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")    # open db connection
    user = db.read_query_data(db_connection, get_username_query, u_value)         # get username from db
    hash = db.read_query_data(db_connection, get_password_query, u_value)         # get hash from db
    db_connection.close()                                                         # close connection

    # if there's an empty field
    if (user_name == "") or (password == ""):
        messagebox.showwarning("Warning", "All fields must be filled")
    # if username does not exist in the db
    elif not user:
        messagebox.showwarning("Warning", "Username does not exist")
    # if password is wrong
    elif not bcrypt.checkpw(password.encode('utf8'), hash[0][0].encode('utf8')): # check password against a hashed value
        messagebox.showwarning("Warning", "Wrong Password")
    else:
        Login_Page.logged_in = user_name     # This variable holds the name of the logged in username
        frame.switch_frame(home.Home_Page)   # switch frame to Home page
 

# This functions opens a url using the default browser
def open_url(url):
    webbrowser.open_new(url)
