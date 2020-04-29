import sys
import deeplabcut
import os
from pathlib import Path

homeDir='c:/Users/labmember'
task='DecNes'
experimenter='tsusumu'
date='2020-03-19'
Ngputouse=0
str_videotype='.mp4'



if len(sys.argv)>1:
    Ngputouse=int(sys.argv[1]);


def repeatAnalyzeVideos(path_config_file,path):
    for curDir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(str_videotype):
                path_videos=os.path.join(curDir,file)
                print(path_videos)
                deeplabcut.analyze_videos(path_config_file,[path_videos], shuffle=1, videotype=str_videotype,save_as_csv=True,gputouse=Ngputouse)


path_workdir = os.path.join(homeDir,task)
#path_workdir = os.path.join(os.getcwd(),'.')

path_config_file=os.path.join(path_workdir,task + '-' + experimenter + '-' + date + '/config.yaml')

print(path_config_file)
path='H:/intan/data/azechi'

def find_DLCResults(path):
    for curDir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".h5"):
                os.remove(os.path.join(curDir,file))
            elif file.endswith(".pickle"):
                os.remove(os.path.join(curDir,file))
            elif file.endswith(".csv"):
                os.remove(os.path.join(curDir,file))

#find_DLCResults(path)

repeatAnalyzeVideos(path_config_file,path)


