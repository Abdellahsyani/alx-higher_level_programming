#!/bin/bash
# GET the body of a response if only the status code is 200
[ "$(curl -sIL -w '%{http_code}' "$1" | tail -n 1)" == 200 ] && curl -sL "$1"
