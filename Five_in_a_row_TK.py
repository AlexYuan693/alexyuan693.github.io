from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import Menu
from Chess_state import chess
import time
# from playsound import playsound
import simpleaudio as sa
def playsound():
    filename = 'chess_sound.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
chess_order=[]
game_over=False
name_of_player=""
step_size=16
turn=True
window = Tk()
image = PhotoImage(file="resize_board.gif")
window.title("Five In a Row")
window.geometry('1080x1080')
lbl = Label(window,text='', font=("Arial Bold",16))
lbl.grid(column=4,row=0)
# txt = Entry(window, width=10)
# txt.grid(column=1,row=2)
# lbl2 = Label(window,text="Name",font=("Arial Bold",20))
# lbl2.grid(column=0,row=2)
# combo = Combobox(window)
# combo['values']=("Easy","Medium","Hard")
# combo.current(1)
# combo.grid(column=0,row=0)
def show_move():
    if turn==True:
        lbl.configure(text="Black moves")
    else:
        lbl.configure(text="White moves")
    window.update()
canvas = Canvas(window,bg='white', height="700",width="700")
canvas.place(x=0,y=50)
state_of_grid=[]
for x in range (26):
    for y in range (26):
        state_of_grid.append(0)
def drawboard():
    canvas.create_image(0,0,image = image,anchor=NW)
    for i in range (16):
        x = 50+(i*40)
        canvas.create_line(x,50,x,650)
    for p in range (16):
        y = 50+(p*40)
        canvas.create_line(50,y,650,y)
def Judgewin (): 
    #not determined (0), black win (1), white win (2)
    for column in range (step_size):
        for x in range (step_size):
            state=column*step_size+x
            if state_of_grid[state]=="black":
                if state_of_grid[state+1]=="black" and state_of_grid[state+2]=="black" and state_of_grid[state+3]=="black" and state_of_grid[state+4]=="black":
                    return 1
            if state_of_grid[state]=="white":
                if state_of_grid[state+1]=="white" and state_of_grid[state+2]=="white" and state_of_grid[state+3]=="white" and state_of_grid[state+4]=="white":
                    return 2
    for row in range (step_size):
        for y in range (step_size-4):
            state=y*step_size+row
            if state_of_grid[state]=="black":
                if state_of_grid[state+step_size]=="black" and state_of_grid[state+2*step_size]=="black" and state_of_grid[state+3*step_size]=="black" and state_of_grid[state+4*step_size]=="black":
                    return 1
            if state_of_grid[state]=="white":
                if state_of_grid[state+step_size]=="white" and state_of_grid[state+2*step_size]=="white" and state_of_grid[state+3*step_size]=="white" and state_of_grid[state+4*step_size]=="white":
                    return 2

    for row in range (step_size):
        for y in range (step_size):
            state=y*step_size+row
            if state_of_grid[state]=="black":
                if state_of_grid[state+step_size+1]=="black" and state_of_grid[state+2*step_size+2]=="black" and state_of_grid[state+3*step_size+3]=="black" and state_of_grid[state+4*step_size+4]=="black":
                    return 1
            if state_of_grid[state]=="white":
                if state_of_grid[state+step_size+1]=="white" and state_of_grid[state+2*step_size+2]=="white" and state_of_grid[state+3*step_size+3]=="white" and state_of_grid[state+4*step_size+4]=="white":
                    return 2

    for row in range (step_size):
        for y in range (step_size):
            state=y*step_size+row
            if state_of_grid[state]=="black":
                if state_of_grid[state+step_size-1]=="black" and state_of_grid[state+2*step_size-2]=="black" and state_of_grid[state+3*step_size-3]=="black" and state_of_grid[state+4*step_size-4]=="black":
                    return 1
            if state_of_grid[state]=="white":
                if state_of_grid[state+step_size-1]=="white" and state_of_grid[state+2*step_size-2]=="white" and state_of_grid[state+3*step_size-3]=="white" and state_of_grid[state+4*step_size-4]=="white":
                    return 2
    return 0
        
def reset ():
    global game_over, turn
    game_over=False
    turn=True
    for x in range (16):
        for y in range (16):
            state=x*16+y
            state_of_grid[state]=0
    canvas.delete('all')
    chess_order.clear()
    drawboard()
    show_move()

def start_clicked():
    # global name_of_player
    # entered_name = txt.get()
    # if entered_name == "":
    #     messagebox.showinfo('Do you have a name?','Enter your name')
    #     return
    # lbl.configure(text="Welcome "+ txt.get())
    # name_of_player=entered_name
    # print (entered_name)
    reset()

