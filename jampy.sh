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
if [ "$EXT" == "cpp" ] && [ "$ARG" == "1" ]
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
	touch "${filePathFull}/${INTXT}"
fi

# Check if interactive python tester are present
if [ -f "${filePathFull}/${N}interactive.py" ]
then
	A="A"
else
	echo "Interactive script does not exist, locate and rename to ${filePath}/${N}interactive.py"
fi

# Check if interactive python tester are present
if [ -f "${filePathFull}/${N}tester.py" ]
then
	A="A"
else
	echo "Tester script does not exist, rename to ${N}tester.py"
fi

# run script
if [ $EXT == "cpp" ]
then
	python "${filePathFull}/${N}interactive.py" python "${filePath}/${N}tester.py" "$CASE" -- "./${filePath}/${FNAME}.o"
else
	python "${filePathFull}/${N}interactive.py" python "${filePath}/${N}tester.py" "$CASE" -- "${filePath}/${STRIN}"
fi