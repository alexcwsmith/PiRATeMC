#!/bin/bash
echo "$1" > $HOME/.pass_file
sudo chmod 400 $HOME/.pass_file
exit
