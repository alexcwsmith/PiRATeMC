#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:40:38 2022

@author: smith
"""
import os
os.chdir('/d1/software/PiRATeMC/')
import tkinter as tk
from tkinter import Button, Radiobutton, Entry, Label
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import ttk
import csv
from paramiko import SSHClient
from datetime import datetime as dt

#%%
def getIPs():
    global boxes
    global addrs
    IPs = askopenfilename(title = 'Select CSV with IDs and IPs', filetypes =  [('CSV', '*.csv')])
    boxes = []
    addrs = []
    with open(IPs, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            boxes.append(row[0])
            addrs.append(row[1])
            
    return boxes, addrs

def makeIPdict(boxes, addrs):
    global IPdict
    IPdict = {boxes[i]:addrs[i] for i in range(len(boxes))}
    
getIPs()
makeIPdict(boxes, addrs)
#%%

def getBoxIP(boxnum):
    global IPaddr
    global box
    box = boxnum
    IPaddr = IPdict["Box"+str(box)]
    
def startRecording():
    IP = IPaddr
    if 'vidTitle' not in globals():
        vidTitle="Started"+dt.now().strftime('%H:%M:%S')
    if time not in globals():
        time = 10
    if 'fpsVal' not in globals():
        fpsVal = 30
    cmd = "./recordVideo.sh " + ' '.join([str(vidTitle), str(time), str(fpsVal)])
    #cmd = "touch testBox"+str(box)+".txt && sshpass -p password scp testBox"+str(box)+".txt rpicam@10.1.1.243:~/ "
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(IP, username='pi', password='oxycodone')
    msg = "Sending command '" + str(cmd) + "' to box " + str(box) + " with IP " + str(IP) + " with FPS " + str(fpsVal) + " and duration " + str(time)
    print(msg)
    stdin, stdout, stderr = client.exec_command(cmd)
    showinfo(title="Recording started", message=msg)
    
def startAll():
    boxes = IPdict.keys()
    IPs = IPdict.values()
    for box in boxes:
        IP = IPdict[box]
       # cmd = "touch test"+str(box)+".txt && sshpass -p password scp test"+str(box)+".txt rpicam@10.1.1.243:~/ "
        if 'vidTitle' not in globals():
            vidTitle="Started"+dt.now().strftime('%H:%M:%S')
        else:
            vidTitle=globals()['vidTitle']
        if 'time' not in globals():
            time = 10
        else:
            time = globals()['time']
        if 'fpsVal' not in globals():
            fpsVal = 30
        else:
            fpsVal=globals()['fpsVal']
        cmd = "./recordVideo.sh " + ' '.join([str(vidTitle), str(time), str(fpsVal)])

        client = SSHClient()
        client.load_system_host_keys()
        client.connect(IP, username='pi', password='oxycodone')
        msg = "Sending command '" + str(cmd) + "' to " + str(box) + " with IP " + str(IP) + " with FPS " + str(fpsVal) + " and duration " + str(time)
        print(msg)
        stdin, stdout, stderr = client.exec_command(cmd)
    showinfo(title="Start all complete", message="Recording started for all boxes")

def rmAllVidFiles():
    IP = IPaddr
    cmd = 'rm *.mp4'
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(IP, username='pi', password='oxycodone')
    msg = "Sending command " + str(cmd) + "to box " + str(box) + " with IP " + str(IP)
    print(msg)
    stdin, stdout, stderr = client.exec_command(cmd)


#%% 
root = tk.Tk()
root.title("PiRATeMC GUI")

title = tk.StringVar()
titleLabel = Label(root, text="Enter title for video(s):")
titleLabel.pack()
titleBox = Entry(root, textvariable=title)
titleBox.pack()

def setTitle():
    global vidTitle
    vidTitle = titleBox.get()
    msg = "Video title set to " + str(vidTitle)
    showinfo(title="Video title set", message=msg)

Button(root, text="Set Title", command=setTitle).pack()

fps = tk.StringVar()
fpsLabel = Label(root, text="Enter Frame Rate (fps):")
fpsLabel.pack()
fpsBox = Entry(root, textvariable=fps)
fpsBox.pack()

def setFPS():
    global fpsVal
    fpsVal = fpsBox.get()
    msg = "Frame rate set to " + str(fpsVal) + " FPS"
    showinfo(title='Frame Rate', message=msg)
    print(msg)

Button(root, text="Set FPS", command=setFPS).pack()

duration = tk.StringVar()
durationLabel = Label(root, text="Enter duration (minutes):")
durationLabel.pack()
durationBox = Entry(root, textvariable=duration)
durationBox.pack()

def setDuration():
    global time
    time = durationBox.get()
    msg = "Duration set to " + str(time) + " minutes"
    showinfo(title='Duration', message=msg)
    print(msg)

Button(root, text="Set duration (minutes)", command=setDuration).pack()
Button(root, text='Pi 1', command=lambda *args: getBoxIP(1)).pack()
if len(IPdict)>1:
    Button(root, text='Pi 2', command=lambda *args: getBoxIP(2)).pack()
if len(IPdict)>2:
    Button(root, text='Pi 3', command=lambda *args: getBoxIP(3)).pack()
if len(IPdict)>3:
    Button(root, text='Pi 4', command=lambda *args: getBoxIP(4)).pack()
if len(IPdict)>4:
    Button(root, text='Pi 5', command=lambda *args: getBoxIP(5)).pack()
if len(IPdict)>5:
    Button(root, text='Pi 6', command=lambda *args: getBoxIP(6)).pack()
if len(IPdict)>6:
    Button(root, text='Pi 7', command=lambda *args: getBoxIP(7)).pack()
if len(IPdict)>7:
    Button(root, text='Pi 8', command=lambda *args: getBoxIP(8)).pack()
if len(IPdict)>8:
    Button(root, text='Pi 9', command=lambda *args: getBoxIP(9)).pack()
if len(IPdict)>9:
    Button(root, text='Pi 10', command=lambda *args: getBoxIP(10)).pack()
if len(IPdict)>10:
    Button(root, text='Pi 11', command=lambda *args: getBoxIP(11)).pack()
if len(IPdict)>11:
    Button(root, text='Pi 12', command=lambda *args: getBoxIP(12)).pack()
if len(IPdict)>12:
    Button(root, text='Pi 13', command=lambda *args: getBoxIP(13)).pack()
if len(IPdict)>13:
    Button(root, text='Pi 14', command=lambda *args: getBoxIP(14)).pack()
if len(IPdict)>14:
    Button(root, text='Pi 15', command=lambda *args: getBoxIP(15)).pack()
if len(IPdict)>15:
    Button(root, text='Pi 16', command=lambda *args: getBoxIP(16)).pack()
if len(IPdict)>16:
    Button(root, text='Pi 17', command=lambda *args: getBoxIP(17)).pack()
if len(IPdict)>17:
    Button(root, text='Pi 18', command=lambda *args: getBoxIP(18)).pack()
if len(IPdict)>18:
    Button(root, text='Pi 19', command=lambda *args: getBoxIP(19)).pack()
if len(IPdict)>19:
    Button(root, text='Pi 20', command=lambda *args: getBoxIP(20)).pack()

Button(root, text="Start Recording", command=startRecording).pack()
Button(root, text="Start All", command=startAll).pack()

def openUtilities():
    utils = tk.Tk()
    utils.title('Utilities')
    Button(utils, text="Get disk usage statistics", command=getDiskUsage).pack()

root.mainloop()
