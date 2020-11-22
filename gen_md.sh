#!/bin/bash

EASY="$(find . -name "1_*.cpp" -o -name "1_*.py" -not -path "./[7-9]_*" | wc -l)"
MEDIUM="$(find . -name "2_*.cpp" -o -name "2_*.py" -not -path "./[7-9]_*" | wc -l)"
HARD="$(find . -name "3_*.cpp" -o -name "3_*.py" -not -path "./[7-9]_*" | wc -l)"
PYTHON="$(find . -name "*.py" -not -path "./[7-9]_*" | wc -l)"
CPP="$(find . -name "*.cpp" -not -path "./[7-9]_*" | wc -l)"

printf '## Problems  \n\n```  ' > tree.md
tree -P "*.cpp|*.py" >> tree.md
printf "Easy:\t$EASY\n" >> tree.md
printf "Medium:\t$MEDIUM\n" >> tree.md
printf "Hard:\t$HARD\n" >> tree.md
printf "C++:\t$CPP\n" >> tree.md
printf "Python:\t$PYTHON\n" >> tree.md
echo '```  ' >> tree.md
cat code_journal.md tree.md > readme.md
rm tree.md