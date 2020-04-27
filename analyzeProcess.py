import sys
import deeplabcut
import os
from pathlib import Path


task='mieno20200327cw'
experimenter='tsusumu'
date='2020-03-27'
Ngputouse=1
str_videotype='.mp4'
videodir='videos/rat/200327_CW'


if len(sys.argv)>1:
    Ngputouse=int(sys.argv[1]);

path_videodir=os.path.join(os.getcwd(),videodir)

def repeatAnalyzeVideos(path_config_file,path):
    for curDir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(str_videotype):
                path_videos=os.path.join(curDir,file)
                print(path_videos)
                deeplabcut.analyze_videos(path_config_file,[path_videos], shuffle=1, videotype=str_videotype,save_as_csv=True,gputouse=Ngputouse)


path_workdir = os.path.join(os.getcwd(),task)
#path_workdir = os.path.join(os.getcwd(),'.')
path_config_file=os.path.join(path_workdir,task + '-' + experimenter + '-' + date + '/config.yaml')


path='/home/tsusumu/Deeplabcut/DLC/videos/rat/200327_CW/it'

def find_DLCResults(path):
    for curDir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".h5"):
                os.remove(os.path.join(curDir,file))
            elif file.endswith(".pickle"):
                os.remove(os.path.join(curDir,file))
            elif file.endswith(".csv"):
                os.remove(os.path.join(curDir,file))

find_DLCResults(path)

repeatAnalyzeVideos(path_config_file,path)


