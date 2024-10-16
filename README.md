# Side Project: Youtube Downloader with Pytube & Tinker

> [!WARNING]
This project is for educational purposes only. It serves as a learning journey aimed at deepening my understanding of various Python concepts and software development practices.


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


## What Has Been the Biggest Challenge? 🗿
Boxing against Pytube ...

![clideo_editor_3b3d8be796cb4196ad87cbec8cfdbaab](https://github.com/user-attachments/assets/d23c9e3b-3e4f-4931-8dd0-5aed7c380251)

Working with Pytube has been like going toe-to-toe with an unpredictable opponent. One of the most significant challenges has been handling video resolution selection:

🥊 __Progressive vs DASH Streams__: While Progressive streams come with video and audio combined, they are limited to lower resolutions (maxing out at _720p_). For higher resolutions like _1080p_ or above, I had to work with DASH streams, where video and audio are separate files that need to be downloaded and merged.

🥊 __Implementing DASH Stream Handling__: Using __DASH__ required extra steps to manually download the separate video and audio streams, then merge them using tools like `ffmeg`. This added complexity to the code and introduced new challenges, such as managing dependencies and ensuring seamless merging.


![photo_2024-07-16_21-40-23](https://github.com/user-attachments/assets/73037ab8-cd9c-4a65-8447-7abca4df94a3)


🥊 __User Experience Considerations__: Allowing users to choose the resolution meant balancing, simplicity and functionality. I had to desing the application to account for both _Progressive_ and _DASH_ streams while keeping the interface user-friendly.


Despite these obstacules, figuring out how to deal with different stream types was a rewarding learning experience,deepening my understanding of video formats and programmatic video processing.

## Lessons Learned 📚

![image](https://github.com/user-attachments/assets/845cd57a-3366-45f5-bfa5-6d635aeceb97)

This project, despite its challenges, offered valuable learning experiences:

- The importance of selecting well-maintained libraries project.
- How to handle frequent updates and breaking changes when working with third-party libraries.
- Real world problem solving skills for debugging issues caused by external dependencies.


## Next steps 🚀

While Pytube may not be a suitable long-term solution, here are some future directions I'm considering ... :
1. __ Exploring alternatives__: Investigating other libraries like ([yt-dlp](https://github.com/yt-dlp/yt-dlp).
2. __Switching to a Different GUI Framework__: Considering other framework such as _PyQt_ or _Kivy_ for a more modern look and additional features.
3. __Contributing to Open Source__: Potencially contributing to the _Pytube_ project or other similar open-source projects to help improve the tools I'm using.


## Requirements 📦

To run the project, you’ll need:

- Python 3.6+: Make sure you have a compatible version installed.
- Dependencies: Install the required libraries:
- 
```sh
pip install pytube
```

### Running the Project ▶️

1. Clone the Repository:

```sh
git clone <repository-url>
cd <repository-folder>
```

2. Run the Script
```sh
python ./app.py
```

Easy, right? 🤠

---

## Contributing 🤝

Since this is a learning project, contributions are more than welcome! Feel free to submit a pull request or open an issue with suggestions.

