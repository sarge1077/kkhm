import tkinter
import os

def casino_start():
    casino_first.pack_forget()
    casino_start_btn.place_forget()
    game_choice.pack()
    game_choice.create_image(720,450,image=casino_choice_back)
    black_jak_btn.place(x=230,y=340)
    poker_btn.place(x=630,y=340)
    dice_btn.place(x=1030,y=340) 

def run_black(): 
    os.system("python blackjak.py")

def run_poker():
    os.system("python poker.py")
    
def run_dice():
    os.system("python dice.py")

casino_root=tkinter.Tk()
casino_root.title("CASINO")
casino_root.geometry("1440x900")
casino_root.resizable(True,True)

casino_first=tkinter.Canvas(casino_root,width=1440,height=900)
casino_first.pack()

game_choice=tkinter.Canvas(casino_root,width=1440,height=900,bg="white")

start_casino_btn=tkinter.PhotoImage(file="start_btn.png")

casino_start_btn=tkinter.Button(casino_root,image=start_casino_btn,command=casino_start)
casino_start_btn.place(x=680,y=560)

black_jak_start_btn=tkinter.PhotoImage(file="black_jak_start_btn.png")
poker_start_btn=tkinter.PhotoImage(file="poker_start_btn.png")
dice_start_btn=tkinter.PhotoImage(file="dice_start_btn.png")

black_jak_btn=tkinter.Button(casino_root,image=black_jak_start_btn,command=run_black)
poker_btn=tkinter.Button(casino_root,image=poker_start_btn,command=run_poker)
dice_btn=tkinter.Button(casino_root,image=dice_start_btn,command=run_dice)


casino_back=tkinter.PhotoImage(file="casino_start.png")
casino_first.create_image(720,450,image=casino_back)

casino_choice_back=tkinter.PhotoImage(file="casino_level_back.png")



casino_root.mainloop()