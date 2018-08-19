// Decrypt Message

/*
An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.

Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q
The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

Explain your solution and analyze its time and space complexities.

Examples:

input:  word = "dnotq"
output: "crime"

input:  word = "flgxswdliefy"
output: "encyclopedia"
Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space. Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.

Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa. You may search the internet for the appropriate method.

Constraints:

[time limit] 5000ms

[input] string word

The ASCII value of every char is in the range of lowercase letters a-z.
[output] string
*/

// my solution
#include <iostream>
#include <string>

using namespace std;

string decrypt( const string& word ) 
{
  if (word.length() == 0)
    return "";
  
  string res = "";
  
  for (int i = word.length()-1; i > 0; i--) {
    int diff = word[i] - word[i-1];
    while (diff < 'a')
      diff += 26;
    
    res = (char)diff + res;
  }
  
  //if the character a
  if (word[0] - 1 < 0)
    res = (char)(word[0] - 1 + 26) + res;
  else
    res = (char)(word[0] - 1) + res;
  
  return res;
}

int main() {
  cout << decrypt("dnotq");
  return 0;
}

/* Note
- ASCII characters
- add 1 to first letter, add value from previous letter afterwards
- subtract 26 from every letter (until in range a-z)
- convert values back to letters


example: "crime"
a-97
c-99
z-122

step 1: 99  114       105       109       101
step 2: 100 214       319       428       529
            
step 3: 100 110*26*n4 111*26*n3 116*26*n2 113*26*n
decrypt: 

d	n	o	t	q

q-t + 26 * n -> -3 + 26 * n = 101 -> e
t-o + 26 * n2
o-n + 26 * n3

time complexity: O(N)
space complexity: O(1)

113 -> 101

//original - [original - 1]
//add 26 until in range
*/


