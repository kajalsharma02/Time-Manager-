import math
from tkinter import *
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = ""

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)
# window.geometry("500x300")

window.resizable(False,False)

canvas = Canvas(width=200, height=224,background=YELLOW)
photo = PhotoImage(file="C:\\Users\\hp\\Documents\\Python Dev Udemy\\Pomodoro App\\tomato.png")
canvas.create_image(103,112,image=photo)
timer_text = canvas.create_text(103,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=2, row=2)


# ---------------------------- TIMER RESET ------------------------------- # 

def restart():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00") 
    name['text'] = "Timer"
    global reps
    reps=0
    global mark
    mark =""
    check['text'] = mark
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN * 60
    short_brak_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        name['text'] = "Long Break Time"
        count_down(long_break_sec)
    
    elif reps % 2 == 0:
        name['text'] = "Short Break Time"
        count_down(short_brak_sec)

    else:
        name['text'] = "Work Time"
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        global mark
        mark+="✔"

        global reps
        if reps%2==0:
            check['text'] = mark
        
        # playsound("C:\\Users\\hp\\Documents\\Python Dev\\Pomodoro App\\notification.mp3")


# ---------------------------- UI SETUP ------------------------------- #

name = Label(text="Timer",font=(FONT_NAME,20,"bold"),fg=GREEN, bg=YELLOW, width=20)
name.grid(column=2, row=1)

start = Button(text="Start",command=start_timer, font=(FONT_NAME,10,"bold"), fg=RED, bg=GREEN)
start.grid(column=1, row=3)

check = Label(text=mark, font=(FONT_NAME,25,"bold"), fg=GREEN, bg=YELLOW)
check.grid(column=2, row=4)

restart = Button(text="Restart", command=restart, font=(FONT_NAME,10,"bold"), fg=RED, bg=GREEN)
restart.grid(column=3, row=3)

window.mainloop()