def clickclick (event):
    global game_over
    if game_over==True:
        messagebox.showinfo('Game Over','Please press "Start Game"')
        return
    # #clicked()
    # print (name_of_player)
    # if name_of_player=="":
    #     #messagebox.showinfo('reminder','please enter your name')
    #     return
    x,y=event.x,event.y
    row=(y-30)//40
    column=(x-30)//40
    if column<0 or row<0 or column>15 or row>15:
        return
    x1=column*40+50
    y1=row*40+50
    state=column*step_size+row
    global turn
    if state_of_grid[state]=="black" or state_of_grid[state]=="white":
        messagebox.showwarning("Warning","Invalid move")
        return
    if turn == True:
        fillcolor='black'
        outline_color='black'
        state_of_grid[state]="black"
        turn = False
    else:
        fillcolor='white'
        outline_color='white'
        state_of_grid[state]="white"
        turn = True
    tag_name=str(column)+"*"+str(row)
    canvas.create_oval(x1-18,y1-18,x1+18,y1+18,fill=fillcolor,outline=outline_color,tag=tag_name)
    # playsound('chess_sound.wav')
    last_chess=chess(fillcolor,column,row)
    chess_order.append(last_chess)
    window.update()
    playsound()
    #print (state_of_grid)
    if Judgewin()==1:
        messagebox.showinfo("Congratulations","Black wins!!")
    if Judgewin()==2:
        messagebox.showinfo("Congratulations","White wins!!")
    if Judgewin()==1 or Judgewin()==2:
        m=messagebox.askyesno("New Game","Do you want to start a new game?")
        if m==True:
            reset()
        if m==False:
            game_over=True
    show_move()


drawboard()
canvas.bind("<Button-1>",clickclick)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New',command=start_clicked)
menu.add_cascade(label='File',menu=new_item)
window.config(menu=menu)

btn = Button(window, text="Start Game", command=start_clicked)
btn.grid(column=0,row=0)
def save_clicked():
    file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),))
    chess_data_file = open(file,'w')
    for x in chess_order:
        order_name=str(x.color)+","+str(x.column)+","+str(x.row)+'\n'
        chess_data_file.write(order_name)
    chess_data_file.close()
    print (file)
    lbl.configure(text="The game has been saved to "+file)
btn2 = Button(window,text="Save Game",command=save_clicked)
btn2.grid(column=1,row=0)
def undo_clicked():
    if len(chess_order)==0:
        messagebox.showinfo("Warning","There is no chess on the board")
        return
    global turn 
    print ("last move removed")
    for c in chess_order:
        print (c.color,c.column,c.row)
    print (len(chess_order))
    chess_last=chess_order.pop()
    print (len(chess_order))
    tag_name=str(chess_last.column)+"*"+str(chess_last.row)
    canvas.delete(tag_name)
    state=chess_last.column*step_size+chess_last.row
    state_of_grid[state]=0
    if chess_last.color=="white":
        turn=False
    if chess_last.color=="black":
        turn=True
    global game_over
    game_over=False
    lbl.configure(text="Last move was removed")
    window.update()
    time.sleep(0.75)
    lbl.configure(text="")
    show_move()
btn3 = Button(window,text="Undo last move",command=undo_clicked)
btn3.grid(column=2,row=0)
def open_clicked():
    reset()
    file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),))
    chess_data_file = open(file,'r')
    strText = chess_data_file.read()
    strText_order=strText.split("\n")
    strText_order.pop()
    for n in strText_order:
        ints = n.split(",")
        print (ints)
        fillcolor=ints[0]
        column=int(ints[1])
        row=int(ints[2])
        x1=column*40+50
        y1=row*40+50
        tag_name=str(column)+"*"+str(row)
        canvas.create_oval(x1-18,y1-18,x1+18,y1+18,fill=fillcolor,tag=tag_name)
        window.update()
        last_chess=chess(fillcolor,column,row)
        global turn
        if fillcolor=="white":
            turn=True
        if fillcolor=="black":
            turn=False
        chess_order.append(last_chess)
        show_move()
        time.sleep(0.5)
    print (strText_order)
    chess_data_file.close()
    show_move()
btn4 = Button(window,text="Open Game",command=open_clicked)
btn4.grid(column=1,row=1)
show_move()
window.mainloop()

