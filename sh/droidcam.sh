#!/bin/bash

# Reinstall droidcam (necessary if kernel is changed)
url="https://files.dev47apps.net/linux/droidcam_1.8.2.zip"
sudo /opt/droidcam-uninstall -y

cd /tmp/ || exit
wget -O droidcam_latest.zip "$url"
unzip droidcam_latest.zip -d droidcam
cd droidcam && sudo ./install-client -y
sudo ./install-video -y
