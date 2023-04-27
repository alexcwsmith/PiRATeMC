#!/bin/bash
#This script converts all .h264 videos in working directory to .mp4, and removes the raw .h264 files.

echo "Converting to mp4"

for i in $(find *h264); do
	MP4Box -add $i ${i%%.*}.mp4 -fps 30
	rm $i
done

echo "Finished for now..."
