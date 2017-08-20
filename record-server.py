#!/usr/bin/env python

import SocketServer
from datetime import datetime
import os
import subprocess

import settings


# Global to store the Popen object corresponding to the recording process
record_process = None


class TCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        global record_process
        data = self.rfile.readline().strip()
        print(data)
        if data == "record":
            if record_process is not None:
                # Terminate any existing process
                print "There's already a recording process, so we're stopping it first."
                record_process.terminate()

            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = "out-{}.{}".format(now, settings.FILE_FORMAT)
            record_command = "{}"
            dest_file = os.path.join(settings.RECORDINGS_DIR, filename)
            print "Start recording to file {}".format(dest_file)
            record_process = subprocess.Popen([settings.FFMPEG_CMD, "-f",
                "avfoundation", "-i", "none:{}".format(settings.INPUT_AUDIO_DEVICE), dest_file])
        elif data == "stop":
            print "Stop recording"
            if record_process is not None:
                record_process.terminate()
            else:
                print "No recording process running currently!"

if __name__ == "__main__":
    HOST, PORT = "localhost", 50123

    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()


