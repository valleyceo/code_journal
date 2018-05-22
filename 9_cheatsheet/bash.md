# Bash cheatsheet

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