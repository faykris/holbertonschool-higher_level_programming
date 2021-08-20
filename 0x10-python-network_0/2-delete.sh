#!/bin/bash
# sends a DELETE request URL passed as first argument, displays body response
curl -sX DELETE "$1" 
