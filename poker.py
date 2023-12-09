import tkinter
import random

ft="Times New Roman"

poker_coin=15
poker_betting_coin=0

max=0

cp_point=0
pp_point=0

cp_txt=''
pp_txt=''

cp_card=[]  #컴퓨터 카드 모음(5장)
pp_card=[]  #플레이어 카드 모음(5장)

card_image_file=[]  #포커 카드 이미지 배열(52장)

pattern=['C','D','H','S']   #포커 카드 문양
number=[2,3,4,5,6,7,8,9,'A','J','K','Q','X']    #포커 카드 숫자

poker_card=[
    '2C','3C','4C','5C','6C','7C','8C','9C','XC','JC','QC','KC','AC',    #클로버
    '2H','3H','4H','5H','6H','7H','8H','9H','XH','JH','QH','KH','AH',    #하트 
    '2D','3D','4D','5D','6D','7D','8D','9D','XD','JD','QD','KD','AD',    #다이아
    '2S','3S','4S','5S','6S','7S','8S','9S','XS','JS','QS','KS','AS'     #스페이드
]
poker_card.sort()

def exit_level_poker():
    gameroot.quit()

def exit_poker_game():
    global poker_coin
    poker_coin=15
    coin_label["text"]=poker_coin
    poker_level_exit_btn.place(x=30,y=30)
    delete_card()
    poker_back_canvas.pack_forget()
    poker_level_canvas.pack()
    re_poker_btn.place_forget()
    coin_label.place_forget()
    status_label.place_forget()
    easy_poker_start_btn.place(x=260,y=600)
    normal_poker_start_btn.place(x=620,y=600)
    hard_poker_start_btn.place(x=980,y=600)
    pp_label.place_forget()
    cp_label.place_forget()
    all_in_btn.place_forget()
    raise_btn.place_forget()
    call_btn.place_forget()
    die_btn.place_forget()
    poker_exit_btn.place_forget()

def setting_card():     #컴퓨터와 플레이어 카드 세팅
    deck=random.sample(poker_card,10)

    for i in range(5):
        cp_card.append(deck[i])
        pp_card.append(deck[i+5])
        
    cp_card.sort()
    pp_card.sort()
        
def suffle_card():
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,250,image=card_back)
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,600,image=card_image_file[poker_card.index(pp_card[i])])
        
def delete_card():
    for i in range(5):
        cp_card.pop(0)
        pp_card.pop(0)
    
def cp_or_pp(list1,num):
    global cp_point,pp_point,cp_txt,pp_txt
    if list1==cp_card:
        cp_point=num
        if num>=13:
            cp_txt='1.로얄 스트레이트 플러쉬'
        elif num>=12:
            cp_txt='2.백 스트레이트 플러쉬'
        elif num>=11:
            cp_txt='3.스트레이트 플러쉬'
        elif num>=10:
            cp_txt='4.포커스'
        elif num>=9:
            cp_txt='5.풀 하우스'
        elif num>=8:
            cp_txt='6.플러쉬'
        elif num>=7:
            cp_txt='7.마운틴'
        elif num>=6:
            cp_txt='8.백 스트레이트'
        elif num>=5:
            cp_txt='9.스트레이트'
        elif num>=4:
            cp_txt='10.트리플'
        elif num>=3:
            cp_txt='11.투 페어'
        elif num>=2:
            cp_txt='12.원 페어'
        elif num>=1:
            cp_txt='13.노 페어'
    if list1==pp_card:
        pp_point=num
        if num>=13:
            pp_txt='1.로얄 스트레이트 플러쉬'
        elif num>=12:
            pp_txt='2.백 스트레이트 플러쉬'
        elif num>=11:
            pp_txt='3.스트레이트 플러쉬'
        elif num>=10:
            pp_txt='4.포커스'
        elif num>=9:
            pp_txt='5.풀 하우스'
        elif num>=8:
            pp_txt='6.플러쉬'
        elif num>=7:
            pp_txt='7.마운틴'
        elif num>=6:
            pp_txt='8.백 스트레이트'
        elif num>=5:
            pp_txt='9.스트레이트'
        elif num>=4:
            pp_txt='10.트리플'
        elif num>=3:
            pp_txt='11.투 페어'
        elif num>=2:
            pp_txt='12.원 페어'
        elif num>=1:
            pp_txt='13.노 페어'
        
