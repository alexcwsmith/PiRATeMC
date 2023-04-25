#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:50:49 2023

@author: smith
"""

import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
import deeplabcut as dlc

videoFormat = '.mp4'

config ='/d1/studies/DLC_Data/vGluT2_RTA-smith-2022-01-18/config.yaml' #if new, modify this after you've created the new project
videoDirectory='/d1/studies/DLC_Data/vGluT2_RTA-smith-2022-01-18/vidsToAnalyze/'

vids = [os.path.join(videoDirectory, x) for x in os.listdir(videoDirectory) if x.endswith(videoFormat)]

dlc.analyze_videos(config, vids, videotype=videoFormat, save_as_csv=True, batchsize=64)



