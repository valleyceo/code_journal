# C++ Cheatsheet
--
## Type conversion
```cpp
// char to int
int a = char - 'A'
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
umap[num1] = num2
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