def case(list2,num1,n):
    if list2[n][0]=='A':                                                                                   
        cp_or_pp(list2,num1+0.95)
    elif list2[n][0]=="K":
        cp_or_pp(list2,num1+0.9)
    elif list2[n][0]=='Q':
        cp_or_pp(list2,num1+0.85)
    elif list2[n][0]=='J':
        cp_or_pp(list2,num1+0.8)
    elif list2[n][0]=='X':
        cp_or_pp(list2,num1+0.75)
    else :
        cp_or_pp(list2,num1+int(list2[n][0])*0.05)    

def  play_poker(list):
    global cp_point,pp_point
    if list[0][1]==list[1][1] and list[0][1]==list[2][1] and list[0][1]==list[3][1] and list[0][1]==list[4][1]:
        if list[0][0]=='A' and list[1][0]=='J' and list[2][0]=='K' and list[3][0]=='Q' and list[4][0]=='X':    #1.로얄 스트레이트 플러쉬,포인트=13
            cp_or_pp(list,13)
        elif list[0][0]=='2' and list[1][0]=='3' and list[2][0]=='4' and list[3][0]=='5' and list[4][0]=='A':    #2.백스트레이트 플러쉬,포인트=12
            cp_or_pp(list,12)
        elif list[0][0]=='2' and list[1][0]=='3' and list[2][0]=='4' and list[3][0]=='5' and list[4][0]=='6':    #3.스트레이트 플러쉬(2),포인트=11.1
            cp_or_pp(list,11.1)
        elif list[0][0]=='3' and list[1][0]=='4' and list[2][0]=='5' and list[3][0]=='6' and list[4][0]=='6':    #3.스트레이트 플러쉬(3),포인트=11.2
            cp_or_pp(list,11.2)
        elif list[0][0]=='4' and list[1][0]=='5' and list[2][0]=='6' and list[3][0]=='7' and list[4][0]=='8':    #3.스트레이트 플러쉬(4),포인트=11.3
            cp_or_pp(list,11.3)
        elif list[0][0]=='5' and list[1][0]=='6' and list[2][0]=='7' and list[3][0]=='8' and list[4][0]=='9':    #3.스트레이트 플러쉬(5),포인트=11.4
            cp_or_pp(list,11.4)
        elif list[0][0]=='6' and list[1][0]=='7' and list[2][0]=='8' and list[3][0]=='9' and list[4][0]=='X':    #3.스트레이트 플러쉬(6),포인트=11.5
            cp_or_pp(list,11.5)
        elif list[0][0]=='7' and list[1][0]=='8' and list[2][0]=='9' and list[3][0]=='J' and list[4][0]=='X':    #3.스트레이트 플러쉬(7),포인트=11.6
            cp_or_pp(list,11.6)
        elif list[0][0]=='8' and list[1][0]=='9' and list[2][0]=='J' and list[3][0]=='Q' and list[4][0]=='X':    #3.스트레이트 플러쉬(8),포인트=11.7
            cp_or_pp(list,11.7)
        elif list[0][0]=='9' and list[1][0]=='J' and list[2][0]=='K' and list[3][0]=='Q' and list[4][0]=='X':    #3.스트레이트 플러쉬(9),포인트=11.8
            cp_or_pp(list,11.8)
        else:                                                                                                    #6.플러쉬,포인트=8
            cp_or_pp(list,8)
    else:
        if list[0][0]==list[1][0] and list[0][0]==list[2][0] and list[0][0]==list[3][0]:                          #4.포카드,포인트=10.n
            case(list,10,0)
        elif list[1][0]==list[2][0] and list[1][0]==list[3][0] and list[1][0]==list[4][0]:                        #4.포카드,포인트=10.n 
            case(list,10,1) 
        elif list[0][0]==list[1][0] and list[0][0]==list[2][0] and list[3][0]==list[4][0]:                        #5.풀하우스,포인트=9.n
            case(list,9,0)
        elif list[0][0]==list[1][0] and list[2][0]==list[3][0] and list[2][0]==list[4][0]:                        #5.풀하우스,포인트=9.n
            case(list,9,2)
        elif list[0][0]=='A' and list[1][0]=='J' and list[2][0]=='K' and list[3][0]=='Q' and list[4][0]=='X':       #7.마운틴,포인트=7
            cp_or_pp(list,7)
        elif list[0][0]=='2' and list[1][0]=='3' and list[2][0]=='4' and list[3][0]=='5' and list[4][0]=='A':       #8.백스트레이트,포인트=6  
            cp_or_pp(list,6)
        elif list[0][0]=='2' and list[1][0]=='3' and list[2][0]=='4' and list[3][0]=='5' and list[4][0]=='6':    #9.스트레이트(2),포인트=5.1
            cp_or_pp(list,5.1)
        elif list[0][0]=='3' and list[1][0]=='4' and list[2][0]=='5' and list[3][0]=='6' and list[4][0]=='6':    #9.스트레이트(3),포인트=5.2
            cp_or_pp(list,5.2)
        elif list[0][0]=='4' and list[1][0]=='5' and list[2][0]=='6' and list[3][0]=='7' and list[4][0]=='8':    #9.스트레이트(4),포인트=5.3
            cp_or_pp(list,5.3)
        elif list[0][0]=='5' and list[1][0]=='6' and list[2][0]=='7' and list[3][0]=='8' and list[4][0]=='9':    #9.스트레이트(5),포인트=5.4
            cp_or_pp(list,5.4)
        elif list[0][0]=='6' and list[1][0]=='7' and list[2][0]=='8' and list[3][0]=='9' and list[4][0]=='X':    #9.스트레이트(6),포인트=5.5
            cp_or_pp(list,5.5)
        elif list[0][0]=='7' and list[1][0]=='8' and list[2][0]=='9' and list[3][0]=='J' and list[4][0]=='X':    #9.스트레이트(7),포인트=5.6
            cp_or_pp(list,5.6)
        elif list[0][0]=='8' and list[1][0]=='9' and list[2][0]=='J' and list[3][0]=='Q' and list[4][0]=='X':    #9.스트레이트(8),포인트=5.7
            cp_or_pp(list,5.7)
        elif list[0][0]=='9' and list[1][0]=='J' and list[2][0]=='K' and list[3][0]=='Q' and list[4][0]=='X':    #9.스트레이트(9),포인트=5.8
            cp_or_pp(list,5.8)
        elif list[0][0]==list[1][0] and list[0][0]==list[2][0]:                                                  #10.트리플,포인트=4.n
            case(list,4,0)
        elif list[1][0]==list[2][0] and list[1][0]==list[3][0]:                                                  #10.트리플,포인트=4.n
            case(list,4,1)
        elif list[2][0]==list[3][0] and list[2][0]==list[4][0]:                                                  #10.트리플,포인트=4.n
            case(list,4,2)
        elif list[0][0]==list[1][0] and list[2][0]==list[3][0]:                                                  #11.투페어,포인트=3.n
            if list[0][0]=='A' or list[2][0]=='A':
                cp_or_pp(list,3.95)
            elif list[0][0]=='K' or list[2][0]=='K':
                cp_or_pp(list,3.9)
            elif list[0][0]=='Q' or list[2][0]=='Q':
                cp_or_pp(list,3.85)
            elif list[0][0]=='J' or list[2][0]=='J':
                cp_or_pp(list,3.8)
            elif list[0][0]=='X' or list[2][0]=='X':
                cp_or_pp(list,3.75)
            elif list[0][0] >list[2][0]:
                case(list,3,0)
            else:
                case(list,3,2)
        elif list[1][0]==list[2][0] and list[3][0]==list[4][0]:                                                  #11.투페어,포인트=3.n
            if list[1][0]=='A' or list[3][0]=='A':
                cp_or_pp(list,3.95)
            elif list[1][0]=='K' or list[3][0]=='K':
                cp_or_pp(list,3.9)
            elif list[1][0]=='Q' or list[3][0]=='Q':
                cp_or_pp(list,3.85)
            elif list[1][0]=='J' or list[3][0]=='J':
                cp_or_pp(list,3.8)
            elif list[1][0]=='X' or list[3][0]=='X':
                cp_or_pp(list,3.75)
            elif list[1][0] >list[3][0]:
                case(list,3,1)
            else:
                case(list,3,3)
        elif list[0][0]==list[1][0] and list[3][0]==list[4][0]:                                                  #11.투페어,포인트=3.n
            if list[0][0]=='A' or list[3][0]=='A':
                cp_or_pp(list,3.95)
            elif list[0][0]=='K' or list[3][0]=='K':
                cp_or_pp(list,3.9)
            elif list[0][0]=='Q' or list[3][0]=='Q':
                cp_or_pp(list,3.85)
            elif list[0][0]=='J' or list[3][0]=='J':
                cp_or_pp(list,3.8)
            elif list[0][0]=='X' or list[3][0]=='X':
                cp_or_pp(list,3.75)
            elif list[0][0] >list[3][0]:
                case(list,3,0)
            else:
                case(list,3,4)
        elif list[0][0]==list[1][0]:                                                                             #12.원페어,포인트=2.n
            case(list,2,0)
        elif list[1][0]==list[2][0]:                                                                             #12.원페어,포인트=2.n
            case(list,2,1)
        elif list[2][0]==list[3][0]:                                                                             #12.원페어,포인트=2.n
            case(list,2,2)
        elif list[3][0]==list[4][0]:                                                                             #12.원페어,포인트=2.n
            case(list,2,3)
        else:                                                                                                    #13.노페어,포인트=1.n
            global max
            k=0
            for i in range(4):
                if list[i][0]>list[i+1][0]:
                    max=list[i][0]
                    k=i
                else:
                    max=list[i+1][0]
                    k=i+1
            case(list,1,k)              
            if list[0][0]=='A' or list[1][0]=='A' or list[2][0]=='A' or list[3][0]=='A' or list[4][0]=='A':
                cp_or_pp(list,1.95)
            elif list[0][0]=='K' or list[1][0]=='K' or list[2][0]=='K' or list[3][0]=='K' or list[4][0]=='K':
                cp_or_pp(list,1.9)
            elif list[0][0]=='Q' or list[1][0]=='Q' or list[2][0]=='Q' or list[3][0]=='Q' or list[4][0]=='Q':
                cp_or_pp(list,1.85)
            elif list[0][0]=='J' or list[1][0]=='J' or list[2][0]=='J' or list[3][0]=='J' or list[4][0]=='J':
                cp_or_pp(list,1.8)   
            elif list[0][0]=='X' or list[1][0]=='X' or list[2][0]=='X' or list[3][0]=='X' or list[4][0]=='X':
                cp_or_pp(list,1.75)   
                
