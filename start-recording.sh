#!/bin/bash -x

{ echo "record"; sleep 0.1; } | telnet localhost 50123
