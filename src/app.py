import asyncio
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError


def download_video():
    global message_label

    # Get video_link_entry from Entry widget
    yt_link = yt_link_entry.get()  
    if yt_link:
        try: 
            if message_label is not None:
                message_label.destroy()
                message_label = None

            # Create a YouTube object
            yt_object = YouTube(yt_link)

            # Get the highest resolution video stream
            stream = yt_object.streams.get_highest_resolution() 

            # Download the video to the current working directory
            stream.download()

            message_label = tk.Label(root, text="Downloading Video...")
            message_label.pack()
        # TODO: Añadir más control de errores
        except RegexMatchError:
            if message_label is not None:
                message_label.destroy()
            message_label = tk.Label(root,text="❌ Invalid YouTube URL, check that it's ok or don't put weird stuff 👺")
        #except AgeRestrictedError:
            #message_label = tk.Label(root,text=AgeRestrictedError.error_string)

# App frame
root = tk.Tk() # create a root widget 
root.title("Youtube Downloader")
root.configure(background="NavajoWhite2")
root.geometry("500x380") # set starting size of window
root.maxsize(1000,580)

message_label = tk.Label(root, text="")
message_label.pack()

# Adding UI elements
title_box = tk.Label(root, text="Insert a Youtube Link", bg="NavajoWhite2", fg="#000")
title_box.pack(pady=20)
title_box.config(font=("Font", 30))


yt_link_frame = tk.Frame(root)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)

download_complete_label = tk.Label(root, text="")
download_complete_label.pack()


# Download Button
download_button = tk.Button(root, text="Download Video", command=download_video, width=15)
download_button.pack(ipady=10, pady=40)
download_button.config(font=("Font", 15))


# ProgressBar
progress_bar = ttk.Progressbar()
progress_bar.pack(ipady=50, pady=50)
progress_bar.step(50)


# Run app
root.mainloop()