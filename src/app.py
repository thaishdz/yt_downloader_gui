from tkinter import *
from pytube import YouTube
from pytube.exceptions import RegexMatchError

root = Tk() # create a root widget 


root.title("Youtube Downloader")
root.configure(background="NavajoWhite2")
root.geometry("500x380") # set starting size of window
root.maxsize(1000,580)


# TODO: Meter asincronia
def download_video():
    message_label = Label(root,text='')

    # Get video_link_entry from Entry widget
    video_url = video_link_entry.get()  
    print("YT URL:", video_url)

    try:

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution() 

        # Download the video to the current working directory
        stream.download()

        message_label.config(text="Downloading Video ...")
        message_label.pack()
        
    except RegexMatchError:
        message_label.config(text="Invalid YouTube URL 🥶, check that it's ok or don't put weird stuff 👺")
        message_label.pack()
        
    




title_box = Label(root, text="Put your link below", bg="NavajoWhite2", fg="#000")
title_box.pack(pady=20)
title_box.config(font=("Font", 30))


video_link_frame = Frame(root)
video_link_frame.pack()

video_link_entry = Entry(video_link_frame, width=50)
video_link_entry.pack(ipady=5)


download_button = Button(root, text="Download Video", command=download_video, width=15)
download_button.pack(ipady=10, pady=40)
download_button.config(font=("Font", 15))
root.mainloop()