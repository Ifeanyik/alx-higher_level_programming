#!/bin/bash
# this script prints the size in bytes of content downloaded with curl
curl $1 -s -w "%{size_download}" | cut -b 11-
