#!/bin/bash

target_dir=$1
icons_dir=$2

cd "$icons_dir" || exit
for file in *; do
  gio set -t string "$target_dir/${file%.*}" metadata::custom-icons_dir file://"$icons_dir/$file";
done

