#!/bin/bash
# curl script
curl -o /dev/null -s -w "%{http_code}" $1
