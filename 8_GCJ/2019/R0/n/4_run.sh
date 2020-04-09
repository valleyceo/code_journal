#!/bin/bash
g++ sol.cpp -std=c++14 -pthread -O3 -o sol.o
python testing_tool.py 0 sol.o