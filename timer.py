import time
import tkinter as tk

window=tk.Tk()

def countdown(t):
        if t > 0:
            window.after(1, countdown, t-1)
            mins = t // 60
            secs = t % 60
            timer = "{:02d}:{02d}, format(mins, secs)"
            # t-= 1
            time.sleep(0.1)
            timer_label = tk.Label(text=f"{mins}:{secs}, formatted as:  {timer}")
            timer_label.pack()
            print(f"{mins}:{secs}, formatted as:  timer")

countdown(30)
window.mainloop()