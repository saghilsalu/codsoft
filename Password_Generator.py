import tkinter as tk
import random
def generate_password():
    try:
        length = int(textbox.get())
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid number for length.")
        return
    complexity = complexity_var.get()
    if complexity == "High":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    elif complexity == "Medium":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password = ''.join(random.choice(chars) for _ in range(length))
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, password)
root = tk.Tk()
root.title("Password Generator")
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
root.configure(bg='#1E1E1E')
container_frame = tk.Frame(root, bg='#2E2E2E', borderwidth=2, relief="solid", padx=15, pady=15)
container_frame.place(relx=0.5, rely=0.5, anchor="center", width=window_width - 40, height=window_height - 40)
title_label = tk.Label(container_frame, text="Password Generator", font=("Helvetica", 14, 'bold'), fg='#FFFFFF',bg='#2E2E2E')
title_label.pack(pady=10)
frame_length = tk.Frame(container_frame, bg='#2E2E2E')
frame_length.pack(pady=5, fill='x')
label_length = tk.Label(frame_length, text="Length", font=("Arial", 12, 'bold'), bg='#2E2E2E', fg='#FFFFFF')
label_length.pack(side=tk.LEFT, padx=5)
textbox = tk.Entry(frame_length, font=("Arial", 12), width=8, bg='#4A4A4A', fg='#FFFFFF', borderwidth=1, relief="solid")
textbox.pack(side=tk.LEFT, padx=5)
frame_complexity = tk.Frame(container_frame, bg='#2E2E2E')
frame_complexity.pack(pady=5, fill='x')
label_complexity = tk.Label(frame_complexity, text="Complexity", font=("Arial", 12, 'bold'), bg='#2E2E2E', fg='#FFFFFF')
label_complexity.pack(side=tk.LEFT, padx=5)
complexity_var = tk.StringVar(value="Low")
radiobutton_high = tk.Radiobutton(frame_complexity, text="High", variable=complexity_var, value="High",font=("Arial", 12), bg='#2E2E2E', fg='#FFFFFF', selectcolor='#5A9BD4', indicatoron=0,relief="flat")
radiobutton_high.pack(side=tk.LEFT, padx=5)
radiobutton_medium = tk.Radiobutton(frame_complexity, text="Medium", variable=complexity_var, value="Medium",font=("Arial", 12), bg='#2E2E2E', fg='#FFFFFF', selectcolor='#5A9BD4',indicatoron=0, relief="flat")
radiobutton_medium.pack(side=tk.LEFT, padx=5)
radiobutton_low = tk.Radiobutton(frame_complexity, text="Low", variable=complexity_var, value="Low", font=("Arial", 12),bg='#2E2E2E', fg='#FFFFFF', selectcolor='#5A9BD4', indicatoron=0, relief="flat")
radiobutton_low.pack(side=tk.LEFT, padx=5)
button = tk.Button(container_frame, text="Generate", font=("Arial", 12, 'bold'), bg='#5A9BD4', fg='#FFFFFF',command=generate_password, borderwidth=0, relief="flat")
button.pack(pady=10)
result_text = tk.Text(container_frame, font=("Arial", 12), width=25, height=4, bg='#4A4A4A', fg='#FFFFFF',borderwidth=1, relief="solid")
result_text.pack(pady=10)
root.mainloop()
