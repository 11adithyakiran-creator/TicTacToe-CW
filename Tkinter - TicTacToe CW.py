from tkinter import *
from tkinter import messagebox

mainWin = Tk()
mainWin.title('TicTacToe')
turn = 1
result = ''

def Win():
    global result
    #print(b1.cget('text'), b2.cget('text'), b3.cget('text'))

    if(b1.cget('text') == b2.cget('text') == b3.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b1.cget('text') == b2.cget('text') == b3.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b4.cget('text') == b5.cget('text') == b6.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b4.cget('text') == b5.cget('text') == b6.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b7.cget('text') == b8.cget('text') == b9.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b7.cget('text') == b8.cget('text') == b9.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b1.cget('text') == b4.cget('text') == b7.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b1.cget('text') == b4.cget('text') == b7.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b2.cget('text') == b5.cget('text') == b8.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b2.cget('text') == b5.cget('text') == b8.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b3.cget('text') == b6.cget('text') == b9.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b3.cget('text') == b6.cget('text') == b9.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b1.cget('text') == b5.cget('text') == b9.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b1.cget('text') == b5.cget('text') == b9.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b3.cget('text') == b5.cget('text') == b7.cget('text') == 'X'):
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()

    elif(b3.cget('text') == b5.cget('text') == b7.cget('text') == 'O'):
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', result)
        mainWin.destroy()
    
    elif(b1.cget('text') != '' and b2.cget('text') != '' and b3.cget('text') != '' and b4.cget('text') != '' and b5.cget('text') != '' and b6.cget('text') != '' and b7.cget('text') != '' and b8.cget('text') != '' and b9.cget('text') != ''):
        result = "Draw"
        messagebox.showinfo('Result', result)
        mainWin.destroy()

def b1click():
    global turn
    myText = b1.cget('text')

    if(myText == ''):
        if(turn == 1):
            b1.configure(text = 'X')
            turn = 2
        else:
            b1.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b2Click():
    global turn
    myText = b2.cget('text')
    if(myText == ''):
        if(turn == 1):
            b2.configure(text = 'X')
            turn = 2
        else:
            b2.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b3Click():
    global turn
    myText = b3.cget('text')
    if(myText == ''):
        if(turn == 1):
            b3.configure(text = 'X')
            turn = 2
        else:
            b3.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b4Click():
    global turn
    myText = b4.cget('text')
    if(myText == ''):
        if(turn == 1):
            b4.configure(text = 'X')
            turn = 2
        else:
            b4.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b5Click():
    global turn
    myText = b5.cget('text')
    if(myText == ''):
        if(turn == 1):
            b5.configure(text = 'X')
            turn = 2
        else:
            b5.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b6Click():
    global turn
    myText = b6.cget('text')
    if(myText == ''):
        if(turn == 1):
            b6.configure(text = 'X')
            turn = 2
        else:
            b6.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b7Click():
    global turn
    myText = b7.cget('text')
    if(myText == ''):
        if(turn == 1):
            b7.configure(text = 'X')
            turn = 2
        else:
            b7.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b8Click():
    global turn
    myText = b8.cget('text')
    if(myText == ''):
        if(turn == 1):
            b8.configure(text = 'X')
            turn = 2
        else:
            b8.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

def b9Click():
    global turn
    myText = b9.cget('text')
    if(myText == ''):
        if(turn == 1):
            b9.configure(text = 'X')
            turn = 2
        else:
            b9.configure(text = 'O')
            turn = 1
    Lbl.configure(text = 'Player ' + str(turn) + ' Turn')
    Win()

b1 = Button(mainWin, text = '', width = 5, command = b1click)
b1.grid(column = 0, row = 0, padx = 5, pady = 5)

b2 = Button(mainWin, text = '', width = 5, command = b2Click)
b2.grid(column = 1, row = 0, padx = 5, pady = 5)

b3 = Button(mainWin, text = '', width = 5, command = b3Click)
b3.grid(column = 2, row = 0, padx = 5, pady = 5)

b4 = Button(mainWin, text = '', width = 5, command = b4Click)
b4.grid(row = 1, column = 0, padx = 5, pady = 5)

b5 = Button(mainWin, text = '', width = 5, command = b5Click)
b5.grid(row = 1, column = 1, padx = 5, pady = 5)

b6 = Button(mainWin, text = '', width = 5, command = b6Click)
b6.grid(row = 1, column = 2, padx = 5, pady = 5)

b7 = Button(mainWin, text = '', width = 5, command = b7Click)
b7.grid(row = 2, column = 0, padx = 5, pady = 5)

b8 = Button(mainWin, text = '', width = 5, command = b8Click)
b8.grid(row = 2, column = 1, padx = 5, pady = 5)

b9 = Button(mainWin, text = '', width = 5, command = b9Click)
b9.grid(column = 2, row = 2, padx = 5, pady = 5)

Lbl = Label(mainWin, text = 'Player ' + str(turn) + ' Turn')
Lbl.grid(row = 3, column = 1, padx = 10, pady = 10)

mainWin.mainloop()