#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl "$1" -X GET -sH "X-HolbertonSchool-User-Id=98"
