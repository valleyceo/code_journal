#!/bin/bash
# THIS SCRIPT IS FOR GOOGLE CODE JAM INTERACTIVE QUESTION
# SUPPORTS CPP AND PYTHON

# Extract file name
STRIN="$1"
CASE="$2"
ARG="$3"
FNAME="${STRIN%.*}"
EXT="${STRIN#*.}"
N="${STRIN:0:2}"
NAME="${FNAME:2}"
filePathFull="$(find . -name $STRIN -exec dirname {} \;)"
filePath="${filePathFull:2}"

# Compile script if extension is cpp
if [ "$EXT" == "cpp" ]
then
	g++ "${filePath}/${STRIN}" -std=c++14 -pthread -O3 -o "${filePath}/${FNAME}.o"
fi

# Run input text
INTXT="${N}0in.txt"
OUTTXT="${N}0out.txt"

# Create input file (if not present)
if [ -f "${filePathFull}/${INTXT}" ]
then
	A="A"
else
	echo "new file created"
	echo "${filePathFull}/${INTXT}"
	touch "${filePathFull}/${INTXT}"
fi

# Check if interactive python tester are present
if [ -f "interactive_runner.py" ]
then
	A="A"
else
	echo "interactive script warning: interactive_runner.py does not exist, you can download at Google coding competition webpage."
fi

# Check if interactive python tester are present
if [ -f "${filePath}/${N}testing_tool.py" ]
then
	A="A"
else
	echo "interactive script warning: Tester script does not exist, rename it to ${filePath}/${N}testing_tool.py"
fi

# run script
if [ $EXT == "cpp" ]
then
	python interactive_runner.py python "${filePath}/${N}testing_tool.py" "$CASE" -- "./${filePath}/${FNAME}.o"
else
	python interactive_runner.py python "${filePath}/${N}testing_tool.py" "$CASE" -- python "${filePath}/${STRIN}"
fi