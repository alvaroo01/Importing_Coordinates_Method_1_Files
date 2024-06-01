
def GUI():

    import tkinter
    import tkinter.messagebox
    import customtkinter
    import InsertCoordsWindow

    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


    class App(customtkinter.CTk):

        WIDTH = 780
        HEIGHT = 520

        def __init__(self):
            super().__init__()
            self.title("Scara GUI")
            self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
            self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

            # ============ create two frames ============

            # configure grid layout (2x1)

            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)

            self.Left_Frame = customtkinter.CTkFrame(master=self,
                                                    width=180,
                                                    corner_radius=0)
            self.Left_Frame.grid(row=0, column=0, sticky="nswe")

            self.Right_Frame = customtkinter.CTkFrame(master=self)
            self.Right_Frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            # ============ Left_Frame ============

            self.Left_Frame.grid_rowconfigure(9, minsize=20)    # empty row with minsize as spacing
   

            self.OptionsLabel = self.OptionsLabel = customtkinter.CTkLabel(master=self.Left_Frame,
                                           text="Options")  # font name and size in px
            self.OptionsLabel.grid(row=1, column=0, pady=10, padx=10)

            self.Button_1 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Import New Coords",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.InsertCoords_ButtonEvent)
            self.Button_1.grid(row=2, column=0, pady=10, padx=20)

            self.Button_2 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 2",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.ButtonEvent_2)
            self.Button_2.grid(row=3, column=0, pady=10, padx=20)

            self.Button_3 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 3",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.ButtonEvent_3)
            self.Button_3.grid(row=4, column=0, pady=10, padx=20)

            self.Button_4 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 4",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.ButtonEvent_4)
            self.Button_4.grid(row=5, column=0, pady=10, padx=20)

            self.Button_5 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 5",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-colorght_Frame
                                                    command=self.ButtonEvent_5)
            self.Button_5.grid(row=6, column=0, pady=10, padx=20)

            self.Button_6 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 6",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.ButtonEvent_6)
            self.Button_6.grid(row=7, column=0, pady=10, padx=20)

            self.Button_7 = customtkinter.CTkButton(master=self.Left_Frame,
                                                    text="Button 7",
                                                    fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                    command=self.ButtonEvent_7)
            self.Button_7.grid(row=8, column=0, pady=10, padx=20)


            self.Switch_1 = customtkinter.CTkSwitch(master=self.Left_Frame, 
                                                    text="Switch 1",
                                                    command=self.Switch_1)
            self.Switch_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

            self.Switch_2 = customtkinter.CTkSwitch(master=self.Left_Frame,
                                                    text="Switch 2",
                                                    command=self.Switch_2)
            self.Switch_2.grid(row=11, column=0, pady=10, padx=20, sticky="w")

            # ============ Right_Frame ============

            # configure grid layout (3x7)
            self.Right_Frame.rowconfigure((0, 1, 2, 3), weight=1)
            self.Right_Frame.rowconfigure(7, weight=10)
            self.Right_Frame.columnconfigure((0, 1), weight=1)
            self.Right_Frame.columnconfigure(2, weight=0)

            self.Label_1 = customtkinter.CTkLabel(master=self.Right_Frame,
                                                    text="Insert text" ,
                                                    height=135,
                                                    fg_color=("white", "gray38"),  # <- custom tuple-color
                                                    justify=tkinter.LEFT)

            self.Label_1.grid(column=0, row=0, columnspan=2, rowspan= 8, sticky="nwe", padx=15, pady=15)

            
            self.radio_var = tkinter.IntVar(value=0)                    


            self.RadioButton_1 = customtkinter.CTkRadioButton(master=self.Right_Frame,
                                                            variable=self.radio_var,
                                                            text="Radio Button 1",
                                                            command=self.RadioButton_1,
                                                            value=0)
            self.RadioButton_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

            self.RadioButton_2 = customtkinter.CTkRadioButton(master=self.Right_Frame,
                                                            variable=self.radio_var,
                                                            text="Radio Button 2",
                                                            command=self.RadioButton_2,
                                                            value=1)
            self.RadioButton_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

            self.RadioButton_3 = customtkinter.CTkRadioButton(master=self.Right_Frame,
                                                            variable=self.radio_var,
                                                            text="Radio Button 3",
                                                            command=self.RadioButton_3,
                                                            value=2)
            self.RadioButton_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

            

            self.slider_1 = customtkinter.CTkSlider(master=self.Right_Frame,
                                                    from_=0,
                                                    to=1,
                                                    number_of_steps=3,
                                                    )
            self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

            self.slider_2 = customtkinter.CTkSlider(master=self.Right_Frame,
                                                    )
            self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

            self.slider_3 = customtkinter.CTkSlider(master=self.Right_Frame,
                                                    )
            self.slider_3.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="we")

            self.slider_button_1 = customtkinter.CTkButton(master=self.Right_Frame,
                                                        height=25,
                                                        text="Slider 1 Button",
                                                        command=self.SliderButton_1)
            self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            self.slider_button_2 = customtkinter.CTkButton(master=self.Right_Frame,
                                                        height=25,
                                                        text="Slider 2 Button",
                                                        command=self.SliderButton_2)
            self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

            self.slider_button_3 = customtkinter.CTkButton(master=self.Right_Frame,
                                                        height=25,
                                                        text="Slider 3 Button",
                                                        command=self.SliderButton_3)
            self.slider_button_3.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")


            self.check_box_1 = customtkinter.CTkCheckBox(master=self.Right_Frame,
                                                        text="CheckBox 1",
                                                        command=self.CheckBox_1)
            self.check_box_1.grid(row=7, column=0, pady=10, padx=20, sticky="w")

            self.check_box_2 = customtkinter.CTkCheckBox(master=self.Right_Frame,
                                                        text="CheckBox 2",
                                                        command=self.CheckBox_2)
            self.check_box_2.grid(row=7, column=1, pady=10, padx=20, sticky="w")

            self.check_box_3 = customtkinter.CTkCheckBox(master=self.Right_Frame,
                                                        text="CheckBox 3",
                                                        command=self.CheckBox_3)
            self.check_box_3.grid(row=7, column=2, pady=10, padx=20, sticky="w")

            self.entry = customtkinter.CTkEntry(master=self.Right_Frame,
                                                width=120,
                                                placeholder_text="Text Input")
            self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

            self.Button_8 = customtkinter.CTkButton(master=self.Right_Frame,
                                                    text="Button 8",
                                                    command=self.ButtonEvent_8)
            self.Button_8.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        
        def ButtonEvent_2(self):
            print("Button 2 pressed")
        
        def ButtonEvent_3(self):
            print("Button 3 pressed")

        def ButtonEvent_4(self):
            print("Button 4 pressed")

        def ButtonEvent_5(self):
            print("Button 5 pressed")

        def ButtonEvent_6(self):
            print("Button 6 pressed")

        def ButtonEvent_7(self):
            print("Button 7 pressed")

        def ButtonEvent_8(self):
            print("Button 8 pressed")

        def RadioButton_1(self):
            print("RadioButton 1 pressed")
        
        def RadioButton_2(self):
            print("RadioButton 2 pressed")
        
        def RadioButton_3(self):
            print("RadioButton 3 pressed")

        def Switch_1(self):
            print("Switch 1 pressed")

        def Switch_2(self):
            print("Switch 2 pressed")

        def SliderButton_1(self):
            print("Slider Button 1 pressed")

        def SliderButton_2(self):
            print("Slider Button 2 pressed")
        
        def SliderButton_3(self):
            print("Slider Button 3 pressed")
        
        def CheckBox_1(self):
            print("CheckBox 1 pressed")

        def CheckBox_2(self):
            print("CheckBox 2 pressed")
        
        def CheckBox_3(self):
            print("CheckBox 3 pressed")

        def InsertCoords_ButtonEvent(self):
            #insert_coords_V6_hybrid.GUI()
            InsertCoordsWindow.win()
            print("Button pressed")

        def on_closing(self, event=0):
            self.destroy()

        def start(self):
            self.mainloop()


    if __name__ == "__main__":
        app = App()
        app.start()

GUI()