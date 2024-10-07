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
    total_files = listbox.size()
    if total_files != 0:
        for index in range(total_files):
            file_path = listbox.get(index)  # Get the file path from the Listbox

            if os.path.isfile(file_path):
                modify_image_with_random_data(file_path)  # Call your function to modify the image
            else:
                messagebox.showerror("Error", f"File not found: {file_path}")
        messagebox.showinfo("Success", "Corrupted files with random data.")
    else:
        messagebox.showerror("Error", "No files selected!")


def browse_file():
    """Open file dialog to select a file."""
    filenames = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])

    listbox.delete(0, tk.END)

    if filenames:
        for filename in filenames:
            listbox.insert(tk.END, filename)  # Insert each selected file into the Listbox

        message_label.config(text=f"{listbox.size()} {'file' if listbox.size()==1 else 'files'} selected")
    else:
        message_label.config(text="Select a file to corrupt:")



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
root.geometry("400x360")  # Set a fixed size for the window
root.configure(bg=bg_color)  # Set background color
root.resizable(False, False)

# Create and place the header
header_label = tk.Label(root, text="Corruptinator", bg=bg_color, font=("Arial", 24, "bold"), anchor='w', fg=text_color)
header_label.pack(padx=20, pady=(10, 0), anchor='n')

# Create and place the widgets within a frame
frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=20, pady=0)

message_label = tk.Label(frame, text="Select a file to corrupt:", bg=bg_color, font=("Arial Black", 10), fg=text_color)
message_label.pack(pady=10)

listbox = tk.Listbox(frame, width=400, height=5)  # You can adjust the width and height as needed
listbox.pack(pady=2)

browse_button = tk.Button(frame, text="Browse", command=browse_file, bg=browse_btn_color, fg="white", font=("Arial Black", 12), bd=0, width=400)
browse_button.pack(pady=2)

submit_button = tk.Button(frame, text="Corrupt", command=submit, bg=submit_btn_color, fg="white", font=("Arial Black", 12), bd=0, width=400)
submit_button.pack(pady=2)

github_link = "GitHub @captainayan"
github_label = tk.Label(root, text=github_link, bg=bg_color, font=("Arial", 10), fg="#007BFF")
github_label.pack(pady=2)
github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/captainayan"))

# Adjust button height
for button in (browse_button, submit_button):
    button.config(height=2)

# Run the application
root.mainloop()
