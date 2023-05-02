# Welcome to Pi-based Remote Acquisition Technology for Motion Capture (PiRATeMC) - version 0.1

Developed by Sam Centanni & Alex Smith

#### PiRATeMC is a local-area-network (LAN) based system for controlling a large number of Raspberry Pi video cameras simultaneously.
This works by configuring a 'remote controller' computer as a DHCP server to assign IP addresses, and using ClusterSSH to simultaneously access many devices.

### Links
---------
* This code is licensed under the [BSD license](https://opensource.org/license/bsd-3-clause/).
* Find a pre-print of our [paper on bioRxiv](https://www.biorxiv.org/content/10.1101/2021.07.23.453577v2) (stay tuned for updates on publication).
* You can find the [operating systems and instructional videos here](https://drive.google.com/drive/folders/1Y9IGVBCkBdnRykqMNaKmlipFwnT6WQuY?usp=share_link).
    - **PiCamOS_cluster** is best for LAN use with several Pis.
    - **PiCamOS_Standalone** is best for local use cases using only a single Pi at a time.
    - Both operating systems are modified versions of Raspberry Pi OS Buster Lite.
* Instructional videos can be found in the docs/videos folder, or [on Google Drive here](https://drive.google.com/drive/folders/1h3RB60rbriQN1XQFxuanafKPQfGkNtjc?usp=sharing).
* [Please report any issues to us](https://github.com/alexcwsmith/PiRATeMC/issues).

### Installation
---------------
We have included a version of rpi-imager in this repository, because newer versions of rpi-imager may not work with Ubuntu 18.04. We plan to update all of this code for Ubuntu 22 in the not-too-distant future.

Flashing the provided PiCamOS is the recommended way to install on a Raspberry Pi. The setupScripts/ folder has information to reproduce this OS. The following packages on the Pi can be installed via apt:
1. sshpass
2. gpac
3. uv4l 
4. uv4l-raspicam
5. uv4l-raspicam-extras 
6. uv4l-webrtc

We also recommend installing the [Adafruit PiTFT driver](https://learn.adafruit.com/pages/11945/elements/3074230/download) for use with a 2.8" touch screen if necessary for troubleshooting.

On the server side, the Ubuntu computer that will serve as the remote controller requires the following packages that can be installed via apt:

1. git
2. openssh-server
3. clusterssh
4. isc-dhcp-server
5. bind9

Detailed installation instructions can be found in our preprint [here](https://www.biorxiv.org/content/10.1101/2021.07.23.453577v2), and will be updated when a published version is out.

## Scripts
-----------
The main script to capture videos is at scripts/recordVideo.sh. This script assumes that several variables are set in your .bashrc file (or from exporting manually): $REMOTE, $REMOTEPASS, $REMOTEVIDPATH, as these provide the location to transfer video to when done recording. If you only want to record locally and not transfer to a network location, you can use recordVideo_local.sh

In addition to the platform for synchronously controlling many cameras through a DHCP server, we also provide several scripts and wiring diagrams for integrating GPIO pins. These scripts can be run simultaneously with the recordVideo.sh script in the terminal, for example:

```
./recordVideo.sh & pulseTTLandLED.py
```

Will run both of those scripts, in our hands there is approximately 20-30 millisecond delay between the two actions.

The pulseTTLandLED.py script outputs a 0.5s TTL signal and illuminates an LED at the same time, every 30 seconds. We use this to send a TTL out to a fiber photometry system, and have the LED illuminated in the frame of the video, and these can then be used to time-lock the behavioral data from the video with fiber photometry data. [A picture of how to wire a Pi up to receive a TTL and illuminate a small LED is here](./images/TTL\_and\_LED_Wiring.png

The script receiveTTL.py allows for triggering recording with a TTL pulse onto a GPIO pin. This script depends on more system variables that are self explanatory: $vidName, $vidLength, $vidFPS. If these variables are not found, defaults will be used, and the defaults can be changed within each script. [A picture of how to wire a Pi up to receive this signal is here](./images/receiveTTL_wiring.png).

## Automating data analysis with DLC
------------------------------------
We also provide a script to use DeepLabCut to analyze videos (AnalyzeVideos_DLC.py). This script depends on having a pre-trained DLC network, and you must change a few variables in the script to be correct for your system:

1. videoFormat : str, type of video that you want to analyze (most likely '.mp4').
2. config : str, path to config file for pre-trained DLC network.
3. videoDirectory : str, path to directory where videos to analyze are (most likely $REMOTEVIDPATH from PiRATeMC).

To use [CRON](https://www.geeksforgeeks.org/crontab-in-linux-with-examples/)to run a script automatically on Linux, enter the following command into a terminal:

```
crontab -e
```

This will bring up a window that looks like ![this](./images/crontab_-e.png):

The window has instructions for how to use CRON to automate tasks. In our example the line we have entered is:
```
0 0 * * * python3 /d1/software/PiRATeMC/AnalyzeVideos_DLC.py)
```
To break down the components of this line:
```
0 0
```
corresponds to 'minute, hour', so 0 0 indicates at 12am (midnight)

The next 3 are 'day of month, month, day of week', and inserting:
```
* * *
```
instructs it to run every day.

The final part is the command to run:
```
python3 /d1/software/PiRATeMC/AnalyzeVideos_DLC.py
```
tells it to use python3 to run the script to analyze videos.

#### We will be updating this regularly over the next several months (as of April 2023) and this is very much still in development. We will produce more documentation as well as more code, and we appreciate pull requests or suggestions!

