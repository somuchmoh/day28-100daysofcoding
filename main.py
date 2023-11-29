import tkinter
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
TICK = "✔"
REPS = 0
TICKER = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TICKER)
    timer.config(text="TIMER")
    tick.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    if REPS == 8:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="BREAK", fg=RED)
    elif REPS % 2 == 1:
        count_down(WORK_MIN*60)
        timer.config(text="WORK", fg=GREEN)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TICKER
        TICKER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

timer = tkinter.Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "normal"), pady=10)
timer.grid(row=1, column=2)

start_button = tkinter.Button(text="Start", borderwidth=0, fg=RED, highlightthickness=0, font=(FONT_NAME, 17, "bold"),
                              command=start_timer)
start_button.grid(row=3, column=1)

reset_button = tkinter.Button(text="Reset", borderwidth=0, fg=RED, highlightthickness=0, font=(FONT_NAME, 17, "bold"),
                              command=reset_timer)
reset_button.grid(row=3, column=3)

tick = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"), pady=10)
tick.grid(row=4, column=2)

window.mainloop()
