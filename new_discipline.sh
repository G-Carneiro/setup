#!/bin/bash

name=$1
path=$2

cd "$path" || exit
mkdir "$name"

cd "$name" || exit
mkdir Slides Trabalhos Provas