#!/bin/bash

printf '## Problems  \n\n```  ' > tree.md
tree >> tree.md
echo '```  ' >> tree.md
cat code_journal.md tree.md > readme.md
rm tree.md