def start_easy_poker():      #포커 게임 켄버스에 카드 이미지 출력
    global poker_betting_coin
    poker_betting_coin=2
    level_delete()
    
def start_normal_poker():      #포커 게임 켄버스에 카드 이미지 출력
    global poker_betting_coin
    poker_betting_coin=3
    level_delete()
    
def start_hard_poker():      #포커 게임 켄버스에 카드 이미지 출력
    global poker_betting_coin
    poker_betting_coin=4
    level_delete()
    
def all_in_betting():
    global poker_coin,poker_betting_coin
    all_in_btn.place_forget()
    raise_btn.place_forget()
    call_btn.place_forget()
    die_btn.place_forget()
    
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,250,image=card_image_file[poker_card.index(cp_card[i])])
        
    cp_label.place(x=250,y=320)
    
    if pp_point>cp_point:
        poker_coin*=2
        status_label["text"]="플레이어 승리"
        coin_label["text"]=poker_coin
    elif pp_point<cp_point:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gameover)
        coin_label["text"]=0
    
    status_label.place(x=470,y=380)
    if poker_coin>=30:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gamewin)   

def raise_betting():
    global poker_coin,poker_betting_coin
    all_in_btn.place_forget()
    raise_btn.place_forget()
    call_btn.place_forget()
    die_btn.place_forget()
    
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,250,image=card_image_file[poker_card.index(cp_card[i])])
        
    cp_label.place(x=250,y=320)
       
    if pp_point>cp_point:
        poker_coin+=poker_betting_coin*2
        status_label["text"]="플레이어 승리"
        coin_label["text"]=poker_coin
    elif pp_point<cp_point:
        poker_coin-=poker_betting_coin*2
        status_label["text"]=" 컴퓨터 승리"
        coin_label["text"]=poker_coin
        
    status_label.place(x=470,y=380)
    if poker_coin>=30:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gamewin)
    if poker_coin<=0:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gameover)
                
