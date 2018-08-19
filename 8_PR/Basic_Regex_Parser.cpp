// Basic Regex Parser

/*
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

[time limit] 5000ms
[input] string text
[input] string pattern
[output] boolean
*/

// my solution
#include <iostream>
#include <string>

using namespace std;

bool isMatch( const string &text, const string &pattern ) 
{
  // your code goes here
  if (text.length() == 0 && pattern.length() == 0)
    return true;
  
  if (text.length() == 0 && pattern.length() == 2 && pattern[1] == '*')
    return true;
  
  if (text.length() == 0 || pattern.length() == 0)
    return false;
  
  if (pattern[0] == '*') 
    return false;
  
  bool is_match = false;
  if (text[0] == pattern[0] || pattern[0] == '.')
    is_match = is_match || isMatch(text.substr(1), pattern.substr(1));
  
  int next_idx1, next_idx2;
  
  if (pattern[1] == '*') {
    is_match = is_match || isMatch(text, pattern.substr(2));
    
    if (text[0] == pattern[0] || pattern[0] == '.') {
      is_match = is_match || isMatch(text.substr(1), pattern.substr(2));
      is_match = is_match || isMatch(text.substr(1), pattern);
    }
  }
  
  return is_match;
}

int main() {
  cout << isMatch("bbbbbb", "b*b*b*") << endl;
  return 0;
}

/* NOTE:
- REGEX isMatch ('.', '*')

example:
text = "aa", pattern = "a"
-> false

text = "acd", pattern = "ab*c."
-> true

text = "acddd", pattern = "acd*ddd"

text = "acd", pattern = "*"
-> false


bool star_flag
for idx in text.length:
  text[idx] == pattern[idx]
  
  check pattern[idx+1] is star
    star_flag= true
    
    while pattern[idx+2] is the same character

*/