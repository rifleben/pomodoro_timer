from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    if timer:
        window.after_cancel(timer)
        timer_label.config(text="Timer")
        canvas.itemconfig(timer_text, text ="00:00")
        check_marks.config(text="")
        global reps
        reps = 0
        start_button["state"] = NORMAL
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    start_button["state"] = DISABLED
    global reps
    reps += 1
    work_sec = 5
    short_br = SHORT_BREAK_MIN * 60
    long_br = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_br)
        timer_label.config(text="Long Break", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=RED)

    elif reps % 2 == 0:
        countdown(short_br)
        timer_label.config(text="Short Break",bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=PINK)

    else:
        countdown(work_sec)
        timer_label.config(text="Heads Down",bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)

# ---------------------------- COUNTDOWN ------------------------------- #
def countdown(count):
    minutes = count // 60
    seconds = count % 60
    if seconds <= 9:
        seconds = f"0{seconds}"
    if minutes <= 9:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        sessions = reps // 2
        for _ in range(sessions):
            marks += "✅"

        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, )

# canvas
canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer")
timer_label.grid(column=1, row=0)
timer_label.config(bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)

# buttons

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0, )
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2, )

check_marks = Label(foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
