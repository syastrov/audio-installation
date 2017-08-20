#!/bin/bash -x

pipe=/tmp/recordpipe

if [[ ! -p $pipe ]]; then
  mkfifo $pipe
fi

echo "stop" >$pipe 

