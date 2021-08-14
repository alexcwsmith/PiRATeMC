ans=$(echo "$2 * 60000" | bc)
now=$(date "+%F")
name=$(echo $HOSTNAME)
raspivid -t $ans -br 50 -w 600 -h 800 --framerate $3 -b 10000000 -awb greyworld -o $1_$name_$now.h264
MP4Box -add $1_$name_$now.h264 $1_$name_$now.mp4 -fps $3
sshpass -f ".pass_file" scp $1_$name_$now.mp4 rpi@10.81.104.166:/d1/studies/Raspicam/
rm $1_$name_$now.h264
