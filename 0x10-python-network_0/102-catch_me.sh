#!/bin/bash
# request that causes the server to respond with message containing You got me!
curl -sL "0.0.0.0:5000/catch_me" -X PUT -H "Origin:HolbertonSchool" -d "user_id=98"
