#!/bin/bash
# request that causes the server to respond with message containing You got me!
curl --silent -L "0.0.0.0:5000/catch_me" --request PUT --header "Origin:HolbertonSchool" --data "user_id=98"
