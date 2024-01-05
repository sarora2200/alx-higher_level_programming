#!/bin/bash
# sends a POST request to a passed URL, and displays body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
