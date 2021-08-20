#!/bin/bash
# Displays the size of the body of the response
curl "$1" -sX POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
