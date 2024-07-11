import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
import threading
import io

def on_paste(event):
    # Llamamos a check_youtube_link después de 10 milisegundos
    event.widget.after(10, check_youtube_link)
    
def check_youtube_link():
    global yt  
    yt_link = app.clipboard_get() 
    try: 
        yt = YouTube(yt_link)
        display_resolutions_radio_button()

    except RegexMatchError:
        messagebox.showerror("Error", message="❌ Invalid YouTube Link ❌")
        yt = None
    except AgeRestrictedError:
        messagebox.showwarning("Warning", message="This video is age restricted, please log in to Youtube to download it")

def display_resolutions_radio_button():
    choose_resolution_label.pack(pady=20)
    global selected_stream
    selected_stream = tk.StringVar()
    for stream in yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True):
        radio_button = tk.Radiobutton(
                                    app, 
                                    text=stream.resolution, 
                                    value=stream.resolution,
                                    variable=selected_stream,
                                    command=get_video_stream
                                    )
        radio_button.pack()
    display_download_vide_button()

def display_download_vide_button():
    download_button.pack(ipady=10, pady=20)

def get_video_stream():
    return yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True, res=selected_stream).first()

def update_progress_bar(progress_bar_widget, total_progress, progress_bar_widget_label):
    progress_bar_widget["value"] = total_progress
    progress_bar_widget_label.configure(text=f"{total_progress}%")
    app.update_idletasks()

def download_video_stream(progress_bar_widget, lock, progress_bar_label_widget, shared_data):
    video_stream = get_video_stream()
    video_stream.download()
    filesize = video_stream.filesize
    bytes_downloaded = 0

    buffer = io.BytesIO()
    video_stream.stream_to_buffer(buffer=buffer)

    for chunk in buffer.getvalue():
        bytes_downloaded += len(chunk) # incrementa la cantidad total descargada con el tamaño del chunk actual
        with lock:
            percent = (bytes_downloaded / filesize) * 50
            shared_data["video_progress"] = int(percent)
            total_progress = shared_data['video_progress'] + shared_data['audio_progress']
            # Llamar a update_progress en el hilo principal
            app.after(0, update_progress_bar, progress_bar_widget, total_progress, progress_bar_label_widget)
    


def download_audio_stream(progress, lock, progress_bar_label_widget, shared_data):
    audio_stream = yt.streams.get_audio_only()
    filesize = audio_stream.filesize
    bytes_downloaded = 0

    buffer = io.BytesIO()
    audio_stream.stream_to_buffer(buffer=buffer)

    for chunk in buffer.getvalue():
        bytes_downloaded = chunk
        with lock:
            percent = (bytes_downloaded / filesize) * 50
            shared_data["audio_progress"] = int(percent)
            total_progress = shared_data['video_progress'] + shared_data['audio_progress']
            # Llamar a update_progress en el hilo principal
            app.after(0, update_progress_bar, progress, total_progress, progress_bar_label_widget)
    

    #https://www.youtube.com/shorts/lZ30aycZjFo

def download_video():
    lock = threading.Lock()
    shared_data = {'video_progress': 0, 'audio_progress': 0}

    # Packing labels
    label_frame.pack(pady=30)
    progress_bar.place(x=200, y=250, width=400)
    downloading_text_label.pack(side=tk.LEFT)
    downloading_percent_label.pack(side=tk.LEFT)

    video_thread = threading.Thread(target=download_video_stream, args=(progress_bar, lock, downloading_percent_label, shared_data))
    audio_thread = threading.Thread(target=download_audio_stream, args=(progress_bar, lock, downloading_percent_label, shared_data))
    
    video_thread.start()
    audio_thread.start()


def download_progress_bar_status(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent = (bytes_downloaded / total_bytes) * 100
    progress_bar["value"] = int(percent)
    text_label = f"{progress_bar["value"]}%"
    downloading_percent_label.configure(text=text_label)

    if bytes_remaining == 0:
        messagebox.showinfo("SUCCESSFULLY", message="Download Complete")

    app.update_idletasks()
    

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

yt_link_entry.bind("<<Paste>>", on_paste)

# searching label
choose_resolution_label = tk.Label(app, text="Choose a Resolution: ", fg="#fff")
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