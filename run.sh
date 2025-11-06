#!/bin/bash

echo "0" > value.txt
./env/bin/python receive.py &
./env/bin/python motor.py
