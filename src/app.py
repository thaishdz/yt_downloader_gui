import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError

import threading

def check_youtube_link():
    # Get video_link_entry from Entry widget
    yt_link = yt_link_entry.get()  
    if yt_link:
        try: 
            download_video(yt_link)

        # TODO: Add more error options
        except RegexMatchError:
            messagebox.showerror("Error", message="❌ Invalid YouTube Link, check that it's ok or don't put weird stuff 👺")
        except AgeRestrictedError:
            messagebox.showwarning(message="This video is age restricted, please log in to Youtube to download it")

def download_video(yt_link):

    # Create a YouTube object
    yt_object = YouTube(yt_link)

    # Get the highest resolution video stream
    stream = yt_object.streams.get_highest_resolution() 

    # Packing labels
    label_frame.pack(pady=30)
    progress_bar.place(x=200, y=250, width=400)
    downloading_text_label.pack(side=tk.LEFT)
    downloading_percent_label.pack(side=tk.LEFT)

    # Register Callback handling by pytube and creating progress bar status thread 
    progress_bar_status_thread = threading.Thread(yt_object.register_on_progress_callback(download_progress_bar_status))

    # Create download video thread 
    download_video_thread = threading.Thread(target=stream.download) 

    download_video_thread.start()
    progress_bar_status_thread.start()


def download_progress_bar_status(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent = (bytes_downloaded / total_bytes) * 100
    progress_bar["value"] = int(percent)
    text_label = f"{int(percent)}%"
    downloading_percent_label.configure(text=text_label)

    if bytes_remaining == 0:
        messagebox.showinfo("SUCCESSFULLY", message="Download Complete 🙌")

    app.update_idletasks()
    

# App frame
app = tk.Tk() # create a root widget 
app.title("Youtube Downloader")
app.configure(background="#912828")
app.geometry("800x350") # set starting size of window
app.resizable(False,False) # height, width

# Adding UI elements
title_box = tk.Label(app, text="Insert a Youtube Link", bg="#eaeaea", fg="#000")
title_box.pack(pady=30)
title_box.config(font=("Font", 30))

# Youtube link form input
yt_link_frame = tk.Frame(app)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)


# Download Button
download_button = tk.Button(app, text="Download Video", command=check_youtube_link, width=15)
download_button.pack(ipady=10, pady=20)
download_button.config(font=("Font", 15))


# ProgressBar
progress_bar = ttk.Progressbar()
label_frame = tk.Frame(app)
downloading_text_label = tk.Label(label_frame, text="Downloading...")
downloading_percent_label = tk.Label(label_frame,text="0%")
# Run app
app.mainloop()