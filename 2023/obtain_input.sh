#!/bin/bash

day=$(date +%d | sed 's/^0//')
url="https://adventofcode.com/2023/day/$day/input"
echo $url
mkdir -p inputs

# Authenticate with Advent of Code
session_cookie=""
curl -b "session=$session_cookie" -o "inputs/day$day.txt" "$url"