def call_betting():
    global poker_coin,poker_betting_coin
    all_in_btn.place_forget()
    raise_btn.place_forget()
    call_btn.place_forget()
    die_btn.place_forget()
    
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,250,image=card_image_file[poker_card.index(cp_card[i])])
        
    cp_label.place(x=250,y=320)
       
    if pp_point>cp_point:
        poker_coin+=poker_betting_coin
        status_label["text"]="플레이어 승리"
        coin_label["text"]=poker_coin
    elif pp_point<cp_point:
        poker_coin-=poker_betting_coin
        status_label["text"]="컴퓨터 승리"
        coin_label["text"]=poker_coin
        
    status_label.place(x=470,y=380)
    if poker_coin>=30:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gamewin)
    if poker_coin<=0:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gameover)
              
def die_betting():
    global poker_coin,poker_betting_coin
    all_in_btn.place_forget()
    raise_btn.place_forget()
    call_btn.place_forget()
    die_btn.place_forget() 
    cp_label.place_forget()
    
    for i in range(5):
        poker_back_canvas.create_image(450+120*i,250,image=card_image_file[poker_card.index(cp_card[i])])
        
    cp_label.place(x=250,y=320)
       
    poker_coin-=poker_betting_coin
    status_label["text"]="컴퓨터 승리"
    coin_label["text"]=poker_coin
    status_label.place(x=470,y=380)
    
    if poker_coin>=30:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gamewin)
    if poker_coin<=0:
        status_label.place_forget()
        poker_back_canvas.create_image(720,450,image=gameover)
           
