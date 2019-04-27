import tkinter as tk
from tkinter import filedialog, messagebox
from core import gbk2utf8

def openfileCallBack(var):
    file_path = filedialog.askopenfilename()
    var.set(file_path)

def convert():
    inputFileLoc = inputVar.get()
    outputFileLoc = outputVar.get()
    if(len(inputFileLoc) == 0 and len(outputFileLoc) == 0):
        messagebox.showinfo( "Missing Parameters Error", "Missing input and output location parameters.")
        return
    if(len(inputFileLoc) == 0):
        messagebox.showinfo( "Missing Parameters Error", "Missing input location parameters.")
        return
    if(len(outputFileLoc) == 0):
        messagebox.showinfo( "Missing Parameters Error", "Missing output location parameters.")
        return
    try:
        gbk2utf8(inputFileLoc, outputFileLoc)
    except FileNotFoundError as e:
        messagebox.showinfo( "Conversion Error", str(e))
        return
    infoString = "The conversion was successful!\nOutput in : " + outputFileLoc
    messagebox.showinfo( "Success", infoString)


mainWin = tk.Tk()
mainWin.title("GBK2UTF8 tool")
mainWin.geometry("450x300")
mainWin.iconbitmap('icon.ico')
firstTextboxDesc = tk.Label(mainWin, text="The first textbox needs the location of GBK encoded file.").grid(row = 2, column = 0)
secondTextboxDesc = tk.Label(mainWin, text="The second textbox needs the location of output file.").grid(row = 4, column = 0)

inputVar = tk.StringVar()
outputVar = tk.StringVar()

intputTextbox = tk.Entry(mainWin, textvariable = inputVar, width = "50").grid(row = 3, column = 0, padx = 10)

button1 = tk.Button(mainWin, text = "select file...", command = lambda: openfileCallBack(inputVar)).grid(row = 3, column = 1)

outputTextbox = tk.Entry(mainWin, textvariable = outputVar, width = "50").grid(row = 5, column = 0, padx = 10)

button2 = tk.Button(mainWin, text = "select file...", command = lambda: openfileCallBack(outputVar)).grid(row = 5, column = 1)

button3 = tk.Button(mainWin, text = "Covert", command = convert).grid(row = 6)

mainWin.mainloop()