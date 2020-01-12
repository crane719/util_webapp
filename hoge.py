import glob
import os
from collections import OrderedDict
import collections
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mp
import shutil

# videoがmp4である前提
def video2mp3(video_dirs, output_dir):
    for video_dir in video_dirs:
        name = video_dir.split("/")[-1]
        name = name.replace(".mp4", "")
        clip_input = mp.VideoFileClip(video_dir).subclip()
        clip_input.audio.write_audiofile(output_dir+name+'.mp3')

def methods(obj):
    for method in dir(obj):
        print(method)

def make_dir(required_dirs):
    dirs = glob.glob("*")
    for required_dir in required_dirs:
        if not required_dir in dirs:
            print("generate file in current dir...")
            print("+ "+required_dir)
            os.mkdir(required_dir)
        print("\n")

def recreate_dir(directory):
    for dir in directory:
        shutil.rmtree(dir)
    make_dir(directory)

def is_dir_existed(directory):
    dirs = glob.glob("*")
    if directory in dirs:
        return True
    else:
        return False

def flatten(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, collections.Iterable) and not isinstance(element, str):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result
