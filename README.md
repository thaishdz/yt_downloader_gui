# YT Downloader with Pytube & Tkinter
__Status : Abandoned__

## Why it was abandoned?
The main reason is because *Pytube* is an obsolete library (not updates since 2021)
Every time YouTube updates its API, things break (logically). 
One day it works fine, the next it doesn't

## What were the objectives with yt_downloader_gui?

- Learning about the __integration of libraries__ (Pytube & Tkinter)
- Learning how __library works__ (Pytube)
- Learning about __GUIs__
- Learning how __Asynchrony__ works in Python
- Learning about __threading__ module
- Learning __good practices__ (PEP8 - Style Guide for Python Code)

# Which has been the biggest challenge? 
Boxing with Pytube hahaha. 

[Context]

I wanted the user could a choose a video resolution,
the thing is, the Progressive streams are video-audio joined but never have 
the highest resolution (720p instead 1080p), 
so I had to work with DASH (separate video and audio).

Downloading the video and audio per separate, 
is no problem because then they can be merged with a module called ffmpeg.

[State of my app on that point]


[Problematic]

The problem itself was, pytube has no "thread-safe"



## What have you learned?

- How to design and set up an GUI (Tkinter)
- How streams works
- Difference between Progressive vs DASH (Dynamic Adaptive Streaming over HTTP)
- Threading and Asynchronous process (well ... something ... around 1%, I hate it)
- Events
- Buffering
- Lambdas function
- How the progress bar works and synchronizes with a downloading stream



