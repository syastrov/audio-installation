#!/bin/bash

AUDIO_PATH="/Users/seth/projects/audio/audio-installation/recordings"

VLC="/Applications/VLC.app/Contents/MacOS/VLC"

trap "{ kill $(jobs -pr); exit; }" SIGINT SIGTERM

while true; do
  if ps ax | grep -v grep | grep $VLC > /dev/null; then
    sleep 1;
  else
    # Prepare a playlist and spawn n instances of VLC, each playlist playing an
    # audio file destined to a different audio channel or device.
    for entry in $AUDIO_PATH/*; do
      echo "playing $entry";
      $VLC --play-and-exit $entry > /dev/null
    done
  fi
done
