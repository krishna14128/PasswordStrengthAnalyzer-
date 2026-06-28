"""
main.py

Main GUI for the Password Strength Analyzer.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from analyzer import calculate_password_strength


# -----------------------------
# Check Password
# -----------------------------
def check_strength():
    """Analyze the entered password."""

    password = password_entry.get()

    # Handle empty input
    if password == "":
        messagebox.showwarning(
            "Empty Password",
            "Please enter a password."
        )
        return

    # Get analysis results
    score, level, suggestions = calculate_password_strength(password)

    # Display score
    score_label.config(text=f"Strength Score: {score}/100")

    # Display level
    level_label.config(text=f"Strength Level: {level}")

    # Update progress bar
    progress["value"] = score

    # Change progress bar color
    if score <= 40:
        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="red"
        )

    elif score <= 60:
        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="gold"
        )

    else:
        style.configure(
            "Custom.Horizontal.TProgressbar",
            background="green"
        )

    # Display suggestions
    suggestion_text.config(state="normal")
    suggestion_text.delete(1.0, tk.END)

    for item in suggestions:
        suggestion_text.insert(tk.END, "• " + item + "\n")

    suggestion_text.config(state="disabled")


# -----------------------------
# Reset Application
# -----------------------------
def reset_fields():
    """Clear all fields."""

    password_entry.delete(0, tk.END)

    score_label.config(text="Strength Score: -")

    level_label.config(text="Strength Level: -")

    progress["value"] = 0

    suggestion_text.config(state="normal")
    suggestion_text.delete(1.0, tk.END)
    suggestion_text.config(state="disabled")


# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle_password():
    """Show or hide password."""

    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()

window.title("Password Strength Analyzer")

window.geometry("600x550")

window.configure(bg="white")

window.resizable(False, False)

# -----------------------------
# Progress Bar Style
# -----------------------------
style = ttk.Style()

style.theme_use("default")

style.configure(
    "Custom.Horizontal.TProgressbar",
    thickness=20,
    background="red"
)

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial", 18, "bold"),
    bg="white"
)

title.pack(pady=15)

# -----------------------------
# Password Label
# -----------------------------
password_label = tk.Label(
    window,
    text="Enter Password",
    bg="white",
    font=("Arial", 12)
)

password_label.pack()

# -----------------------------
# Password Entry
# -----------------------------
password_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12),
    show="*"
)

password_entry.pack(pady=10)

# -----------------------------
# Show Password Checkbox
# -----------------------------
show_password = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_password,
    command=toggle_password,
    bg="white"
)

show_checkbox.pack()

# -----------------------------
# Buttons Frame
# -----------------------------
button_frame = tk.Frame(
    window,
    bg="white"
)

button_frame.pack(pady=15)

# Check Button
check_button = tk.Button(
    button_frame,
    text="Check Strength",
    bg="dodgerblue",
    fg="white",
    width=15,
    command=check_strength
)

check_button.grid(row=0, column=0, padx=5)

# Reset Button
reset_button = tk.Button(
    button_frame,
    text="Reset",
    bg="dodgerblue",
    fg="white",
    width=10,
    command=reset_fields
)

reset_button.grid(row=0, column=1, padx=5)

# Exit Button
exit_button = tk.Button(
    button_frame,
    text="Exit",
    bg="dodgerblue",
    fg="white",
    width=10,
    command=window.destroy
)

exit_button.grid(row=0, column=2, padx=5)

# -----------------------------
# Score Label
# -----------------------------
score_label = tk.Label(
    window,
    text="Strength Score: -",
    font=("Arial", 12),
    bg="white"
)

score_label.pack(pady=10)

# -----------------------------
# Level Label
# -----------------------------
level_label = tk.Label(
    window,
    text="Strength Level: -",
    font=("Arial", 12),
    bg="white"
)

level_label.pack()

# -----------------------------
# Progress Bar
# -----------------------------
progress = ttk.Progressbar(
    window,
    length=350,
    maximum=100,
    style="Custom.Horizontal.TProgressbar"
)

progress.pack(pady=20)

# -----------------------------
# Suggestions Label
# -----------------------------
suggestion_label = tk.Label(
    window,
    text="Suggestions",
    font=("Arial", 12, "bold"),
    bg="white"
)

suggestion_label.pack()

# -----------------------------
# Suggestions Text Area
# -----------------------------
suggestion_text = tk.Text(
    window,
    width=60,
    height=10,
    font=("Arial", 10)
)

suggestion_text.pack(pady=10)

suggestion_text.config(state="disabled")

# -----------------------------
# Run Application
# -----------------------------
window.mainloop()