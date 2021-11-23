# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:24:19 2018

@author: takahashilab
"""

import cv2
import os
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio


#parameters
DLCName0='DeepCut'
DLCName1='DeepCut_resnet'
DLCName2='shuffle1_1030000.h5'

#task='PDmouseLED'
#task='seabird201810241527'
task='trout'
#video='videos/current/PDmouseNOLED.mp4'
#video='videos/current/examples/images1811051905.mp4'
#videodir=os.path.split(video)[0]
#videodir='videos/rat'
#videodir='videos/seabird/201810241527'
#videodir='videos/trout/'
#videodir='videos/rat/'
#videodir='videos/seabird/'
#videodir='videos/DHL/'
#videodir='videos/seabird/'
videodir='.'

"""
videoName=os.path.split(video)[1]
videoN=os.path.splitext(videoName)[0]
path_videos = os.path.join(os.getcwd(),video)
path_workdir = os.path.join(os.getcwd(),task)
path_config_file=os.path.join(path_workdir,'PDmouseLED-tsusumu-2018-11-29/config.yaml')
"""
path_videodir = os.path.join(os.getcwd(),videodir)
#path_videodir='/home/tsusumu/Dropbox/DeepHLVideo/'
"""
#read config file
with open(str(path_config_file),'r') as file:
    cfg= yaml.load(file)
Task = str(cfg['Task'])
date = str(cfg['date'])
resnet = str(cfg['resnet'])
"""

"""
#check the total number of frames in the video        
#cap = cv2.VideoCapture(path_videos)
#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#print( length )
if x1.size==length:
        print('tracking OK!', length, x1.size)
    else:
        print('tracking Bad', length, x1.size)
#read tracked points
#h5fname=videoN + DLCName1 + resnet + '_' + Task + date + DLCName2
#path_h5file=os.path.join(os.getcwd(),videodir + '/' + h5fname)
"""



def convDLC2mat(path_h5file):
    Dataframe=pd.read_hdf(path_h5file)
    scorer=np.unique(Dataframe.columns.get_level_values(0))[0]
    bodyparts2plot = list(np.unique(Dataframe.columns.get_level_values(1)))
    bp=bodyparts2plot[0]
    x1=Dataframe[scorer][bp]['x']
    y1=Dataframe[scorer][bp]['y']
    bp=bodyparts2plot[1]
    x2=Dataframe[scorer][bp]['x']
    y2=Dataframe[scorer][bp]['y']
    """
    bp=bodyparts2plot[2]
    x3=Dataframe[scorer][bp]['x']
    y3=Dataframe[scorer][bp]['y']
    """
    #x,y dimensions of two body parts detected by DLC
    xydims=np.vstack((x1,y1,x2,y2))
#    xydims=np.vstack((x1,y1,x2,y2,x3,y3))
    plt.plot(x1,y1)
    #check the consistency between video and tracked points
    #save mat file
    fname=os.path.splitext(path_h5file)[0] 

    #path_matfile=os.path.splitext(path_h5file)[0] + '.mat'
    path_matfile=fname.split(DLCName0)[0] + '.mat'
    print(path_matfile)
    #path_matfile=os.path.join(os.getcwd(),matfname + '.mat')
    scio.savemat(path_matfile,{'xydims':xydims})
    
def find_h5(path):
    for curDir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".h5"):
                convDLC2mat(os.path.join(curDir,file))

find_h5(path_videodir)
