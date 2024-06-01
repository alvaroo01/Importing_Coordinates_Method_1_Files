from xml.dom.expatbuilder import parseFragment


def win():

    import tkinter
    import customtkinter
    from PIL import Image, ImageTk  # <- import PIL for the images
    import os
    from tkinter import filedialog
    from fileinput import filename
    from posixpath import dirname
    from xml.etree.ElementTree import tostring
    from tkinter import messagebox
    import InsertCoordsFunctions

    PATH = os.path.dirname(os.path.realpath(__file__))
    PathNames = ["","",""]
    customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTkToplevel()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
    app.geometry("450x350")
    app.title("ImportCoordinates")

##############################################################################################################################################
# Button Definitions
# Gets the pathnames and sends them to the CoordFunctions.py to be processed

    def buttonFolder():
        dirName = filedialog.askdirectory(initialdir="/", title="Select Folder")
        PathNames[0] = dirName
        ListFolder = customtkinter.CTkLabel(master=frame_1,
                                            text=PathNames[0],
                                            text_font=("Roboto Medium", -10),
                                            )  # font name and size in px
        ListFolder.grid(row=2, column=0, pady=5, padx=20, columnspan=3)

    def buttonFile():
        fileName = filedialog.askopenfilename(initialdir="/", title="Select File",  filetypes=[("Excel", ".xlsx")])
        PathNames[1] = fileName
        ListFile = customtkinter.CTkLabel(master=frame_1,
                                            text=PathNames[1],
                                            text_font=("Roboto Medium", -10),
                                            )  # font name and size in px
        ListFile.grid(row=4, column=0, columnspan=3, pady=5, padx=20, sticky="we")
    
    def buttonRun():
        PathNames[2] = EntryContent.get()
        if (PathNames[2] == ""):
            messagebox.showerror('ListNameError', 'Error: List name not specified!')
        elif (PathNames[1] == ""):
            messagebox.showerror('ExcelFileError', 'Error: Excel file not specified!')
        elif (PathNames[0] == ""):
            messagebox.showerror('ExcelFileError', 'Error: Project Directory not specified!')
        else:
            #Transfer().main(PathNames)~
            print(PathNames)
            InsertCoordsFunctions.main(PathNames)


##############################################################################################################################################
# Window format
# Build-up of the Window

    image_size = 20

    add_folder_image = ImageTk.PhotoImage(Image.open(PATH + "/test_images/add-folder.png").resize((image_size, image_size), Image.ANTIALIAS))
    add_list_image = ImageTk.PhotoImage(Image.open(PATH + "/test_images/add-list.png").resize((image_size, image_size), Image.ANTIALIAS))

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1, minsize=200)

    frame_1 = customtkinter.CTkFrame(master=app, width=250, height=40, corner_radius=15)
    frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    frame_1.grid_columnconfigure(0, weight=1)
    frame_1.grid_columnconfigure(1, weight=1)
    frame_1.grid_columnconfigure(2, weight=1)

    ButtonFolder = customtkinter.CTkButton(master=frame_1, image=add_folder_image, text="Add Folder", width=190, height=40,
                                    compound="right", command=buttonFolder)
    ButtonFolder.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    ButtonFile = customtkinter.CTkButton(master=frame_1, image=add_list_image, text="Add Excel", width=190, height=40,
                                    compound="right",
                                    command=buttonFile)
    ButtonFile.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

    ListNameLabel = customtkinter.CTkLabel(master=frame_1,
                                              text="Name The List",
                                              text_font=("Roboto Medium", -16),
                                              )  # font name and size in px
    ListNameLabel.grid(row=5, column=0, pady=10, padx=20, columnspan=3)

    EntryContent = customtkinter.CTkEntry(master=frame_1,
                                            width=120,
                                            placeholder_text="Name")
    EntryContent.grid(row=6, column=0, columnspan=3, pady=5, padx=20, sticky="we")

    ButtonRun = customtkinter.CTkButton(master=frame_1, text="RUN", width=190, height=40,
                                    compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                    command=buttonRun)
    ButtonRun.grid(row=7, column=1, columnspan=1, padx=20, pady=20, sticky="ew")

    app.mainloop()

