#!/bin/bash
# request to a URL passed as the first argument and displays body of response
curl --silent --header "Content-Type: application/json" --request POST --data @"$2" "$1"