def re_start():
    status_label.place_forget()
    
    all_in_btn.place(x=370,y=380)
    raise_btn.place(x=520,y=380)
    call_btn.place(x=670,y=380)
    die_btn.place(x=820,y=380)
    
    cp_label.place_forget()
    
    delete_card()
    
    setting_card()
    suffle_card()
    
    play_poker(cp_card)
    play_poker(pp_card) 
    
    cp_label["text"]=cp_txt
    pp_label["text"]=pp_txt
    
    pp_label.place(x=250,y=480)
    
def level_delete():
    global poker_coin
    
    poker_back_canvas.pack()
    poker_back_canvas.create_image(720,450,image=poker_level_back)
    poker_exit_btn.place(x=30,y=30)
    poker_back_canvas.create_image(720,450,image=table_image)
    poker_back_canvas.create_image(1240,150,image=casino_plate)
    poker_back_canvas.create_image(1100,150,image=chip_image)
    
    poker_level_exit_btn.place_forget()
    
    easy_poker_start_btn.place_forget()  
    normal_poker_start_btn.place_forget()
    hard_poker_start_btn.place_forget()
    poker_level_canvas.pack_forget()
    
    all_in_btn.place(x=370,y=380)
    raise_btn.place(x=520,y=380)
    call_btn.place(x=670,y=380)
    die_btn.place(x=820,y=380)
    
    re_poker_btn.place(x=1100,y=370)
    
    setting_card()
    suffle_card()
    
    play_poker(cp_card)
    play_poker(pp_card)
    
    coin_label.place(x=1200,y=100)

    cp_label["text"]=cp_txt
    pp_label["text"]=pp_txt
    
    pp_label.place(x=250,y=480)

