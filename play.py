#!/usr/bin/env python

import subprocess
import os
import os.path
import random
import glob

import settings


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

lastFile = None

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
    print "Playing %s on speaker %d (on device %s; channel: %s)" % (audioFile, speakerNo, device, audioChannel)
    playAudioToDevice(audioFile, device, audioChannel)

while True:
    # Refresh audio file list
    speakerNo = random.choice(speakers)
    
    audioFile = None
    while audioFile == lastFile or audioFile is None:
        files = glob.glob(settings.RECORDINGS_DIR + '/*.' + settings.FILE_FORMAT)
        audioFile = random.choice(files)
    
    lastFile = audioFile
    playAudio(audioFile, speakerNo)

