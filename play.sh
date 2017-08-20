#!/bin/bash

AUDIO_PATH="/Users/seth/Documents/recordings"

export AUDIODRIVER="coreaudio"
export AUDIODEV="Fast Track"
export AUDIODEV="Fast Track"

trap "{ kill $(jobs -pr); exit; }" SIGINT SIGTERM

while true; do
  if ps ax | grep -v grep | grep '\.flac' > /dev/null; then
    sleep 1;
  else
    # Prepare a playlist and spawn n instances of VLC, each playlist playing an
    # audio file destined to a different audio channel or device.
    for entry in $AUDIO_PATH/*; do
      echo "playing $entry";
      play "$entry" &
    done
  fi
done
