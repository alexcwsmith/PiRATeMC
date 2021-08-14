#!/bin/bash
sudo apt update
sudo apt install sshpass gpac clusterssh bc python3-pip -y
curl https://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
echo 'deb https://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main' | sudo tee -a /etc/apt/sources.list
sudo apt update
sudo apt install uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-webrtc -y
exit
