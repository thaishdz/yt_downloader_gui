import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
import threading
    

def display_progress_bar_status():
    
    text_label_frame.pack(pady=30)
    progress_bar_widget.place(x=200, y=250, width=400)
    downloading_text_label.pack(side=tk.LEFT)
    downloading_percent_label.pack(side=tk.LEFT)

    app.update_idletasks()
    

def update_progress_bar_status(stream, chunk, bytes_remaining): 
    
    if bytes_remaining == 0:
        messagebox.showinfo("SUCCESSFULLY", message="Download Complete")

    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent = (bytes_downloaded / total_bytes) * 100
    progress_bar_widget["value"] = int(percent)
    text_label = f"{progress_bar_widget["value"]}%"
    downloading_percent_label.configure(text=text_label)

    app.update_idletasks() 


def download_video():
    try:
        display_progress_bar_status()
        yt = YouTube(yt_link_entry.get())
        stream = yt.streams.get_highest_resolution()

        # Register Callback handling by pytube and creating progress bar status thread 
        progress_bar_status_thread = threading.Thread(yt.register_on_progress_callback(update_progress_bar_status))
        # Create download video thread 
        download_video_thread = threading.Thread(target=stream.download) 

        download_video_thread.start()
        progress_bar_status_thread.start()


    except RegexMatchError:
        messagebox.showerror("Error", message="❌ Invalid YouTube Link ❌")
    except AgeRestrictedError:
        messagebox.showwarning("Warning", message="This video is age restricted, please log in to Youtube to download it")
  

# App frame
app = tk.Tk() # create a root widget 
app.title("Youtube Downloader")
app.configure(background="#912828")
app.geometry("800x450") # set starting size of window
app.resizable(False,False) # height, width

# Adding UI elements
title_box = tk.Label(app, text="Paste a YouTube Link", fg="#fff")
title_box.pack(pady=30)
title_box.config(font=("Font", 30))

# Youtube link form input
yt_link_frame = tk.Frame(app)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)

# Download Button
download_button = tk.Button(app, text="Download Video", command=download_video, width=15)
download_button.config(font=("Font", 15))
download_button.pack(ipady=10, pady=20)


# ProgressBar
progress_bar_widget = ttk.Progressbar()
text_label_frame = tk.Frame(app)
downloading_text_label = tk.Label(text_label_frame, text="Downloading...")
downloading_percent_label = tk.Label(text_label_frame,text="0%")


# Run app
app.mainloop()