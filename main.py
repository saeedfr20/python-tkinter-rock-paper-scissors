import tkinter
from game_functions import *



# -----------------------------------main--------------------------------

win=tkinter.Tk()
win.title("Rock Paper Scissors Game")
win.geometry("600x500")
win.configure(bg="Silver")
lblOptions=tkinter.Label(win,text="Rock,Paper,Scissors",font=("Helvetica",20),bg="black", fg="red")
lblOptions.pack()


lblanswer=tkinter.Label(win,text="Your Plan:",font=("Helvetica",16),bg="black", fg="White")
lblanswer.pack()

txtUser=tkinter.Entry(win,width=20,font=("Helvetica ", 14),highlightthickness=4, highlightcolor='black')
txtUser.pack(pady=10)

lblmsg=tkinter.Label(win,text='',bg='Silver')
lblmsg.pack()


lblScore=tkinter.Label(win,text="Your Score:0 *** Pc Score:0",fg="black",bg="Gray",font=("Helvetica",14))
lblScore.pack()

btnGame=tkinter.Button(win,text="Play...",width=15,font=("Helvetica",16),bg="black",fg="yellow",command=lambda : play(txtUser,lblmsg,lblScore,btnGame))
btnGame.pack(pady=10)


win.mainloop()
