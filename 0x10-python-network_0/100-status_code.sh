#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
