import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("Szozat (Liszt Ferenc feldolgozasa S.486 - reszlet alapjan vegyeskarra es szimfonikus....mp4"))
video.audio.write_audiofile(os.path.join("Szozat (Liszt Ferenc feldolgozasa S.486 - reszlet alapjan vegyeskarra es szimfonikus....mp3"))