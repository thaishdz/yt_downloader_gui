![clideo_editor_3b3d8be796cb4196ad87cbec8cfdbaab](https://github.com/user-attachments/assets/d23c9e3b-3e4f-4931-8dd0-5aed7c380251)# YT Downloader with Pytube & Tkinter
__Status : Blocked__ ⛔

## Why it was blocked?
The main reason is because *Pytube* is an obsolete library (not updates since 2021)
Every time YouTube updates its API, things break (logically). 
One day it works fine, the next it doesn't

## What were the objectives with __yt_downloader_gui__?

- Learning about the __integration of libraries__ (Pytube & Tkinter)
- Learning how __library works__ (Pytube)
- Learning about __GUIs__
- Learning how __Asynchrony__ works in Python
- Learning about __threading__ module
- Learning __good practices__ (PEP8 - Style Guide for Python Code)

## Which has been the biggest challenge? 
Boxing against Pytube.







[Context]

I wanted the user could a choose a video resolution,
the thing is, the Progressive streams are video-audio joined but never have 
the highest resolution (720p instead 1080p), 
so I had to work with DASH (separate video and audio).

Downloading the video and audio per separate, 
is no problem because then they can be merged with a module called ffmpeg.

[State of my app on that point]

I had 2 threads : 
1. To download the stream itself
2. To update the progress bar as the stream download progresses

That worked well 👍

[THE PROBLEM]

![image](https://github.com/user-attachments/assets/845cd57a-3366-45f5-bfa5-6d635aeceb97)

Pytube is not «thread-safe»,
because of this, it would not be able to make a third thread 
which unloads a second stream in parallel to the other 2.

## What have you learned?

- How to design and set up an GUI (Tkinter)
- How streams works
- Difference between Progressive vs DASH (Dynamic Adaptive Streaming over HTTP)
- Threading and Asynchronous process (well ... something ... around 1%, I hate it)
- Events
- Buffering
- Lambdas function
- How the progress bar works and synchronizes with a downloading stream


## Future steps or ideas





