#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random
from tkinter import simpledialog, messagebox



# --- Configuration ---

BIRTHDATE = datetime(1999, 7, 2)
DEATH_AGE = 66
DEATH_DATE = BIRTHDATE.replace(year=BIRTHDATE.year + DEATH_AGE)

QUOTES = [
    "Make today count!",
    "Live with purpose.",
    "Time is precious.",
    "Do something meaningful.",
    "You write your legacy."
]

# --- GUI Setup ---
root = tk.Tk()
root.title("Death Countdown")
root.geometry("240x120")
root.overrideredirect(True)  # Remove default window border
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", 0.95)
root.configure(bg="#1e1e1e")




def on_enter(event):
    root.wm_attributes("-alpha", 1.0)

def on_leave(event):
    root.wm_attributes("-alpha", 0.85)

root.bind("<Enter>", on_enter)
root.bind("<Leave>", on_leave)

# --- Styles ---
style = ttk.Style()
style.configure("Title.TLabel", font=("Segoe UI", 10, "bold"), foreground="white", background="#1e1e1e")
style.configure("Countdown.TLabel", font=("Segoe UI", 20), foreground="#00d1ff", background="#1e1e1e")
style.configure("Quote.TLabel", font=("Segoe UI", 9), foreground="#aaaaaa", background="#1e1e1e")

# --- Draggable Title Bar ---
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    dx = root.winfo_pointerx() - root.x
    dy = root.winfo_pointery() - root.y
    root.geometry(f"+{dx}+{dy}")

title_bar = tk.Frame(root, bg="#2a2a2a", height=30)
title_bar.pack(fill="x")
title_label = ttk.Label(title_bar, text="Death Countdown", style="Title.TLabel")
title_label.pack(side="left", padx=10)
close_button = tk.Label(title_bar, text="✕", bg="#2a2a2a", fg="gray", font=("Segoe UI", 10))
close_button.pack(side="right", padx=8)
close_button.bind("<Button-1>", lambda e: root.destroy())
settings_button = tk.Label(title_bar, text="⚙", bg="#2a2a2a", fg="gray", font=("Segoe UI", 10))
settings_button.pack(side="right", padx=8)
settings_button.bind("<Button-1>", lambda e: open_settings())
title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<B1-Motion>", do_move)

# --- Widgets ---
countdown_label = ttk.Label(root, text="", style="Countdown.TLabel")
countdown_label.pack(pady=10)

quote_label = ttk.Label(root, text=random.choice(QUOTES), style="Quote.TLabel")
quote_label.pack()

# --- Context Menu (Right-click Exit) ---
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Exit", command=root.destroy)

def show_context_menu(event):
    try:
        context_menu.tk_popup((event.x_root, event.y_root))
    finally:
        context_menu.grab_release()

root.bind("<Button-3>", show_context_menu)

# --- Timer Logic ---
def update_timer():
    now = datetime.now()
    remaining = DEATH_DATE - now

    if remaining.total_seconds() <= 0:
        countdown_label.config(text="⏳ Time's up.")
    else:
        years = remaining.days // 365
        days = remaining.days % 365
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_label.config(
            text=f"{years}y {days}d  {hours:02d}:{minutes:02d}:{seconds:02d}"
        )

    root.after(1000, update_timer)

update_timer()

# Set window icon (PNG only)
icon_path = "death_icon.png"
if os.path.exists(icon_path):
    img = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, img)

# --- Settings Dialog ---
# --- Functions ---
def open_settings():
    # Ask for birthdate

    global BIRTHDATE, DEATH_AGE, DEATH_DATE
    date_str = simpledialog.askstring(
        "Settings",
        "Enter your birthdate (YYYY-MM-DD):",
        initialvalue=BIRTHDATE.strftime("%Y-%m-%d")
    )
    if not date_str:
        return

    try:
        new_birthdate = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
        return

    # Ask for death age
    death_age_str = simpledialog.askstring(
        "Settings",
        "Enter expected death age:",
        initialvalue=str(DEATH_AGE)
    )
    try:
        new_death_age = int(death_age_str)
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter a valid number for death age.")
        return

    BIRTHDATE = new_birthdate
    DEATH_AGE = new_death_age
    DEATH_DATE = BIRTHDATE.replace(year=BIRTHDATE.year + DEATH_AGE)
    quote_label.config(text=random.choice(QUOTES))

root.mainloop()