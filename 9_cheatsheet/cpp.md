# C++ Cheatsheet
--
## Type conversion
```cpp
// char to int
int a = (int)ch;
```

## String manipulation
```cpp
reverse(s.begin(), s.end());
sort(s.begin(), s.end());
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

```
