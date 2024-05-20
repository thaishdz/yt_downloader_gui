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
            # Create a YouTube object
            yt_object = YouTube(yt_link)
            download_video(yt_object)

        # TODO: Añadir más control de errores
        except RegexMatchError:
            messagebox.showerror(message="❌ Invalid YouTube Link, check that it's ok or don't put weird stuff 👺")
        except AgeRestrictedError:
            messagebox.showwarning(message="This video is age restricted, please log in to Youtube to download it")


def download_video(yt_object):
    # Get the highest resolution video stream
    stream = yt_object.streams.get_highest_resolution() 

    # Create a thread to download the video
    download_thread = threading.Thread(target=stream.download) 

    # Start the download thread 
    download_thread.start() 

    # Blocks the thread until it ends
    download_thread.join()

    messagebox.showinfo(message="Video Downloaded 🙌")


# App frame
app = tk.Tk() # create a root widget 
app.title("Youtube Downloader")
app.configure(background="#912828")
app.geometry("800x300") # set starting size of window
app.resizable(False,False) # height, width

# Adding UI elements
title_box = tk.Label(app, text="Insert a Youtube Link", bg="#eaeaea", fg="#000")
title_box.pack(pady=20)
title_box.config(font=("Font", 30))


yt_link_frame = tk.Frame(app)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)


# Download Button
download_button = tk.Button(app, text="Download Video", command=check_youtube_link, width=15)
download_button.pack(ipady=10, pady=40)
download_button.config(font=("Font", 15))


# ProgressBar
progress_bar = ttk.Progressbar(app, length=400)
progress_bar.pack(pady=50)

# Run app
app.mainloop()