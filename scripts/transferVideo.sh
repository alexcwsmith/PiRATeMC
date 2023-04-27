#!/bin/bash
#This script copies all .mp4 videos in the working directory to a network location defined in .bashrc ($REMOTEVIDPATH). This is primarily useful if videos are not automatically transferred after recorded with the recordVideo.sh script.

echo "Started data transfer to " $REMOTEVIDPATH " at " $(date +%H:%M:%S)

for i in $(find *mp4); do
	sshpass -p $REMOTEPASS scp $i $REMOTE:$REMOTEVIDPATH
	#rm $i
done

echo "Finished data transfer at " $(date)
