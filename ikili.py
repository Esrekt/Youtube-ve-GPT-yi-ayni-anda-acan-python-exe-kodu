import tkinter as tk
from tkinter import *
import webview
pencere=Tk()
pencere.geometry("900x450")
webview.create_window("youtube","https://www.youtube.com/")
webview.create_window("gpt","https://chatgpt.com/")
webview.start()


mainloop()




