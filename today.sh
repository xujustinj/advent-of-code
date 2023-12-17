#!/bin/sh

# THIS SCRIPT IS MEANT TO BE SOURCED, NOT RUN
# source today.sh

mamba activate advent-of-code
python -m $(date +"%Y.%d")
