#!/bin/bash
#This script records a video and copies it to network location defined in .bashrc (REMOTEVIDPATH)
#Arguments: $1:Name of Video, $2: Length (minutes), $3: Frames per second
ans=$(echo "$2 * 60000" | bc)
now=$(date "+%F")
echo "Started recording at" $(date +%H:%M:%S)
raspivid -t $ans -br 50 -w 600 -h 800 --framerate $3 -b 10000000 --awb greyworld -o $1"_"$HOSTNAME"_"$now.h264
echo "Converting to mp4"
MP4Box -add $1"_"$HOSTNAME"_"$now.h264 $1"_"$HOSTNAME"_"$now.mp4 -fps $3
echo "Started data transfer to " $REMOTEVIDPATH " at " $(date +%H:%M:%S)
sshpass -p $REMOTEPASS scp $1"_"$HOSTNAME"_"$now.mp4 $REMOTE:$REMOTEVIDPATH
echo "Finished data transfer at " $(date)
rm $1"_"$HOSTNAME"_"$now.*
echo "Finished for now..."
