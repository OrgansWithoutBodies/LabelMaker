#!/bin/bash
/home/v/.venv/bin/python labelMaker.py "$1"
lpr ./test.png
