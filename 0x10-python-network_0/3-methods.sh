#!/bin/bash
# Takes A URL and displays the size of the body in bytes
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
