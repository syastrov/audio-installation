#!/bin/bash -x

{ echo "stop"; sleep 0.1; } | telnet localhost 50123
