from tkinter import *
from os.path import dirname, join
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t):
    mins = math.floor(t // 60)
    secs = t % 60
    t_show = f"{mins:02d}:{secs:02d}"
    canvas.itemconfig(timer_label, text = t_show)
    if t > 0: 
        window.after(100, countdown, t-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.geometry("300x400")
window.title("Pomodoro")
window.config(padx=10, pady=50, bg=YELLOW)


current_dir = dirname(__file__)
file_path = join(current_dir, "tomato.png")

tick_path = join(current_dir, "tick.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

tomato_img = PhotoImage(file=file_path)
tick_img = PhotoImage(file=tick_path)
# tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#calls action() when pressed
button = Button(text="Start", command=starttimer, highlightthickness=0)
button.grid(row=2, column=0)

tick_label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 20))
tick_label.grid(row=3, column=1)
# canvas.create_image(10, 70, image=tick_img)

button = Button(text="Reset", command=reset, highlightthickness=0)
button.grid(row=2, column=2)

# canvas.pack()
window.mainloop()