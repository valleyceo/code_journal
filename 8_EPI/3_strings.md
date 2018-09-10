# Strings

<details>
<summary> Is Palindromic </summary>

```cpp
bool IsPalindromic(const string& s) {
	for (int i = 0, j = size(s) - 1; i < j; ++i, ++j) {
		if (s[i] != s[j]) {
			return false;
		}
	}
	return true;
}
```
</details>


<details>
<summary> Int to String and String to Int </summary>

```cpp
string IntToString(int x) {
	bool is_negative = false;

	if (x < 0) {
		is_negative = true;
	}

	string s;

	do {
		s += '0' + abs(x % 10);
		x /= 10;
	} while (x);

	s += is_negative ? "-" : "";
	return {rbegin(s), rend(s)};
}

int StringToInt(const string& s) {
	return (sp[0] == '-' ? -1 : 1) * accumulate(begin(s) + (s[0] == '-'), end(s),
												0, [](int running_sum, char c) {
													return running_sum * 10 + c - '0';
												})
}
```
</details>


<details>
<summary> Base Conversion (need to review) </summary>

---
- Assume b1 <= 2, b2 <= 16
- pg. 88

---

```cpp
string ConvertBase(cons string& num_as_string, int b1, int b2) {
	bool is_negative = num_as_string.front() == '-';

	int num_as_string = accumulate(begin(num_as_string) + is_negative, end(num_as_string), 0,
									[b1](int x, char c) { 
										return x * b1 + (isdigit(c) ? c - '0' : c - 'A' + 10);
									});
	return (is_negative ? "-" : "") + (num_as_int == 0 ? "0" : ConstructFromBase(num_as_int, b2));
}

string ConsructFromBase(int num_as_int, int base) {
	return num_as_int == 0 ? "" 
							: ConstructFromBase(num_as_int / base, base) + 
								(char)(num_as_int & base >= 10 
											? 'A' + num_as_int % base - 10
											: '0' + num_as_int % base);
}
```
</details>


<details>
<summary> Spreadsheet Column Encoding </summary>

---
- ex: "A" -> 1, "AA" -> 27, "ZZ" -> 702

---

```cpp
int SSDecodeColID(const string& col) {
	return accumulate(begin(col), end(col), 0, [](int result, char c) {
		return result * 26 + c - 'A' + 1;
	});
}
```

---
- time: O(n)
- "ZZ" = 26^2 + 26 = 702

---
</details>


<details>
<summary> Replace and Remove </summary>

```cpp
int ReplaceAndRemove(int size, char s[]) {
	int write_idx = 0, a_count = 0;

	for (int i = 0; i < size; ++i) {
		if (s[i] != 'b') {
			s[write_idx++] = s[i];
		}
		if (s[i] == 'a') {
			++a_count;
		}
	}

	int cur_idx = write_idx - 1;
	write_idx = write_idx + a_count - 1; 
	const int final_size = write_idx + 1; // total size (after adding "aa"s)

	while (cur_idx >= 0) {
		if (s[cur_idx] == 'a') {
			s[write_idx--] = 'd';
			s[write_idx--] = 'd';
		} else {
			s[write_idx--] = s[cur_idx];
		}
		--cur_idx;
	}

	return final_size;
}
```

---
- time: O(n)

---
</details>


<details>
<summary> Is Palindrome (more general) </summary>

```cpp
bool IsPalindrome(const string& s) {
	int i = 0, j = size(s) - 1;

	while (i < j) {
		while (!isalnum(s[i]) && i < j) {
			++i;
		}

		while (!isalnum(s[j]) && i < j) {
			--j;
		}

		if (tolower(s[i++]) != tolower(s[j--])) {
			return false;
		}
	}

	return true;
}
```

---
- time: O(n)

---
</details>


<details>
<summary> Reverse Words </summary>

---

---

```cpp

```

---

---
</details>