#!/bin/bash
# curl script
curl -sI "$1" | grep "Allow: " | cut -f2- -d " "
