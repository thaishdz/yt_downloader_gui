import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError


def download_video():
    global message_label

    # Get video_link_entry from Entry widget
    yt_link = yt_link_entry.get()  
    if yt_link:
        try: 
            # Create a YouTube object
            yt_object = YouTube(yt_link)

            # Get the highest resolution video stream
            stream = yt_object.streams.get_highest_resolution() 

            # Download the video to the current working directory
            stream.download()

        # TODO: Añadir más control de errores
        except RegexMatchError:
            messagebox.showerror(message="❌ Invalid YouTube Link, check that it's ok or don't put weird stuff 👺")
        except AgeRestrictedError:
            messagebox.showwarning(message="This video is age restricted, please log in to Youtube to download it")


# App frame
app = tk.Tk() # create a root widget 
app.title("Youtube Downloader")
app.configure(background="NavajoWhite2")
app.geometry("500x380") # set starting size of window
app.maxsize(1000,580)

# Adding UI elements
title_box = tk.Label(app, text="Insert a Youtube Link", bg="NavajoWhite2", fg="#000")
title_box.pack(pady=20)
title_box.config(font=("Font", 30))


yt_link_frame = tk.Frame(app)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)

download_complete_label = tk.Label(app, text="")
download_complete_label.pack()


# Download Button
download_button = tk.Button(app, text="Download Video", command=download_video, width=15)
download_button.pack(ipady=10, pady=40)
download_button.config(font=("Font", 15))


# ProgressBar
progress_bar = ttk.Progressbar(app, length=400)
progress_bar.pack(pady=50)


# Run app
app.mainloop()