import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser


def modify_image_with_random_data(file_path):
    """Replace file data with random bytes."""
    file_size = os.path.getsize(file_path)
    random_data = bytes(random.getrandbits(8) for _ in range(file_size))

    with open(file_path, 'wb') as f:
        f.write(random_data)


def submit():
    """Handle the submit button click."""
    file_path = file_entry.get()
    if os.path.isfile(file_path):
        modify_image_with_random_data(file_path)
        messagebox.showinfo("Success", f"Corrupted {file_path} with random data.")
    else:
        messagebox.showerror("Error", "File not found!")


def browse_file():
    """Open file dialog to select a file."""
    filename = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    file_entry.delete(0, tk.END)  # Clear the entry
    file_entry.insert(0, filename)  # Insert the selected file path


# mongo smoothie theme
bg_color = "#f8edeb"
browse_btn_color= "#fec89a"
submit_btn_color= "#fa9595"
text_color = "#fa9595"

# dark theme
# bg_color = "#303952"
# browse_btn_color= "#596275"
# submit_btn_color= "#596275"
# text_color = "#f0f0f0"

# Create the main window
root = tk.Tk()
root.title("Corruptinator")
root.geometry("400x320")  # Set a fixed size for the window
root.configure(bg=bg_color)  # Set background color
root.resizable(False, False)

# Create and place the header
header_label = tk.Label(root, text="Corruptinator", bg=bg_color, font=("Arial", 24, "bold"), anchor='w', fg=text_color)
header_label.pack(padx=20, pady=(10, 0), anchor='n')

# Create and place the widgets within a frame
frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=20, pady=0)

tk.Label(frame, text="Select a file to corrupt:", bg=bg_color, font=("Arial", 12), fg=text_color).pack(pady=10)

file_entry = tk.Entry(frame, width=400, font=("Arial", 12), bd=2, relief="groove")
file_entry.pack(pady=10)


browse_button = tk.Button(frame, text="Browse", command=browse_file, bg=browse_btn_color, fg="white", font=("Arial Black", 12), bd=0, width=400)
browse_button.pack(pady=5)

submit_button = tk.Button(frame, text="Corrupt", command=submit, bg=submit_btn_color, fg="white", font=("Arial Black", 12), bd=0, width=400)
submit_button.pack(pady=5)

github_link = "GitHub @captainayan"
github_label = tk.Label(root, text=github_link, bg=bg_color, font=("Arial", 10), fg="#007BFF")
github_label.pack(pady=2)
github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/captainayan"))

# Adjust button height
for button in (browse_button, submit_button):
    button.config(height=2)

# Run the application
root.mainloop()
