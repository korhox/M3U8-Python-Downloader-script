# Purpose
This script is made to download multiple m3u8 playlist files to mp4 files.

# Depenencies
* (Python)[https://www.python.org/]
* (FFmpeg bin)[https://ffmpeg.org/] (must be in path)
* (ffmpeg-python)[https://github.com/kkrffmpeg-pythonoening/ffmpeg-python]
* (simple-calk)[https://github.com/olsonpm/py_simple-chalk]

# Installation
First of all, you need to have (Python)[https://www.python.org/] and (FFmpeg bin)[https://ffmpeg.org/] installed on your computer. Install them according to their documentations and ensure they are in your PATH/environment variables.

Install Python depedencies:
```
pip install -r requirements.txt
```

# Usage
create file `links.txt` to src directory where each line is a single link. Before the link there is the title of final mp4 file name. The title and the link are separated by a comma. Example:
```
Title,URL
This is an example title,https://cdn.xyz.example.com/
```

Open the src directory in your Terminal app (cmd or powershell on Windows) and run command:
```
python main.py
```