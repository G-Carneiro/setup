#!/bin/bash

sudo /opt/droidcam-uninstall -y

cd /tmp/ || exit
wget -O droidcam_latest.zip https://files.dev47apps.net/linux/droidcam_1.8.2.zip
unzip droidcam_latest.zip -d droidcam
cd droidcam && sudo ./install-client -y
sudo ./install-video -y
