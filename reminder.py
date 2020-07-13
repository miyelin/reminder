from tkinter import *
import tkinter.messagebox

def main():
    def new(*args):
        def rm():
            try:
                notes[thiscount] = None
                t.destroy()
            except:
                t.destroy()
                text.destroy()

        def add():
            if text.get(1.0, END) != "" and text.get(1.0, END) != '\n':
                notes.append(text.get(1.0, END))
            else : tkinter.messagebox.showinfo("empty note", "the note is empty")

        thiscount = len(notes)
        if len(args) > 0: thiscount = args[1]
        if thiscount > 0: t = Toplevel()
        else: t = Frame(canvas).pack(side="top")
        nw = Frame(t)
        nw.pack()

        text = Text(nw, bg="lightpink", width=30, height=15)
        if len(args) > 0: text.insert(END, args[0])
        text.pack(padx=2, side="top")

        ad = Button(nw, text="+", command=add, bd=0 ).pack()
        rmv = Button(nw, text="-", command=rm, bd=0).pack()
    def sq():
        file = open("reminders.txt", "w")
        for a in notes:
            if a != None and a != "\n": file.write(a)
        quit(0)


    root = Tk()
    root.resizable(width=False, height=0)
    fr = open("reminders.txt", "r")
    canvas = Canvas(root, bd=0, width=32)
    canvas.pack()
    menu = Menu(root)
    menu.add_command(label="new reminder", command=new)
    menu.add_command(label="save and quit", command=sq)
    root.config(menu=menu)
    notes = []

    for i in fr:
        notes.append(i)

    if len(notes) > 0:
        for item in range(len(notes)):
            new(notes[item], item)
    else: new()

    root.mainloop()

main()
