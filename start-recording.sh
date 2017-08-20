#!/bin/bash -x

FFMPEG="/Applications/ffmpeg"

pipe=/tmp/recordpipe

if [[ ! -p $pipe ]]; then
  mkfifo $pipe
fi

echo "record" >$pipe 

