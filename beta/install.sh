#!/bin/sh
echo "installing"
apt update  # To get the latest package lists
apt install git -y
apt install python -y
git clone https://github.com/kvvu/tweeb.git
echo "please do : python keyb.py to continue"
#
