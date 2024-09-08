import tkinter

def main(msg):
    master = tkinter.Tk()
    master.title("Pravda GUI System")
    tkinter.Label(master, text=msg, font=("Helvetica", 36, "normal")).pack()
    master.mainloop()
