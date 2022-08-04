#!/bin/bash

for f in *.pdf ; do pdf2svg "$f" "${f%.pdf}.svg" ; done
for f in *.pdf ; do rm "$f" ; done
