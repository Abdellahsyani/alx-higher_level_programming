#!/bin/bash
# Takes A URL and displays the size of the body in bytes
curl -sX POST --data-urlencode 'email=test@gmail.com' --data-urlencode 'subject=I will always be here for PLD' "$1"
