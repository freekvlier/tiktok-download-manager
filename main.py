import tkinter as tk
from tkinter import filedialog
import os
from snaptik import SnapTikReversed  # Make sure to replace 'your_script' with the actual name of your script file
from firebase_manager import FirebaseManager

def download_video():
    url = url_entry.get()
    destination = dest_entry.get()
    firebase_manager = FirebaseManager()

    if not url:
        status_label.config(text="Please enter a TikTok URL")
        return

    if firebase_manager.is_url_downloaded(url):
        status_label.config(text="This video has already been downloaded.")
    else:
        downloader = SnapTikReversed()
        result = downloader.get_video(url, destination)
        if result:  # Check if download was successful
            firebase_manager.add_downloaded_url(url)
            status_label.config(text="Download successful: " + result)
        else:
            status_label.config(text="Download failed.")

def set_default_destination():
    default_path = os.path.dirname(os.path.realpath(__file__))
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, default_path)

root = tk.Tk()
root.title("TikTok Downloader")

# URL Entry
tk.Label(root, text="TikTok URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Destination Entry
tk.Label(root, text="Destination:").pack()
dest_entry = tk.Entry(root, width=50)
dest_entry.pack()
set_default_destination()  # Set default destination

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Status Label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
