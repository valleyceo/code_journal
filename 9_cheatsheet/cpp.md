# C++ Cheatsheet
--
## Type conversion
```cpp
// char to int
int a = char - 'A'

// string to int
stoi(s) // to int
stof(s) // to float
stold(s) // to long double
```

## Array
```cpp
// create matrix
vector<vector<int>> matrix(ROW, vector<int>(COL));

// resize vector
matrix.resize(ROW);
matrix[i].resize(COL);
```

## String manipulation
```cpp
reverse(s.begin(), s.end());
sort(s.begin(), s.end());

// split string into half
string cmd = "HELLO WORLD";
string arg;
string::size_type pos = cmd.find(' ');
if(cmd.npos != pos) {
    arg = cmd.substr(pos + 1);
    cmd = cmd.substr(0, pos);
}
//=> cmd:"HELLO", arg:"WORLD"
```

## Linked List
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

// create node
ListNode *odds = new ListNode(0);

```

## Hashing
```cpp
/*** unordered map ***/

unordered_map<int, int> umap;
// add n delete
umap[num1] = num2
umap.erase(num);
// search
if(umap.find(numx) == umap.end());
// look up
val = umap.at(numx)

// iterate and find
for (auto a : umap){
    if (a.second == count)...;
}
```

## Trees
```cpp

```

## Class
```cpp
// colon initialization (works like regular init with type removed)
TicTacToe(int n): b_size(n), rows(n, 0), cols(n, 0), diag1(0), diag2(0) {}


```