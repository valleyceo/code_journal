#!/bin/bash

#source: https://stackoverflow.com/questions/23989232/is-there-a-way-to-represent-a-directory-tree-in-a-github-readme-md
#tree=$(tree -tf --noreport -I '*~' --charset ascii $1 |
#       sed -e 's/| \+/  /g' -e 's/[|`]-\+/ */g' -e 's:\(* \)\(\(.*/\)\([^/]\+\)\):\1[\4](\2):g')

#printf '## Problems  \n\n```  ' > tree.md
#tree >> tree.md
#echo '```  ' >> tree.md
md-file-tree > tree.md

cat code_journal.md tree.md > readme.md
