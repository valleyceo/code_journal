#!/bin/bash
# THIS SCRIPT IS FOR GOOGLE CODE JAM TESTING
# SUPPORTS CPP and PYTHON

# Extract file name
STRIN="$1"
FNAME="${STRIN%.*}"
EXT="${STRIN#*.}"
N="${STRIN:0:2}"
NAME="${FNAME:2}"
filePathFull="$(find . -name $STRIN -exec dirname {} \;)"
foundPathCount=$(find . -name $STRIN -exec dirname {} \; | wc -l)
filePath="${filePathFull:2}"

if [ $foundPathCount -eq 0 ];
then
	echo "Error: No files named $STRIN have been found."
	exit 1
elif [ $foundPathCount -gt 1 ];
then
	echo "Error: Multiple files of $STRIN have been found. Locations are:"
	echo "$filePathFull"
	exit 1
fi

# Compile script if extension is cpp
if [ "$EXT" == "cpp" ]
then
	g++ "${filePath}/${STRIN}" -std=c++14 -pthread -O3 -o "${filePath}/${FNAME}.o"
	echo "completed c++ compiling!"
fi

# Run input text
INTXT="${N}0in.txt"
OUTTXT="${N}0out.txt"

# Create input file (if not present)
if [ -f "${filePath}/${INTXT}" ]
then
	A="A"
else
	echo "new file created"
	touch "${filePath}/${INTXT}"
fi

# run script
start=$(date +%s)
if [ $EXT == "cpp" ]
then
	"./${filePath}/${FNAME}.o" < "${filePath}/$INTXT" > "${filePath}/$OUTTXT"
else
	python "${filePath}/${STRIN}" < "${filePath}/$INTXT" > "${filePath}/$OUTTXT"
fi
end=$(date +%s)
runtime=$(python -c "print(${end} - ${start})")
echo "Runtime: $runtime second(s)."