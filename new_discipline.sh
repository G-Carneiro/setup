#!/bin/bash

discipline=$1
path=$2
newpath="$path/$discipline"

mkdir "$newpath" "$newpath/Slides" "$newpath/Trabalhos" "$newpath/Provas"