gameroot=tkinter.Tk()   #기본 root
gameroot.title("게임 모음")
gameroot.geometry("1440x900")
gameroot.resizable(True,True)

poker_level_canvas=tkinter.Canvas(gameroot,width=1440,height=900)
poker_level_canvas.pack()

poker_back_canvas=tkinter.Canvas(gameroot,width=1440,height=900)    #포커 게임의 배경

poker_level_back=tkinter.PhotoImage(file="casino_level_back.png")
poker_level_canvas.create_image(720,450,image=poker_level_back)

poker_title=tkinter.PhotoImage(file="poker_title.png")
poker_level_canvas.create_image(720,300,image=poker_title)

status_label=tkinter.Label(gameroot,text="",font=(ft,80),fg="white",bg="light sea green")
coin_label=tkinter.Label(gameroot,text=poker_coin,font=(ft,80),bg="red4",fg="white")

cp_label=tkinter.Label(gameroot,text='',font=(ft,30),fg="white",bg="light sea green")
pp_label=tkinter.Label(gameroot,text='',font=(ft,30),fg="white",bg="light sea green")

hard=tkinter.PhotoImage(file="hard.png")
normal=tkinter.PhotoImage(file="normal.png")
easy=tkinter.PhotoImage(file="easy.png")

easy_poker_start_btn=tkinter.Button(gameroot,command=start_easy_poker,image=easy)
easy_poker_start_btn.place(x=260,y=600)

normal_poker_start_btn=tkinter.Button(gameroot,command=start_normal_poker,image=normal)
normal_poker_start_btn.place(x=620,y=600)

hard_poker_start_btn=tkinter.Button(gameroot,command=start_hard_poker,image=hard)
hard_poker_start_btn.place(x=980,y=600)

all_in=tkinter.PhotoImage(file="all_in_btn.png")
raize=tkinter.PhotoImage(file="raise_btn.png")
call=tkinter.PhotoImage(file="call_btn.png")
die=tkinter.PhotoImage(file="die_btn.png")

all_in_btn=tkinter.Button(gameroot,image=all_in,command=all_in_betting)
raise_btn=tkinter.Button(gameroot,image=raize,command=raise_betting)
call_btn=tkinter.Button(gameroot,image=call,command=call_betting)
die_btn=tkinter.Button(gameroot,image=die,command=die_betting)

re_play=tkinter.PhotoImage(file="replay.png")

re_poker_btn=tkinter.Button(gameroot,image=re_play,command=re_start,font=(ft,100))

poker_exit_btn=tkinter.Button(gameroot,text="X",fg="black",font=(ft,30),command=exit_poker_game)

poker_level_exit_btn=tkinter.Button(gameroot,text="X",fg="black",font=(ft,30),command=exit_level_poker)
poker_level_exit_btn.place(x=30,y=30)

chip_image=tkinter.PhotoImage(file="poker_chip.png")
table_image=tkinter.PhotoImage(file="poker_table.png")
casino_plate=tkinter.PhotoImage(file="casino_plate.png")

gamewin=tkinter.PhotoImage(file="gamewin.png")
gameover=tkinter.PhotoImage(file="gameover.png")

for n in number:
    for p in pattern:
        card_image_file.append(tkinter.PhotoImage(file=f"{n}{p}.png"))

card_back=tkinter.PhotoImage(file="back.png")

gameroot.mainloop()