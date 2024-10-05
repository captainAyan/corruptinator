import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox


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
        messagebox.showinfo("Success", f"Modified {file_path} with random data.")
    else:
        messagebox.showerror("Error", "File not found!")


def browse_file():
    """Open file dialog to select a file."""
    filename = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    file_entry.delete(0, tk.END)  # Clear the entry
    file_entry.insert(0, filename)  # Insert the selected file path


# Create the main window
root = tk.Tk()
root.title("Corruptinator")

# Create and place the widgets
tk.Label(root, text="Select a file to corrupt:").pack(pady=10)

file_entry = tk.Entry(root, width=50)
file_entry.pack(padx=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
