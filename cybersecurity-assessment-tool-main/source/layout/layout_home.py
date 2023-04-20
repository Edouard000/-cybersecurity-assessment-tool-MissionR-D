"""" Here is everything related to the home page after logging in """

import layout.layout_irp as irp
import layout.layout_csm as csm
import layout.layout_login as login
import db
import main
import DATA

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import nametofont
import matplotlib.pyplot as plt
import bcrypt
import os


""" This class handles the the layout of the Home page as in the first page after logging in """
class Home_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Home')

        self.config(bg=main.bg_frame)

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        
        #Importation of the  buttons, labels & images
        title_label       = main.Main_App.set_label(self, "FIELD HOSPITALS ASSESSMENT TOOL", ("Calibri", 40, "bold"))
        subtitle_label    = main.Main_App.set_label(self, "Home", ("Calibri", 30, "bold"))
        image_computer    = tk.PhotoImage(file=os.path.join("resources","Computer.png"))
        image_label       = tk.Label(self, image=image_computer, bg=main.bg_label)
        image_label.image = image_computer                                                              #To avoid a garbage collection error
        cadre_label       = tk.Label(self, bg=main.bg_frame, borderwidth=4, relief='solid', fg=main.fg_label, width=75, height= 30)
        titledef1_label   = main.Main_App.set_label(self, "What is cybersecurity ?", ("Calibri", 14, "bold"))
        def1_label        = main.Main_App.set_label(self, "Cybersecurity is all the means implemented, hardware and software,\nwhich guarantee a certain level of security against cyberattacks.", "Calibri 13")
        titledef2_label   = main.Main_App.set_label(self, "To whom are these tests for ?", ("Calibri", 14, "bold"))
        def2_label        = main.Main_App.set_label(self, "These assessment tests are intended for field hospital users who\nhave the requisite knowledge of the field they are working in so\nthat they can describe it and take stock of the cyber protection arrangements.", "Calibri 13")
        titledef3_label   = main.Main_App.set_label(self, "What is the aim of this tool ?", ("Calibri", 14, "bold"))
        def3_label        = main.Main_App.set_label(self, "The purpose of this tool is to provide the user with an objective\ndiagnosis of the current level of cyber security of the equipment.", "Calibri 13")
        

        # Placement of the objects on the grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        
        title_label.grid(row=0, column=1, sticky='s')
        subtitle_label.grid(row=1, column=1)
        image_label.grid(row=2, column=1)
        cadre_label.grid(row=3, column=1, rowspan=6, pady=10)
        titledef1_label.grid(row=3, column=1, pady=5)
        def1_label.grid(row=4, column=1, sticky='n')
        titledef2_label.grid(row=5, column=1)
        def2_label.grid(row=6, column=1, sticky='n')
        titledef3_label.grid(row=7, column=1)
        def3_label.grid(row=8, column=1, sticky='n')
   
    
        #Menu with buttons
        menu=tk.Frame(self, bg=main.bg_menu)
        menu.grid(row=0, column=0, rowspan=20, sticky='nsew')
       
        home_button        = main.Main_App.set_button(menu, " 🏠 Home", "Calibri 20", 'w', 160, lambda: master.switch_frame(Home_Page))
        launch_button      = main.Main_App.set_button(menu, " 🚀 Launch a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(LaunchTest_Page))
        modify_button      = main.Main_App.set_button(menu, " 📝 Modify a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(ModifyTest_Page))
        results_button     = main.Main_App.set_button(menu, " 📈 View Results", "Calibri 15", 'w', 160, lambda: master.switch_frame(ViewResults_Page))
        change_pass_button = main.Main_App.set_button(menu, " 🔒 Change Password", "Calibri 15", 'w', 160, lambda: master.switch_frame(Change_Password_Page))
        logout_button      = main.Main_App.set_button(menu, " ⬅️ Log out", "Calibri 15", 'w', 160, lambda: master.switch_frame(login.Login_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=35, sticky='e')
        launch_button.grid(row=1, column=0, padx=30, pady=10, sticky='e')
        modify_button.grid(row=2, column=0, padx=30, pady=10, sticky='e')
        results_button.grid(row=3, column=0, padx=30, pady=10, sticky='e')
        change_pass_button.grid(row=4, column=0, padx=30, pady=10, sticky='e')
        logout_button.grid(row=5, column=0, padx=30, pady=10, sticky='e')
        
        
        #Disclaimer
        disclaimer = tk.Label(menu, font='Calibri 15', borderwidth=4, bg='#24150E', fg='white', relief='raised', text=' ⚠️ Disclaimer ⚠️ ')
        ToolTip(widget=disclaimer, text="The only aim of this tool is to evaluate the current protection level of a field hospital in front of cyberattacks.\nIt has not the role to improve the current protection but to prevent the risks.")
        disclaimer.grid(row=8, column=0, padx=30, pady=400, sticky='s')
        
        #Solves display issues with the buttons of the menu
        self.update()
        menu.update()
        
        # if admin is logged in
    #endregion


""" This class handles the the layout of the Launch a Test page """
class LaunchTest_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Launch a Test')
        
        self.config(bg=main.bg_frame)
        
        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")
        
        # Definitions of the textbox
        irp_text = "The Inherent Risk Profile identifies the institution’s inherent risk before implementing controls."
        csm_text = "The Cyber Security Maturity includes domains, assessment factors, components, and individual declarative statements across five maturity levels to identify specific controls and practices that are in place."

        irp_textbox = tk.Text(self, height=3, width=50, wrap="word", font="Calibri 15", relief='groove', borderwidth=4, bg=main.bg_entry)
        csm_textbox = tk.Text(self, height=3, width=50, wrap="word", font="Calibri 15", relief='groove', borderwidth=4, bg=main.bg_entry)

        irp_textbox.insert(tk.END, irp_text)
        csm_textbox.insert(tk.END, csm_text)

        irp_textbox.config(state="disabled")
        csm_textbox.config(state="disabled")


        #Importation of the  buttons, labels & images
        irp_button       = main.Main_App.set_button(self, "Assess Risk", "Calibri 14", None, 130, lambda: master.switch_frame(irp.IRP_Page))
        csm_button       = main.Main_App.set_button(self, "Assess Maturity", "Calibri 14", None, 130, lambda: master.switch_frame(csm.CSM_Page))
        overview_irp_button  = main.Main_App.set_button(self, "Overview IRP", "Calibri 14", None, 130, lambda: master.switch_frame(OverviewIRP_Page))
        overview_csm_button  = main.Main_App.set_button(self, "Overview CSM", "Calibri 14", None, 130, lambda: master.switch_frame(OverviewCSM_Page))
        
        title_label       = main.Main_App.set_label(self, "FIELD HOSPITALS ASSESSMENT TOOL", ("Calibri", 40, "bold"))
        subtitle_label    = main.Main_App.set_label(self, "Launch a Test", ("Calibri", 30, "bold"))
        image_computer    = tk.PhotoImage(file=os.path.join("resources","Computer.png"))
        image_label       = tk.Label(self, image=image_computer, bg=main.bg_label)
        image_label.image = image_computer                                                              #To avoid a garbage collection error
        
        
        # Placement
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        
        title_label.grid(row=0, column=1, columnspan=2, sticky='s')
        subtitle_label.grid(row=1, column=1, columnspan=2)
        image_label.grid(row=2, column=1, columnspan=2)
        
        overview_irp_button.grid(row=3, column=1)
        overview_csm_button.grid(row=3, column=2)
        irp_button.grid(row=4, column=1, pady=10)
        csm_button.grid(row=4, column=2, pady=10)
        irp_textbox.grid(row=5, column=1)
        csm_textbox.grid(row=5, column=2)
        
        
        #Menu with buttons
        menu=tk.Frame(self, bg=main.bg_menu)
        menu.grid(row=0, column=0, rowspan=20, sticky='nsew')
       
        home_button        = main.Main_App.set_button(menu, " 🏠 Home", "Calibri 20", 'w', 160, lambda: master.switch_frame(Home_Page))
        launch_button      = main.Main_App.set_button(menu, " 🚀 Launch a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(LaunchTest_Page))
        modify_button      = main.Main_App.set_button(menu, " 📝 Modify a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(ModifyTest_Page))
        results_button     = main.Main_App.set_button(menu, " 📈 View Results", "Calibri 15", 'w', 160, lambda: master.switch_frame(ViewResults_Page))
        change_pass_button = main.Main_App.set_button(menu, " 🔒 Change Password", "Calibri 15", 'w', 160, lambda: master.switch_frame(Change_Password_Page))
        logout_button      = main.Main_App.set_button(menu, " ⬅️ Log out", "Calibri 15", 'w', 160, lambda: master.switch_frame(login.Login_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=35, sticky='e')
        launch_button.grid(row=1, column=0, padx=30, pady=10, sticky='e')
        modify_button.grid(row=2, column=0, padx=30, pady=10, sticky='e')
        results_button.grid(row=3, column=0, padx=30, pady=10, sticky='e')
        change_pass_button.grid(row=4, column=0, padx=30, pady=10, sticky='e')
        logout_button.grid(row=5, column=0, padx=30, pady=10, sticky='e')
        
        
        #Solves display issues with the buttons of the menu
        self.update()
        menu.update()
        
    #endregion
    

""" This class handles the the layout of the Modify a Test page """
class ModifyTest_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Launch a Test')
        
        self.config(bg=main.bg_frame)
        
        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")

        #Importation of the  buttons, labels & images (these buttons are just a template for a future implementation)
        irp_label    = main.Main_App.set_label (self, "Inherent Risk Profile Tests", "Calibri 18")
        irp1_button  = main.Main_App.set_button(self, "Test n°1", "Calibri 14", None, 130, None)
        irp2_button  = main.Main_App.set_button(self, "Test n°2", "Calibri 14", None, 130, None)
        irp3_button  = main.Main_App.set_button(self, "Test n°3", "Calibri 14", None, 130, None)
        irp4_button  = main.Main_App.set_button(self, "Test n°4", "Calibri 14", None, 130, None)
        
        csm_label    = main.Main_App.set_label (self, "Cyber Security Maturity Tests", "Calibri 18")
        csm1_button  = main.Main_App.set_button(self, "Test n°1", "Calibri 14", None, 130, None)
        csm2_button  = main.Main_App.set_button(self, "Test n°2", "Calibri 14", None, 130, None)
        csm3_button  = main.Main_App.set_button(self, "Test n°3", "Calibri 14", None, 130, None)
        csm4_button  = main.Main_App.set_button(self, "Test n°4", "Calibri 14", None, 130, None)
        
        title_label       = main.Main_App.set_label(self, "FIELD HOSPITALS ASSESSMENT TOOL", ("Calibri", 40, "bold"))
        subtitle_label    = main.Main_App.set_label(self, "Modify a Test", ("Calibri", 30, "bold"))
        image_computer    = tk.PhotoImage(file=os.path.join("resources","Computer.png"))
        image_label       = tk.Label(self, image=image_computer, bg=main.bg_label)
        image_label.image = image_computer                                                              #To avoid a garbage collection error
        select_label      = main.Main_App.set_label(self, "Select the test you want to modify, continue, or delete", "Calibri 20")
        
        
        # Placement
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        
        title_label.grid(row=0, column=1, columnspan=2, sticky='s')
        subtitle_label.grid(row=1, column=1, columnspan=2)
        image_label.grid(row=2, column=1, columnspan=2)
        select_label.grid(row=3, column=1, columnspan=2, pady=5)
        
        irp_label.grid(row=4, column=1)
        irp1_button.grid(row=5, column=1)
        irp2_button.grid(row=6, column=1)
        irp3_button.grid(row=7, column=1)
        irp4_button.grid(row=8, column=1)
        
        csm_label.grid(row=4, column=2)
        csm1_button.grid(row=5, column=2)
        csm2_button.grid(row=6, column=2)
        csm3_button.grid(row=7, column=2)
        csm4_button.grid(row=8, column=2)
     
        
        #Menu with buttons
        menu=tk.Frame(self, bg=main.bg_menu)
        menu.grid(row=0, column=0, rowspan=20, sticky='nsew')
       
        home_button        = main.Main_App.set_button(menu, " 🏠 Home", "Calibri 20", 'w', 160, lambda: master.switch_frame(Home_Page))
        launch_button      = main.Main_App.set_button(menu, " 🚀 Launch a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(LaunchTest_Page))
        modify_button      = main.Main_App.set_button(menu, " 📝 Modify a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(ModifyTest_Page))
        results_button     = main.Main_App.set_button(menu, " 📈 View Results", "Calibri 15", 'w', 160, lambda: master.switch_frame(ViewResults_Page))
        change_pass_button = main.Main_App.set_button(menu, " 🔒 Change Password", "Calibri 15", 'w', 160, lambda: master.switch_frame(Change_Password_Page))
        logout_button      = main.Main_App.set_button(menu, " ⬅️ Log out", "Calibri 15", 'w', 160, lambda: master.switch_frame(login.Login_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=35, sticky='e')
        launch_button.grid(row=1, column=0, padx=30, pady=10, sticky='e')
        modify_button.grid(row=2, column=0, padx=30, pady=10, sticky='e')
        results_button.grid(row=3, column=0, padx=30, pady=10, sticky='e')
        change_pass_button.grid(row=4, column=0, padx=30, pady=10, sticky='e')
        logout_button.grid(row=5, column=0, padx=30, pady=10, sticky='e')
        
        
        #Solves display issues with the buttons of the menu
        self.update()
        menu.update()
        
    #endregion

    
""" This class handles the the layout of the View Results page """
class ViewResults_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - View Results')

        self.config(bg=main.bg_frame)

        self.unbind_all("<MouseWheel>")
        self.unbind_all("<Return>")
       
        #Importation of the  buttons, labels & images
        display_irp_button = main.Main_App.set_button(self, "Risk Results", "Calibri 14", None, 150, lambda: display_irp(master))
        display_csm_button = main.Main_App.set_button(self, "Maturity Results", "Calibri 14", None, 150, lambda: display_csm(master))
        title_label        = main.Main_App.set_label(self, "FIELD HOSPITALS ASSESSMENT TOOL", ("Calibri", 40, "bold"))
        subtitle_label     = main.Main_App.set_label(self, "View Results", ("Calibri", 30, "bold"))
        image_computer     = tk.PhotoImage(file=os.path.join("resources","Computer.png"))
        image_label        = tk.Label(self, image=image_computer, bg=main.bg_label)
        image_label.image  = image_computer                                                              #To avoid a garbage collection error
        select_label       = main.Main_App.set_label(self, "Select a type of results you want to see", "Calibri 20")
        

        # Placement
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        
        
        title_label.grid(row=0, column=1, columnspan=2, sticky='s')
        subtitle_label.grid(row=1, column=1, columnspan=2)
        image_label.grid(row=2, column=1, columnspan=2)
        select_label.grid(row=3, column=1, columnspan=2, pady=5)
        
        display_irp_button.grid(row=4, column=1)
        display_csm_button.grid(row=4, column=2)
        
        
        #Menu with buttons
        menu=tk.Frame(self, bg=main.bg_menu)
        menu.grid(row=0, column=0, rowspan=20, sticky='nsew')
       
        home_button        = main.Main_App.set_button(menu, " 🏠 Home", "Calibri 20", 'w', 160, lambda: master.switch_frame(Home_Page))
        launch_button      = main.Main_App.set_button(menu, " 🚀 Launch a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(LaunchTest_Page))
        modify_button      = main.Main_App.set_button(menu, " 📝 Modify a Test", "Calibri 15", 'w', 160, lambda: master.switch_frame(ModifyTest_Page))
        results_button     = main.Main_App.set_button(menu, " 📈 View Results", "Calibri 15", 'w', 160, lambda: master.switch_frame(ViewResults_Page))
        change_pass_button = main.Main_App.set_button(menu, " 🔒 Change Password", "Calibri 15", 'w', 160, lambda: master.switch_frame(Change_Password_Page))
        logout_button      = main.Main_App.set_button(menu, " ⬅️ Log out", "Calibri 15", 'w', 160, lambda: master.switch_frame(login.Login_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=35, sticky='e')
        launch_button.grid(row=1, column=0, padx=30, pady=10, sticky='e')
        modify_button.grid(row=2, column=0, padx=30, pady=10, sticky='e')
        results_button.grid(row=3, column=0, padx=30, pady=10, sticky='e')
        change_pass_button.grid(row=4, column=0, padx=30, pady=10, sticky='e')
        logout_button.grid(row=5, column=0, padx=30, pady=10, sticky='e')
        
        
        #Solves display issues with the buttons of the menu
        self.update()
        menu.update()
        
    #endregion

""" This class handles the the layout of the Overview IRP Test : ~10 questions to show the advantages of fully carrying out a diagnosis. """
class OverviewIRP_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Overview IRP")

        self.config(bg=main.bg_frame)
        
        
        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg=main.bg_menu, relief='groove', borderwidth=4)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")
        
        home_button = main.Main_App.set_button(top_frame, "🏠 HOME", "Calibri 11", None, 100, lambda: master.switch_frame(Home_Page))
        back_button = main.Main_App.set_button(top_frame, "🔙 Back", "Calibri 11", None, 100, lambda: master.switch_frame(LaunchTest_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)


        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg=main.bg_menu, relief='groove', borderwidth=4)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = main.Main_App.set_button(bottom_frame, "SUBMIT", "Calibri 11", None, 100, lambda: master.switch_frame(LaunchTest_Page))
        clear_button = main.Main_App.set_button(bottom_frame, "CLEAR", "Calibri 11", None, 100, lambda: irp.clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)


        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg=main.bg_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg=main.bg_frame)
        
        # defines the scrolling distance when mousewheel is used
        def scroll(event):
            if event.delta < 0:
                my_canvas.yview("scroll", 1, "units")
            elif event.delta > 0:
                my_canvas.yview("scroll", -1, "units")
    
        my_canvas.bind_all("<MouseWheel>", scroll)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar (Cette ligne contraint le scroll sur la barre de scroll et empêche d'aller trop ou trop bas)
        
        middle_frame = tk.Frame(my_canvas, bg=main.bg_frame)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Labels representing the risk levels
        label1 = tk.Label(middle_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(middle_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(middle_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(middle_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(middle_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=3, sticky='w', padx=30)
        label4.grid(row=0, column=4, sticky='w', padx=30)
        label5.grid(row=0, column=5, sticky='w', padx=30)

        # Get the questions from DATA and align them on screen     #Changes = width=50 -> 20 & pady=20 ->50
        i = 0
        for key, value in DATA.OverviewIRP.items():

            question = tk.Label(middle_frame, width=43, text=key, wraplength=350, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg=main.bg_frame)
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" This class handles the the layout of the Overview CSM Test : ~20 questions to show the advantages of fully carrying out a diagnosis. """
class OverviewCSM_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Overview CSM")

        self.config(bg=main.bg_frame)
        
        
        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg=main.bg_menu, relief='groove', borderwidth=4)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")
        
        home_button = main.Main_App.set_button(top_frame, "🏠 HOME", "Calibri 11", None, 100, lambda: master.switch_frame(Home_Page))
        back_button = main.Main_App.set_button(top_frame, "🔙 Back", "Calibri 11", None, 100, lambda: master.switch_frame(LaunchTest_Page))
        
        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)


        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg=main.bg_menu, relief='groove', borderwidth=4)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = main.Main_App.set_button(bottom_frame, "SUBMIT", "Calibri 11", None, 100, lambda: master.switch_frame(LaunchTest_Page))
        clear_button = main.Main_App.set_button(bottom_frame, "CLEAR", "Calibri 11", None, 100, lambda: irp.clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)

        bottom_frame.columnconfigure(1, weight=1)


        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self, bg=main.bg_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg=main.bg_frame)
        
        # defines the scrolling distance when mousewheel is used
        def scroll(event):
            if event.delta < 0:
                my_canvas.yview("scroll", 1, "units")
            elif event.delta > 0:
                my_canvas.yview("scroll", -1, "units")
    
        my_canvas.bind_all("<MouseWheel>", scroll)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar (Cette ligne contraint le scroll sur la barre de scroll et empêche d'aller trop ou trop bas)
        
        middle_frame = tk.Frame(my_canvas, bg=main.bg_frame)
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")


        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.OverviewCSM.items():               
            for j in range(len(values)):

                question = tk.Label(middle_frame, text=values[j], width=130, wraplength=1100, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg=main.bg_frame, relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg=main.bg_frame, relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg=main.bg_frame, relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
                """ First part of the value references the answer (1 = yes | 2 = yes compensating | 3 = no)
                    Second part of the value references the maturity level (1 = Baseline | 2 = Evolving | 3 = Intermediate | 4 = Advanced | 5 = Innovative) """

                # Baseline
                if key.endswith('1'):
                    yes_answer['value'] = 11
                    yes_c_answer['value'] = 21
                    no_answer['value'] = 31

                # Evolving
                if key.endswith('2'):
                    yes_answer['value'] = 12
                    yes_c_answer['value'] = 22
                    no_answer['value'] = 32

                # Intermediate
                if key.endswith('3'):
                    yes_answer['value'] = 13
                    yes_c_answer['value'] = 23
                    no_answer['value'] = 33

                # Advanced
                if key.endswith('4'):
                    yes_answer['value'] = 14
                    yes_c_answer['value'] = 24
                    no_answer['value'] = 34

                # Innovative
                if key.endswith('5'):
                    yes_answer['value'] = 15
                    yes_c_answer['value'] = 25
                    no_answer['value'] = 35
                
                yes_answer.grid(row=i, column=1, padx=20)
                yes_c_answer.grid(row=i, column=2, padx=10)
                no_answer.grid(row=i, column=3, padx=15)

                i += 1
    #endregion



""" This class handles the layout of the change password page """
class Change_Password_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + ' - Change Password')
        
        self.config(bg=main.bg_frame)
        
        old_password_label         = main.Main_App.set_label(self, "Current Password", "Calibri 20")
        new_password_label         = main.Main_App.set_label(self, "New Password", "Calibri 20")
        confirm_new_password_label = main.Main_App.set_label(self, "Confirm Password", "Calibri 20")

        old_password_entry         = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=4, bg=main.bg_entry, 
                                     fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show="*")

        new_password_entry         = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=4, bg=main.bg_entry, 
                                     fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show="*")

        confirm_new_password_entry = tk.Entry(self, font="Calirbi 15", relief='groove', borderwidth=4, bg=main.bg_entry, 
                                     fg=main.fg_entry, insertbackground=main.insertbackground_entry, cursor=main.cursor_entry, show="*")

        
        cancel_button = main.Main_App.set_button(self, "CANCEL", "Calibri 14", None, 150, lambda: master.switch_frame(Home_Page))
        confirm_button = main.Main_App.set_button(self, "CONFIRM", "Calibri 14", None, 150, lambda: Change_Password_Page.change_password(master, old_password_entry.get(), new_password_entry.get(), confirm_new_password_entry.get()))
        

        old_password_label.place(relx=0.40, rely=0.3, anchor='center')
        new_password_label.place(relx=0.40, rely=0.4, anchor='center')
        confirm_new_password_label.place(relx=0.40, rely=0.5, anchor='center')

        old_password_entry.place(relx=0.60, rely=0.3, anchor='center')
        new_password_entry.place(relx=0.60, rely=0.4, anchor='center')
        confirm_new_password_entry.place(relx=0.60, rely=0.5, anchor='center')

        cancel_button.place(relx=0.4, rely=0.7, anchor='center')
        confirm_button.place(relx=0.6, rely=0.7, anchor='center')

        # add tooltips to the new password and confirm password entry fields
        ToolTip(widget=new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase,\n1+ numeric and1+ special characters ($,@,#,%)')
        ToolTip(widget=confirm_new_password_entry, text='Password must be at least 9 characters long, with 1+ uppercase,\n1+ numeric and 1+ special characters ($,@,#,%)')

    
    """ This function handles all the verifications and the changing of the password
        @arg frame - parent frame (master) to switch
        @arg old_pass - references the user's old password
        @arg new_pass - references the user's new password
        @arg confirm_new_pass - references the password confirmation """
    def change_password(frame, old_pass, new_pass, confirm_new_pass):
        SpecialChar = ['$', '@', '#', '%']

        # Generate salt and a hash code from the user's entered password
        salt = bcrypt.gensalt(rounds=12)
        new_hash = bcrypt.hashpw(new_pass.encode('utf8'), salt)

        get_password_query = """ SELECT password FROM users WHERE username=%s; """
        change_password_query = """ UPDATE users SET password=%s, salt=%s WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]
        new_values = [new_hash, salt, login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
        old_hash = db.read_query_data(db_connection, get_password_query, u_value)
        db_connection.close()

        confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to reset your password ?')
        if confirm:
            # if empty fields
            if (old_pass == "") or (new_pass == "") or (confirm_new_pass == ""):
                messagebox.showwarning("Warning", "All fields must be filled")
            # if wrong old password entered
            elif not bcrypt.checkpw(old_pass.encode('utf8'), old_hash[0][0].encode('utf8')): # check password against a hashed value
                messagebox.showwarning("Warning", "Wrong password")
            # if new password does not match the confirm new password 
            elif new_pass != confirm_new_pass:
                messagebox.showwarning("Warning", "Password mismatch")
            # if new password does not conform to the required format 
            elif (len(new_pass) < 9 or not any(char.isdigit() for char in new_pass) or not any(char.isupper() for char in new_pass) or not any(char in SpecialChar for char in new_pass)):
                messagebox.showwarning("Warning", "Password must be 9 characters long with at least 1 numeric, 1 uppercase and 1 special character ($,@,#,%)")
            else:
                db_connection = db.create_db_connection("localhost", "root", db.rp, "CSA")
                db.execute_query_data(db_connection, change_password_query, new_values)
                db_connection.close()
                frame.switch_frame(Home_Page)
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
        label = tk.Label(tw, text = self.text, background = "red", fg='white', relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        if tw is not None:
            tw.destroy()
        self.tooltipwindow = None
    #endregion



""" This class handles the layout of the IRP results page """
class Display_IRP(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Inherent Risk Profile Results')
        self.config(bg=main.bg_frame)

        # top frame
        top_frame = tk.Frame(self, bg=main.bg_menu, borderwidth=4)
        top_frame.pack(side=tk.TOP, fill='x')

        back_button = main.Main_App.set_button(top_frame, "🔙 Back", "Calibri 10", None, 100, lambda: master.switch_frame(ViewResults_Page))
        graph_button = main.Main_App.set_button(top_frame, "📊 Graph Display", "Calibri 10", None, 120, lambda: Display_IRP.graph(table.item(table.focus())))


        back_button.pack(side=tk.LEFT, padx=50, pady=10)
        graph_button.place(relx=0.5, rely=0.5, anchor='center')

        # bottom frame
        bottom_frame = tk.Frame(self, bg=main.bg_menu, borderwidth=4)
        bottom_frame.pack(side=tk.BOTTOM, expand='yes', fill='both')

        # columns of the display table
        cols = ('Date','Name','Least','Minimal','Moderate','Significant','Most','Risk Level')
        table = ttk.Treeview(bottom_frame, columns=cols, show='headings')

        scrollbar = ttk.Scrollbar(bottom_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        table.configure(yscrollcommand=scrollbar.set)

        cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

        get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
        username = [login.Login_Page.logged_in]
        uid = db.read_query_data(cnx, get_user_id_query, username)

        get_irp_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp WHERE user=%s ORDER BY date DESC; """
        get_irp_all_query = """ SELECT date, name, least, minimal, moderate, significant, most, risk_level FROM irp ORDER BY date DESC; """
        user = [uid[0][0]]

        if login.Login_Page.logged_in == 'admin':
            results = db.read_query(cnx, get_irp_all_query)
            delete_button = tk.Button(top_frame, text="Delete Row",  width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', 
                                      activebackground='light blue', command=lambda: Display_IRP.delete(table.item(table.focus()), master))
            delete_button.pack(side='left')
        else:
            results = db.read_query_data(cnx, get_irp_query, user)

        cnx.close()

        # display table column names and width
        for col in cols:
            table.heading(col, text=col)
            table.column(col, width=50, anchor='center')

        # insert data rows into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))
        
        nametofont("TkHeadingFont").configure(weight='bold')    # headings font bold
        table.pack(side=tk.LEFT, expand='yes', fill='both')

    # this function handles the display of a single row from the table as a bar graph
    def graph(row):
        values = row.get('values')
        
        if not values:
            messagebox.showwarning('Warning', 'Select an assessment to visualize')
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            get_irp_query = """ SELECT least, minimal, moderate, significant, most FROM irp WHERE name=%s; """
            name_value = [values[1]]
            result = db.read_query_data(cnx, get_irp_query, name_value)
            cnx.close()

            # labels on the x-axis
            x_axis = ['Least', 'Minimal', 'Moderate', 'Significant', 'Most']

            plt.bar(x_axis, result[0])                          # create the bars
            plt.title('Assessment: {}'.format(values[1]))       # assessment name as the title for the graph
            plt.show()                                          # show graph

    # this function deletes a row from the irp table when given the name of the assessment in the row
    def delete(row, frame):
        values = row.get('values')

        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM irp WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this row ?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                frame.switch_frame(Display_IRP)
            cnx.close()
    #endregion


""" This class handles the layout of the CSM results page """
class Display_CSM(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        master.title(login.Login_Page.logged_in.upper() + ' - Cybersecurity Maturity Results')
        self.config(bg=main.bg_frame)

        # top frame
        top_frame = tk.Frame(self, bg=main.bg_menu, borderwidth=4)
        top_frame.pack(side=tk.TOP, fill='x')

        back_button = main.Main_App.set_button(top_frame, "🔙 Back", "Calibri 10", None, 100, lambda: master.switch_frame(ViewResults_Page))
        graph_button = main.Main_App.set_button(top_frame, "📊 Graph Display", "Calibri 10", None, 120, lambda: Display_CSM.graph(table.item(table.focus())))


        back_button.pack(side=tk.LEFT, padx=50, pady=10)
        graph_button.place(relx=0.5, rely=0.5, anchor='center')

        # bottom frame
        bottom_frame = tk.Frame(self, bg=main.bg_menu, borderwidth=4)
        bottom_frame.pack(side=tk.BOTTOM, expand='yes', fill='both')

        # columns of the display table
        cols = ('Date','Name',
        'B (Y)', 'E (Y)', 'Inter (Y)', 'A (Y)', 'Inno (Y)',
        'B (C)', 'E (C)', 'Inter (C)', 'A (C)', 'Inno (C)',
        'B (N)', 'E (N)', 'Inter (N)', 'A (N)', 'Inno (N)',
        'Maturity Level')

        table = ttk.Treeview(bottom_frame, columns=cols, show='headings')

        # scrollbar
        scrollbar = ttk.Scrollbar(bottom_frame, orient='vertical', command=table.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        table.configure(yscrollcommand=scrollbar.set)

        # Display table column names and width
        for col in cols:
            table.heading(col, text=col)
            if col == 'Date' or col == 'Name':
                table.column(col, width=70, anchor='center')
            elif col == 'Maturity Level':
                table.column(col, width=45, anchor='center')
            else:
                table.column(col, width=15, anchor='center')

        cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

        get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
        username = [login.Login_Page.logged_in]
        uid = db.read_query_data(cnx, get_user_id_query, username)
        
        get_csm_query = """ 
        SELECT date, name, 
        baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
        baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
        baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no,
        maturity_level FROM csm WHERE user=%s ORDER BY date DESC; """

        get_csm_all_query = """ 
        SELECT date, name, 
        baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
        baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
        baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no,
        maturity_level FROM csm ORDER BY date DESC; """

        user = [uid[0][0]]

        if login.Login_Page.logged_in == 'admin':
            results = db.read_query(cnx, get_csm_all_query)
            delete_button = tk.Button(top_frame, text="Delete Row",  width=10, font="Calibri 10", relief='raised', borderwidth=2, bg='azure3', 
                                      activebackground='light blue', command=lambda: Display_CSM.delete(table.item(table.focus()), master))
            delete_button.pack(side='left')
        else:
            results = db.read_query_data(cnx, get_csm_query, user)

        cnx.close()

        # insert values into display table
        for result in results:
            vals = []
            for i in range(len(result)):
                vals.append(result[i])
            table.insert("", "end", values=tuple(vals))

        nametofont("TkHeadingFont").configure(weight='bold') # make headings bold
        table.pack(side=tk.LEFT, expand='yes', fill='both')

        # hint label that displays information about the symbols found on this page
        hint_label = tk.Label(top_frame, text='Hint', font="Calibri 10 underline", bg='ghost white', fg='blue')
        hint_label.place(relx=0.9, rely=0.5, anchor='center')
        hint_label.bind("<Button-1>", lambda e: top_level(self, hint_label))

    # this function handles the display of a single row from the table as a bar graph
    def graph(row):
        values = row.get('values')
        
        if not values:
            messagebox.showwarning('Warning', 'Select an assessment to visualize')
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            get_csm_query = """ SELECT 
            baseline_yes, evolving_yes, intermediate_yes, innovative_yes, advanced_yes, 
            baseline_compensating, evolving_compensating, intermediate_compensating, advanced_compensating, innovative_compensating,
            baseline_no, evolving_no, intermediate_no, advanced_no, innovative_no 
            FROM csm WHERE name=%s; """
            name_value = [values[1]]
            result = db.read_query_data(cnx, get_csm_query, name_value)
            cnx.close()

            # labels on the x-axis
            x_axis = ['B(Y)', 'E(Y)', 'I(Y)', 'A(Y)', 'I(Y)',
                      'B(C)', 'E(C)', 'I(C)', 'A(C)', 'I(C)',
                      'B(N)', 'E(N)', 'I(N)', 'A(N)', 'I(N)']

            plt.bar(x_axis, result[0])                      # create the bars
            plt.title('Assessment: {}'.format(values[1]))   # assessment name as the title of the graph
            plt.show()                                      # show graph

    # this function deletes a row from the csm table when given the name of the assessment in the row
    def delete(row, frame):
        values = row.get('values')

        if not values:
            messagebox.showwarning("Warning", "Select a row to delete")
        else:
            cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")
            delete_row_query = """ DELETE FROM csm WHERE name=%s; """
            name_value = [values[1]]
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this row ?"):
                db.execute_query_data(cnx, delete_row_query, name_value)
                frame.switch_frame(Display_CSM)
            cnx.close()
    #endregion


# this function handles the top level window when the hint label is pressed (displays information about the symbols)
def top_level(frame, widget):
    top = tk.Toplevel(frame, background = "#ffffe0", relief = 'solid')
    top.geometry("+{}+{}".format(widget.winfo_rootx()-300, widget.winfo_rooty()))
    top.wm_overrideredirect(1)

    info_label = tk.Label(top, background = "#ffffe0", font='Calibri 10', 
                          text='Symbols found in this page:\nB: Baseline, E: Evolving, I/Inter: Intermediate, A: Advanced, I/Inno: Innovative\n(Y): Yes, (C): Compensating, (N): No')
    
    info_label.pack()
    top.focus()

    top.bind('<Escape>', lambda e: hide())
    top.bind('<FocusOut>', lambda e: hide())

    def hide():
        top.destroy()


# this function handles the validation before displaying the IRP results
def display_irp(frame):
    cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

    get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
    username = [login.Login_Page.logged_in]
    uid = db.read_query_data(cnx, get_user_id_query, username)

    get_irp_query = """ SELECT iid FROM irp WHERE user=%s; """
    get_irp_all_query = """ SELECT iid FROM irp; """
    user = [uid[0][0]]

    if uid[0][0] == 1:
        results = db.read_query(cnx, get_irp_all_query)
    else:
        results = db.read_query_data(cnx, get_irp_query, user)

    cnx.close()

    if not results:
        messagebox.showwarning("Warning", "No assessments have been saved by this user")
    else:
        frame.switch_frame(Display_IRP)


# this function handles the validation before displaying the CSM results 
def display_csm(frame):
    cnx = db.create_db_connection("localhost", "root", db.rp, "CSA")

    get_user_id_query = """ SELECT uid FROM users WHERE username=%s; """
    username = [login.Login_Page.logged_in]
    uid = db.read_query_data(cnx, get_user_id_query, username)

    get_csm_query = """ SELECT cid FROM csm WHERE user=%s; """
    get_csm_all_query = """ SELECT cid FROM csm; """
    user = [uid[0][0]]

    if uid[0][0] == 1:
        results = db.read_query(cnx, get_csm_all_query)
    else:
        results = db.read_query_data(cnx, get_csm_query, user)

    cnx.close()

    if not results:
        messagebox.showwarning("Warning", "No assessments have been saved by this user")
    else:
        frame.switch_frame(Display_CSM)


# this function displays a confirmation box and then resets all the answers before logging out
def reset_and_logout(frame):
    confirm = messagebox.askokcancel('Confirmation', 'Are you sure you want to logout ? Unsaved results will be lost')
    if confirm:
        csm.reset_csm()
        irp.reset_irp()
        frame.switch_frame(login.Login_Page)
