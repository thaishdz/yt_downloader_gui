import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from pytube import YouTube, Stream
from pytube.exceptions import RegexMatchError, AgeRestrictedError
import threading

def on_paste(event):
    # Llamamos a check_youtube_link después de 10 milisegundos
    event.widget.after(10, check_youtube_link)
    
def check_youtube_link():
    yt_link = app.clipboard_get() 
    if yt_link:
        try:   
            global yt           
            yt = YouTube(yt_link)
            choose_resolution_label.pack(pady=20)
            display_resolutions_radio_button(yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True))

        except RegexMatchError:
            messagebox.showerror("Error", message="❌ Invalid YouTube Link, check that it's ok or don't put weird stuff 👺")
        except AgeRestrictedError:
            messagebox.showwarning(message="This video is age restricted, please log in to Youtube to download it")

def display_resolutions_radio_button(streams):
    global selected_stream
    selected_stream = tk.StringVar()
    for stream in streams:
        radio_button = tk.Radiobutton(
                                    app, 
                                    text=stream.resolution, 
                                    value=stream.resolution,
                                    variable=selected_stream,
                                    command=get_selected_stream
                                    )
        radio_button.pack()
    display_download_vide_button()

def get_selected_stream() :
    return yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True, res=selected_stream).first()

def display_download_vide_button():
    download_button.pack(ipady=10, pady=20)
    
def download_video(): 

    stream = get_selected_stream()

    # Packing labels
    label_frame.pack(pady=30)
    progress_bar.place(x=200, y=250, width=400)
    downloading_text_label.pack(side=tk.LEFT)
    downloading_percent_label.pack(side=tk.LEFT)


    # Register Callback handling by pytube and creating progress bar status thread 
    progress_bar_status_thread = threading.Thread(yt.register_on_progress_callback(download_progress_bar_status))

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
app.geometry("800x450") # set starting size of window
app.resizable(False,False) # height, width

# Adding UI elements
title_box = tk.Label(app, text="Insert a Youtube Link", fg="#fff")
title_box.pack(pady=30)
title_box.config(font=("Font", 30))

# Youtube link form input
yt_link_frame = tk.Frame(app)
yt_link_frame.pack()

yt_link_entry = tk.Entry(yt_link_frame, width=50)
yt_link_entry.pack(ipady=5)

yt_link_entry.bind("<<Paste>>", on_paste)

# searching label
choose_resolution_label = tk.Label(app, text="Choose a video resolution: ", fg="#fff")
choose_resolution_label.config(font=("Font", 15))

# Download Button
download_button = tk.Button(app, text="Download Video", command=download_video, width=15)
download_button.config(font=("Font", 15))


# ProgressBar
progress_bar = ttk.Progressbar()
label_frame = tk.Frame(app)
downloading_text_label = tk.Label(label_frame, text="Downloading...")
downloading_percent_label = tk.Label(label_frame,text="0%")


# Run app
app.mainloop()