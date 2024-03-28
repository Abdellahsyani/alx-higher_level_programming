#!/bin/bash
# Takes A URL and displays the size of the body in bytes
curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
