# Bash cheatsheet

# file manipulation

```bash  
# open file on screen
cat filename.txt

# scroll view mode (older version: more, most)
less filename.txt 

# search text file
grep search_word filename.txt

# search and word count
grep search_word file.txt | wc -l
```

# file stream

```bash  

# pure bash
i=0
while (( i++ < 10 ))
do
  read line
done < file.txt
echo $line

# other solutions
sed -n '10p' file.txt
awk 'NR == 10' file.txt

```

# environment

```bash  
# Contains username of the current logged-in account
$LOGNAME

# Shell prompt name
$PS1
PS1 = '$ '

# useful alias
alias ll='ls -la'
alias cl='curl -L'
alias ..='cd ..'
alias now='date + "%T'
```bash