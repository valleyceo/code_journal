// Word Count Engine

/*
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3). We ask this because in compiled languages such as C#, Java, C++, C etc., it’s not straightforward to create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.). The expected output will simply be an array of string arrays.

Constraints:

[time limit] 5000ms
[input] string document
[output] array.array.string

My Note:
- receive a string
- return list of all unique words and number of occurences
- descending order
- if two or more have same count, sorted according to string
- all english alphabet
- case insensitive
- should strip out punctuation
- use whitespaces to separate words

ex: "Practice makes perfect. you'll only
     get Perfect by practice. just practice!"
      
time complexity: O(3n) ~= O(n) // get words + assign to buckets + read from largest
space complexity: O(n)
*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>

using namespace std;

vector<vector<string>> wordCountEngine( const string& document ) 
{
  // your code goes here
  unordered_map<string, int> umap;
  vector<string> words;
  vector<vector<string>> res;
  string temp_word = "";
  int max_ct = 0;
  
  for (char a : document) {
    
    if (a == ' ') {
      umap[temp_word]++;
      words.push_back(temp_word);
      max_ct = max(max_ct, umap[temp_word]);
      temp_word = "";
    } else if (a >= 65 && a <= 90) {
      temp_word += (a + 32);
    } else if (a >= 97 && a <= 122) {
      temp_word += a;
    }
  }
  
  if (temp_word.length() > 0) {
    umap[temp_word]++;
    words.push_back(temp_word);
    max_ct = max(max_ct, umap[temp_word]);
  }
  
  // create a bucket
  vector< vector<string>> buckets (max_ct + 1, vector<string>());
  
  for (auto w : words) {
    if (umap.find(w) != umap.end()) {
      buckets[umap[w]].push_back(w);
      umap.erase(w);
    }
  }
  
  for (int i = max_ct; i >= 0; --i) {
    if (buckets[i].size() == 0 || buckets[i][0] == "")
      continue;
    
    for (auto b : buckets[i]) {
      vector<string> temp;
      temp.push_back(b);
      temp.push_back(to_string(i));
      res.push_back(temp);
    }
  }
  
  return res;
}

int main() {
  const string s1 = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!";
  
  const string s2 = "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. ";
    
  vector<vector<string>> x = wordCountEngine(s2);
  
  for (auto l : x) {
    cout << l[0] << " " << l[1] << endl;
  }
  
  return 0;
}