import ffmpeg
import time
from pathlib import Path
from simple_chalk import *
import os

# OPTIONS
quiet_output = True
stack = 5
cooldown = 0  # seconds (600s = 10min)

# CODE
os.system("cls" if os.name == "nt" else "clear")

print(blue("M3U8 to video Downloader Script\n"))

try:
    f = open("links.txt", "r", encoding="utf-8")
except Exception as e:
    print(red.bold("File opening failed. Does the file exist?") + "Error:\n", e)
    exit()

try:
    lines = f.read().split("\n")
except Exception as e:
    print(red.bold("Incorrect file format.") + "Error:\n", e)
    exit()


errors = 0
warnings = 0

for i, line in enumerate(lines):
    if i % stack == 0:
        time.sleep(cooldown)

    try:
        line = line.split(",")
        title = line[0].strip()
        link = line[1].strip()
    except:
        print(red.bold("Invalid line formatting on line " + white(str(i+1)) + ". Skipping..."))
        errors += 1
        continue

    if Path(title + ".mp4").exists():
        print(yellow("File " + title + ".mp4 already exists. Skipping..."))
        warnings += 1
        continue

    try:
        print(blue("Downloading file: ") + cyan(title) + " " + blue(str(i+1) + "/" + str(len(lines))))
        stream = ffmpeg.input(link)
        stream = ffmpeg.output(stream, title + ".mp4", acodec="copy", vcodec="copy")
        ffmpeg.run(stream, quiet=quiet_output)
        print(green.bold("File downloaded successfully "))
    except Exception as e:
        print(red.bold("Error occured during download. ") + "Error:\n", e)
        errors += 1
        continue

print()

if errors:
    print(red("During script completion there was ") + red.bold(str(errors)) + red(" errors."))

if warnings:
    print(yellow("During script completion there was ") + yellow.bold(str(warnings)) + yellow(" warnings."))

print(green("All operations done."))
