# Purpose
This script is made to download multiple m3u8 playlist files to mp4 files.

# Depenencies
* [Python](https://www.python.org/) Must be in path!
* [FFmpeg](https://ffmpeg.org/) Must be in path!
* [ffmpeg-python](https://github.com/kkrffmpeg-pythonoening/ffmpeg-python) (pip module)
* [simple-calk](https://github.com/olsonpm/py_simple-chalk) (pip module)

# Installation
First of all, you need to have [Python](https://www.python.org/) and [FFmpeg](https://ffmpeg.org/) installed on your computer. Install them according to their documentation and ensure they are in your PATH/environment variables.

Install Python dependencies:
```
pip install -r requirements.txt
```

# Usage
create file `links.txt` to the src directory where each line is a single link. Before the link, there is the title of the final mp4 file name. The title and the link are separated by a comma. Example:
```
Title for the file,https://example.com/
This is an example title,https://cdn.xyz.example.com/
```

Open the src directory in your Terminal app cmd or PowerShell on Windows and run the command:
```
python main.py
```