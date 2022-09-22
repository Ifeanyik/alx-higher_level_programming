#!/bin/bash
# this script prints the size in bytes of content downloaded with curl
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
