#!/bin/bash

# update the old pacakges
sudo apt update
# install pip package if not present
sudo apt install python3-pip
# install qrcode library as well as pil for image
pip install qrcode[pil]
#install opencv-python
pip install opencv-python
