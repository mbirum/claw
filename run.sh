#!/bin/bash

echo "0" > output.txt
./env/bin/python receive.py &
./env/bin/python motor.py
