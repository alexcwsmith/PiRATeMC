#!/bin/bash
#This script records a video and converts it to an mp4 and stores it locally.
#Arguments: $1:Name of Video, $2: Length (minutes), $3: Frames per second
ans=$(echo "$2 * 60000" | bc)
now=$(date "+%F")
echo "Started recording at" $(date +%H:%M:%S)
raspivid -t $ans -br 50 -w 600 -h 800 --framerate $3 -b 10000000 --awb greyworld -o $1"_"$HOSTNAME"_"$now.h264
echo "Converting to mp4"
MP4Box -add $1"_"$HOSTNAME"_"$now.h264 $1"_"$HOSTNAME"_"$now.mp4 -fps $3
echo "Finished for now..."
