#!/bin/sh
apt update  # To get the latest package lists
apt install git -y && apt install python -y
git clone https://github.com/kvvu/tweeb.git
pip install -r requirements.txt | grep -v "Requirement already satisfied"
#
