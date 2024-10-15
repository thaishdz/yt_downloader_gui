# Side Project: Youtube Downloader with Pytube & Tinker

This project serves as a learning jorney to deepen my understanding of various Python topics and software development practices

> [!CAUTION]
__Status : Blocked__ ⛔

## Objectives 🎯

- __Integrating libraries__: Working with external libraries such as [Pytube](https://github.com/pytube/pytube) for downloading Youtube videos and [Tkinter](https://docs.python.org/es/3/library/tkinter.html) for building graphical user interfaces (GUIs).
- __Mastering Asynchronous Programming__: Learning how to implement asynchrony in Python to avoid blocking operations.
- __Following Python Best Practices__: Writing code that adheres to [PEP8](https://peps.python.org/pep-0008/), the style guide for Python, to ensure clean and maintainable code.
- __Reading documentation__: Enhancing my skills in reading and understanding library documentation to fully leverage their features. 

## Why the Project Was blocked? ⛔
The main reason for halting development is due to the limitations of the *Pytube* library.
- __Lack of Maintenance__: Pytube has not been updated since 2011, leading to compatibility issues.
- __Frequent Breakages__: Whenever Youtube updates its API or makes change to its website, Pytube often breaks. This results in unpredictable behavior:
  - One day the library works fine, and the next day it doesn't.


## What has been the biggest challenge? 🗿
Boxing against Pytube ...

![clideo_editor_3b3d8be796cb4196ad87cbec8cfdbaab](https://github.com/user-attachments/assets/d23c9e3b-3e4f-4931-8dd0-5aed7c380251)

[Context]

I wanted the user could a choose a video resolution,
the thing is, the Progressive streams are video-audio joined but never have 
the highest resolution (720p instead 1080p), 
so I had to work with DASH (separate video and audio).

![photo_2024-07-16_21-40-23](https://github.com/user-attachments/assets/73037ab8-cd9c-4a65-8447-7abca4df94a3)


Downloading the video and audio per separate, 
is no problem because then they can be merged with a module called ffmpeg.


[Status of my app on that point]

I had 2 threads : 
1. To download the stream itself
2. To update the progress bar as the stream download progresses

That worked well 👍

[THE PROBLEM]

![image](https://github.com/user-attachments/assets/845cd57a-3366-45f5-bfa5-6d635aeceb97)

Pytube is not «thread-safe»,
because of this, it would not be able to make a third thread 
which unloads a second stream in parallel to the other 2.

## What have you learned? 💡

- How to design and set up an GUI (Tkinter)
- How streams works
- Difference between Progressive vs DASH (Dynamic Adaptive Streaming over HTTP)
- Threading and Asynchronous process (well ... something ... around 1%, I hate it)
- Events
- Buffering
- Lambdas function
- How the progress bar works and synchronizes with a downloading stream


## Next steps or ideas 🚀
1. Find alternatives to Pytube ([yt-dlp](https://github.com/yt-dlp/yt-dlp) is popular, but its api ... no)
2. Choose the directory where to save the content
3. Download only audio from videos
4. Download playlists


__Techie Stack__ 💻:
- Python ([Pytube](https://github.com/pytube/pytube))
- [Tkinter](https://docs.python.org/es/3/library/tkinter.html) (GUI)
