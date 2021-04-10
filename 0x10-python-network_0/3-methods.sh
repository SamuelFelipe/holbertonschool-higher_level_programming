#!/bin/bash
# Displays the size of the body of the response
curl -sI "$1" | cut -d' ' -f2- | grep OPTIONS
