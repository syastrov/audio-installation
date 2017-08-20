#!/usr/bin/env python

import subprocess
import os
import os.path
import random
import glob

recordingsDir = "/Users/seth/Documents/recordings"


outputDevices = ["Fast Track", "Built-in Output"]

speakers = [0, 1, 2, 3]
speakersToDevice = {
    0: "Fast Track",
    1: "Fast Track",
    2: "Built-in Output",
    3: "Built-in Output"
}
speakersToChannel = {
    0: "L",
    1: "R",
    2: "L",
    3: "R"
}

def playAudioToDevice(audioFile, device, channel):
    my_env = os.environ.copy()
    my_env["AUDIODRIVER"] = "coreaudio"
    my_env["AUDIODEV"] = device

    if channel == "L":
        leftIn = "-"
        rightIn = "0"
    else:
        leftIn = "0"
        rightIn = "-"
    cmd = ["play", audioFile, "remix", leftIn, rightIn]
    print "Running: %s" % (" ".join(cmd))
    p = subprocess.Popen(cmd, env=my_env)
    p.wait()

def playAudio(audioFile, speakerNo):
    device = speakersToDevice[speakerNo]
    audioChannel = speakersToChannel[speakerNo]
    print "Playing on speaker %d (on device %s; channel: %s)" % (speakerNo, device, audioChannel)
    playAudioToDevice(audioFile, device, audioChannel)

while True:
    # Refresh audio file list
    files = glob.glob(recordingsDir + '/*.flac')

    speakerNo = random.choice(speakers)
    audioFile = random.choice(files)

    playAudio(audioFile, speakerNo)

