import random

plans=['Rock','Paper','Scissors']

def getWinner(user, pc):
    if (user == 'Rock' and pc == 'Scissors') or (user == 'Paper' and pc == 'Rock') or ( user == 'Scissors' and pc == 'Paper'):

        return 'user'
    elif user == pc:
        return 'equal'
    else:
        return 'pc'

userScore=0
pcScore=0
def play(txtUser,lblmsg,lblScore,btnGame):
    global userScore,pcScore

    user=txtUser.get().capitalize()

    if user=='Exit':
        lblmsg.configure(text="Finished", font=("Helvetica", 16), fg="red", bg="Silver")
        btnGame.configure(state='disabled')
        txtUser.delete(0, 'end')
        txtUser.configure(state='disabled')
        return

    if user not in plans:
        lblmsg.configure(text="Wrong Input!!!",font=("Helvetica",15),fg="red",bg="Silver")
        txtUser.delete(0,'end')
        return
    pcPlan=random.choice(plans)
    result=getWinner(user,pcPlan)
    if result=='user':
        lblmsg.configure(text=f"Computer chose: '{pcPlan}' Awesome! You’re the Winner ",font=("Helvetica",15),fg="green",bg="Silver")
        userScore+=1
        lblScore.configure( text=f"Your Score:{userScore} *** Pc Score:{pcScore}")
    elif result=='equal':
        lblmsg.configure(text=f"Computer chose: '{pcPlan}' It's a Tie ", font=("Helvetica", 15), fg="blue", bg="Silver")
    else:
        lblmsg.configure(text=f"Computer chose: '{pcPlan}' Oops! The Computer Beat You ", font=("Helvetica", 15), fg="red", bg="Silver")
        pcScore+=1
        lblScore.configure(text=f"Your Score:{userScore} *** Pc Score:{pcScore}")
    txtUser.delete(0,'end')