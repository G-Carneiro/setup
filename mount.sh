#!/bin/bash

sudo ntfsfix /dev/sdc1
sudo ntfsfix /dev/sdd1
echo "Done: NTFSFIX"

sudo mount -o remount /dev/sdc1
sudo mount -o remount /dev/sdd1
echo "Done: remount"

sudo chmod +w /dev/sdc1
sudo chmod +w /dev/sdd1
echo "Done: chmod"
