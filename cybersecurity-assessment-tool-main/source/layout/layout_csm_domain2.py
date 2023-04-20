
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY DOMAIN 2"""

import layout.layout_home as home
import layout.layout_csm as csm
import layout.layout_login as login
import DATA

import tkinter as tk
from tkinter import messagebox


""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 2 page """
class CSM_Domain2_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Threat Intelligence and Collaboration")

        self.unbind_all("<MouseWheel>")
        self.config(bg="ghost white")

        home_button = tk.Button(self, width=10, text="HOME", font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        back_button = tk.Button(self, width=10, text="BACK", font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(csm.CSM_Page))

        threat_intelligence_button = tk.Button(self, text="Threat Intelligence", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                               command=lambda: master.switch_frame(CSM_Domain2_ThreatIntelligence_Page))

        monitoring_and_analyzing_button = tk.Button(self, text="Monitoring and Analyzing", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                                    command=lambda: master.switch_frame(CSM_Domain2_MonitoringAndAnalyzing_Page))

        information_sharing_button = tk.Button(self, text="Information Sharing", font='Calibri 14', relief='groove', borderwidth=2, bg='light gray', activebackground='light blue',
                                               command=lambda: master.switch_frame(CSM_Domain2_InformationSharing_Page))

        threat_intelligence_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                             text=str(csm.submit_pressed(CSM_Domain2_ThreatIntelligence_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain2_ThreatIntelligence[i]) for i in DATA.CSM_Domain2_ThreatIntelligence])))
        
        monitoring_and_analyzing_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                                  text=str(csm.submit_pressed(CSM_Domain2_MonitoringAndAnalyzing_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain2_MonitoringAndAnalyzing[i]) for i in DATA.CSM_Domain2_MonitoringAndAnalyzing])))
        
        information_sharing_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                             text=str(csm.submit_pressed(CSM_Domain2_InformationSharing_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain2_InformationSharing[i]) for i in DATA.CSM_Domain2_InformationSharing])))

        reset_button = tk.Button(self, text='RESET', width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: CSM_Domain2_Page.reset(master))

        home_button.place(relx=0.1, rely=0.1)
        back_button.place(relx=0.25, rely=0.1)

        threat_intelligence_button.place(relx=0.5, rely=0.3, anchor='center')
        monitoring_and_analyzing_button.place(relx=0.5, rely=0.4, anchor='center')
        information_sharing_button.place(relx=0.5, rely=0.5, anchor='center')

        threat_intelligence_label.place(relx=0.67, rely=0.3, anchor='center')
        monitoring_and_analyzing_label.place(relx=0.67, rely=0.4, anchor='center')
        information_sharing_label.place(relx=0.67, rely=0.5, anchor='center')

        reset_button.place(relx=0.5, rely=0.8, anchor='center')

    # reset the answers of Domain 2
    def reset(frame):
        confirm = messagebox.askokcancel('Confirmation', 'Are your sure you want to reset your answers ?')
        if confirm:
            csm.clear_pressed(CSM_Domain2_ThreatIntelligence_Page.values)
            csm.clear_pressed(CSM_Domain2_MonitoringAndAnalyzing_Page.values)
            csm.clear_pressed(CSM_Domain2_InformationSharing_Page.values)
            frame.switch_frame(CSM_Domain2_Page)
    #endregion


""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 2 - Threat Intelligence page """
class CSM_Domain2_ThreatIntelligence_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Threat Intelligence")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain2_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain2_Page))

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)
        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")
        
        # defines the scrolling distance when mousewheel is used
        def scroll(event):
            if event.delta < 0:
                my_canvas.yview("scroll", 1, "units")
            elif event.delta > 0:
                my_canvas.yview("scroll", -1, "units")
    
        my_canvas.bind_all("<MouseWheel>", scroll)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar (Cette ligne contraint le scroll sur la barre de scroll et empêche d'aller trop ou trop bas)
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain2_ThreatIntelligence.items():               
            for j in range(len(values)): 

                question = tk.Label(middle_frame, text=values[j], width=130, wraplength=1100, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
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


""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 2 - Monitoring and Analyzing page """
class CSM_Domain2_MonitoringAndAnalyzing_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Monitoring and Analyzing")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain2_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain2_Page))

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)
        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")
        
        # defines the scrolling distance when mousewheel is used
        def scroll(event):
            if event.delta < 0:
                my_canvas.yview("scroll", 1, "units")
            elif event.delta > 0:
                my_canvas.yview("scroll", -1, "units")
    
        my_canvas.bind_all("<MouseWheel>", scroll)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar (Cette ligne contraint le scroll sur la barre de scroll et empêche d'aller trop ou trop bas)
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain2_MonitoringAndAnalyzing.items():               
            for j in range(len(values)): 

                question = tk.Label(middle_frame, text=values[j], width=130, wraplength=1100, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
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


""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 2 - Information Sharing page """
class CSM_Domain2_InformationSharing_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title(login.Login_Page.logged_in.upper() + " - Information Sharing")
        self.config(bg='ghost white')

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")

        home_button = tk.Button(top_frame, text="HOME", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        home_button.pack(side=tk.LEFT, padx=20, pady=20)

        back_button = tk.Button(top_frame, text="BACK", width=10, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(CSM_Domain2_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, relief="groove", borderwidth=3, bg='ghost white')
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(CSM_Domain2_Page))

        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: csm.clear_category(self.values))

        submit_button.grid(row=1, column=3, padx=20, pady=10)
        clear_button.grid(row=1, column=2)
        bottom_frame.columnconfigure(1, weight=1)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")

        vertical_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        horizontal_scrollbar = tk.Scrollbar(bottom_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        horizontal_scrollbar.grid(row=0, column=0, columnspan=10, sticky='nsew')

        my_canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg="white")
        
        # defines the scrolling distance when mousewheel is used
        def scroll(event):
            if event.delta < 0:
                my_canvas.yview("scroll", 1, "units")
            elif event.delta > 0:
                my_canvas.yview("scroll", -1, "units")
    
        my_canvas.bind_all("<MouseWheel>", scroll)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind scroll region to scrollbar (Cette ligne contraint le scroll sur la barre de scroll et empêche d'aller trop ou trop bas)
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain2_InformationSharing.items():               
            for j in range(len(values)): 

                question = tk.Label(middle_frame, text=values[j], width=130, wraplength=1100, justify=tk.LEFT, relief='groove', font='Calibri 13')
                question.grid(row=i, column=0, pady=15, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                no_answer = tk.Radiobutton(middle_frame, text="N", bg='white', relief='groove', font='Calibri 14 bold', borderwidth=0, variable=self.values[i])
                
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
