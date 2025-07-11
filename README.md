# Title: Last Frame Extractor

## Watch the Example Video
[![Watch the Example Video](https://img.youtube.com/vi/vTbwd43GKOs/0.jpg)](https://youtu.be/vTbwd43GKOs)

## Notice
- Change the path to your folder, this code is at the end of the file
- you need python instaled on your PC
```python
if __name__ == "__main__":
    folder_to_watch = r"E:\Downloads\videonew"  # Change this to your folder path
    main(folder_to_watch)
```

# Overview:
- This Python script monitors a specified folder for new video files and automatically extracts the last frame from each video. 
- It provides an interactive user interface to confirm the clarity of the extracted frame and allows the user to save an additional frame near the end of the video if the first frame is not clear.

## Features:

- Automatic Monitoring: Continuously scans a designated folder for new video files in formats such as MP4, AVI, and MOV.
- Frame Extraction: Captures the last frame of each video and saves it as an image file.
- User Interaction: Prompts the user to confirm if the extracted frame is clear:
  - If the frame is clear, it moves on to the next video.
  - If the frame is unclear, it captures and saves another frame near the end of the video.
- Error Handling: Provides informative error messages if a video file cannot be opened or if frames cannot be read, helping users troubleshoot issues with specific video files.

# Usage:

- Set the path to the folder containing the video files in the script.
- Run the script. It will automatically process new videos as they are added to the folder.
- Follow the prompts to confirm the clarity of the extracted frames.

# Requirements:

- Python 3.x
- Basic knowledge of running Python scripts
- OpenCV library (opencv-python)
```python
pip install opencv-python opencv-python-headless numpy



