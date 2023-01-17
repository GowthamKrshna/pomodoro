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
reps = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_head.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_head.config(text='Break', fg= PINK)
    else:
        count_down(work_sec)
        label_head.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += '✓'
        label_2.config(text=mark)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_head.config(text="Timer")
    label_2.config(text="")
    global reps
    reps = 0
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=20, pady=20, bg=YELLOW)
label_head = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
label_head.grid(column=1, row=0)
canvas = tkinter.Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
pom_image = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(105, 115, image= pom_image)

timer_text = canvas.create_text(103, 130, fill='white', text='00.00', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row= 1)

button_1 = tkinter.Button(text='Start', command=start_timer)
button_1.grid(column=0, row=2)
button_2 = tkinter.Button(text='Reset', command=reset_timer)
button_2.grid(column=2, row=2)
label_2 = tkinter.Label(fg=GREEN, bg=YELLOW)
label_2.grid(column=1, row=3)
window.mainloop()