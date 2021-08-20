#!/bin/bash
# Url options
curl -sI "$1" | cut -d' ' -f2- | grep OPTIONS
