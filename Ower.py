from doctest import master
from logging import shutdown
from multiprocessing.pool import ApplyResult
import subprocess
from tkinter import*
import tkinter
from turtle import width
import webbrowser
import customtkinter
import os
import time
import tkinter.font as font
soundPercentage = 100
loaded = False

def gui():
    global soundPercentage
    global osShutdown
    global loaded
    customtkinter.set_appearance_mode("Dark")  
    customtkinter.set_default_color_theme("blue")  



    app = customtkinter.CTk()  
    app.geometry("1000x500")
    app.title("Ower UI 1.0 :D")

    title = customtkinter.CTkLabel(master=app,text="Ower OS 1.0",bg="darkblue")
    title.config(font=("Courier", 30))
    title.pack()

    def browserButton():
        def youtubeButton():
            webbrowser.open("https://youtube.com")
            browserList.destroy()
        def googleButton():
            webbrowser.open("https://google.com")
            browserList.destroy()
        def customSiteButton():
            print("Enter URL in TERMINAL")
            get_url = input("")
            webbrowser.open(get_url)
            browserList.destroy()
            #under here is an unfinish code
            #SiteOpening = customtkinter.CTk()
            #SiteOpening.title("Open Site")
            #SiteOpening.geometry("350x120")
            #def GetUrl():
                #textBox = textBox.get("1.0",customtkinter.END)
                #webbrowser.open(textBox)
            #textBox = customtkinter.CTkEntry(master=SiteOpening,width=500,height=30)
            #textBox.pack(pady=35) 
            #openButton = customtkinter.CTkButton(master=SiteOpening,text="Open",command=GetUrl)
            #openButton.place(relx=0.5,rely=0.88,anchor=tkinter.CENTER)
            #SiteOpening.mainloop()
        def gmailButton():
            webbrowser.open("https://gmail.com")
            browserList.destroy()

        browserList = customtkinter.CTk()
        browserList.title("Browser Lists")
        browserList.geometry("300x300")

        google = customtkinter.CTkButton(master=browserList,text="    Google    ",command=googleButton)
        google.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

        youtube = customtkinter.CTkButton(master=browserList,text="    Youtube    ",command=youtubeButton)
        youtube.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)

        gmail = customtkinter.CTkButton(master=browserList,text="    Gmail    ",command=gmailButton)
        gmail.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)


        openCustomSite = customtkinter.CTkButton(master=browserList,text="    Custom    ",command=customSiteButton)
        openCustomSite.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

        browserList.mainloop()

    def exitButton():
        global osShutdown
        app.destroy()
        osShutdown = True
    def appButton():
        appLists = customtkinter.CTk()
        appLists.geometry("500x500")
        appLists.title("App Lists")
        appTitle = customtkinter.CTkLabel(master=appLists,text="App Lists")
        appTitle.config(font=("Courier",30))
        appTitle.pack()
        def calc():
            calc = customtkinter.CTk()
            calc.geometry("400x450")
            calc.mainloop()
        calculator = customtkinter.CTkButton(master=appLists,text="         Calculator         ",command=calc)
        calculator.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
        appLists.mainloop()
    def settingsButton():
        def switchThemeLight():
            customtkinter.set_appearance_mode("Light")
        def switchThemeDark():
            customtkinter.set_appearance_mode("Dark")
        settingsWindow = customtkinter.CTk()
        settingsWindow.title("Settings")
        settingsWindow.geometry("750x650")
        settingsText = customtkinter.CTkLabel(master=settingsWindow,text="Settings")
        settingsText.pack()
        settingsText.config(font=("Courier",30))
        themeLabel = customtkinter.CTkLabel(master=settingsWindow,text="Themes")
        themeLabel.pack(pady=45)
        themeLabel.config(font=("Courier",20))
        themeSwitchLight = customtkinter.CTkButton(master=settingsWindow,text="          Light Theme         ",width=50,height=30,command=switchThemeLight)
        themeSwitchLight.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
        themeSwitchDark = customtkinter.CTkButton(master=settingsWindow,text="           Dark Theme         ",width=50,height=30,command=switchThemeDark)
        themeSwitchDark.place(relx=0.5,rely=0.26,anchor=tkinter.CENTER)
        settingsWindow.mainloop()
    def shutdownButton():
        shutdownConfirmWindow = customtkinter.CTk()
        shutdownConfirmWindow.geometry("650x250")
        shutdownConfirmWindow.title("Are you sure you want to shutdown?")
        def restart():
            os.system("shutdown /r /t 5")
            print("System will restart in 5 seconds")
        def cancel():
            print("System restart has been canceled")
            shutdownConfirmWindow.destroy()
        label = customtkinter.CTkLabel(master=shutdownConfirmWindow,text="ARE YOU SURE YOU WANT TO SHUT DOWN?")
        label.pack(pady=10)
        label.config(font=("Courier",20))
        shutdownConfirmYes = customtkinter.CTkButton(master=shutdownConfirmWindow,text="          Yes         ",command=restart)
        shutdownConfirmYes.place(relx=0.3,rely=0.5,anchor=tkinter.CENTER)
        shutdownConfirmNo = customtkinter.CTkButton(master=shutdownConfirmWindow,text="          No          ",command=cancel)
        shutdownConfirmNo.place(relx=0.7,rely=0.5,anchor=tkinter.CENTER)
        shutdownConfirmWindow.mainloop()

    browser = customtkinter.CTkButton(master=app, text="          Browsers          ",width=40,height=40, command=browserButton)
    browser.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)

    exit = customtkinter.CTkButton(master=app, text="          Exit          ",width=40,height=40, command=exitButton)
    exit.place(relx=0.9,rely=0.9,anchor=tkinter.CENTER)

    apps = customtkinter.CTkButton(master=app, text="          Apps          ",width=40,height=40, command=appButton)
    apps.place(relx=0.09,rely=0.3,anchor=tkinter.CENTER)

    settings = customtkinter.CTkButton(master=app, text="       Settings      ",width=40,height=40, command=settingsButton)
    settings.place(relx=0.9,rely=0.8,anchor=tkinter.CENTER)
    
    ShutDown = customtkinter.CTkButton(master=app, text="       Shutdown      ",width=40,height=40, command=shutdownButton) 
    ShutDown.place(relx=0.095,rely=0.4,anchor=tkinter.CENTER)

    app.mainloop()

osShutdown = False

gui()
if osShutdown == True:
    exit()

#compile after every update
