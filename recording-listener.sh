#!/bin/bash -x

# To list devices:
# /Applications/ffmpeg -f avfoundation -list_devices true -i ""

OUT_DIR="/Users/seth/Documents/recordings"
OUT_DIR=`cd "$OUT_DIR"; pwd`

FFMPEG="/Applications/ffmpeg"
INPUT_AUDIO_DEVICE=0

PID_FILE=/tmp/record.pid

pipe=/tmp/recordpipe


if [[ ! -p $pipe ]]; then
  mkfifo $pipe
fi

while :; do # if we hit end-of-FIFO, then loop around and try to reopen
  while read line <$pipe
  do
    echo "Got input:"
    echo $line
    if [[ "$line" == 'record' ]]; then
      echo "Start recording"
      OUT_FILE="out-$(date '+%Y%m%d%H%M%S').flac"
      nohup $FFMPEG -f avfoundation -i "none:$INPUT_AUDIO_DEVICE" "$OUT_DIR/$OUT_FILE" &
      pid=$!
      # Save pid to file
      echo $pid > "$PID_FILE"
    elif [[ "$line" == 'stop' ]]; then
      echo "Stop recording"
      if [ ! -f "$PID_FILE" ]; then
        echo "No recording process running currently!"
      else
        kill $(cat "$PID_FILE")
        rm "$PID_FILE"
      fi
    fi
  done
done
