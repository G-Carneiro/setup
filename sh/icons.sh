#!/bin/bash

dir=$1
icon=$2

gio set -t string "$dir" metadata::custom-icon file://"$icon"

