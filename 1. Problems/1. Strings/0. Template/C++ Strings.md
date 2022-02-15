# Strings


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

```cpp
// Assume b1 <= 2, b2 <= 16

string ConvertBase(cons string& num_as_string, int b1, int b2) {
	bool is_negative = num_as_string.front() == '-';

	int num_as_string = accumulate(begin(num_as_string) + is_negative, end(num_as_string), 0,
									[b1](int x, char c) {
										return x * b1 + (isdigit(c) ? c - '0' : c - 'A' + 10);
									});
	return (is_negative ? "-" : "") + (num_as_int == 0 ? "0" : ConstructFromBase(num_as_int, b2));
}

string ConsructFromBase(int num_as_int, int base) {
	return num_as_int == 0 ? "" :
											ConstructFromBase(num_as_int / base, base) +
											(char)(num_as_int & base >= 10
											? 'A' + num_as_int % base - 10
											: '0' + num_as_int % base);
}

```
</details>

<details>
<summary> Spreadsheet Column Encoding </summary>

```cpp
// ex: "A" -> 1, "AA" -> 27, "ZZ" -> 702
int SSDecodeColID(const string& col) {
	return accumulate(begin(col), end(col), 0, [](int result, char c) {
		return result * 26 + c - 'A' + 1;
	});
}
```

***
- time: O(n)
- "ZZ" = 26^2 + 26 = 702

***
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

***
- time: O(n)
***

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

***
- time: O(n)

***
</details>


<details>
<summary> Reverse Words </summary>

***

***

```cpp
void ReverseWords(string* s) {
	reverse(begin(*s), end(*s));

	size_t start = 0, finish;

	while ((finish = s->find(" ", start)) != string::npos) {
		reverse(begin(*s) + start, begin(*s) + finish);
		start = finish + 1;
	}

	reverse(begin(*s) + start, end(*s));
}
```

***
- time: O(n), space: O(1)

***
</details>


<details>
<summary> Phone Mnemonic </summary>

***
- given a dial number, return all possible character sequences

***

```cpp
vector<string> PhoneMnemonic(const string& phone_number) {
	vector<string> mnemonics;

	PhoneMnemonicHelper(phone_number, 0,
						make_unique<string>(size(phone_number), 0).get(),
						&mnemonics);
	return mnemonics;
}

const int kNumTelDigits = 10;

const array<string, kNumTelDigits> kMapping = {
	{"0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"}};

void PhoneMnemonicHelper(const string& phone_number, int digit,
						 string* partial_mnemonic,
						 vector<string>* mnemonics) {
	if (digit == size(phone_number)) {
		mnemonics->emplace_back(*partial_mnemonic);
	} else {
		for (char c : kMapping[phone_number[digit] - '0']) {
			(*partial_mnemonic)[digit] = c;
			PhoneMnemonicHelper(phone_number, digit + 1, partial_mnemonic, mnemonics);
		}
	}
}
```

***
- time: O(4^n * n) - permutation takes O(4^n), base case takes O(n)

***
</details>


<details>
<summary> Look and Say Sequence </summary>

***
- <1, 11, 21, 1211, 111221, 312211, ...>

***

```cpp
string LookAndSay(int n) {
	string s = "1";
	for (int i = 1; i < n; ++i) {
		s = NextNumber(s);
	}

	return s;
}

string NextNumber(cont string& s) {
	string result;

	for (int i = 0; i < size(s); ++i) {
		int count = 1;

		while (i + 1 < size(s) && s[i] == s[i + 1]) {
			++i, ++count;
		}
		result += to_string(count) + s[i];
	}

	return result;
}
```

***
- time: O(2^n * n)
- explanation: if all numbers are different, string can double at max (2^n). Also, the iteration is run n times (n).

***
</details>


<details>
<summary> Roman to Decimal </summary>

```cpp
int RomanToInteger(const string& s) {
	unordered_map<char, int> T = {{'I', 1}, {'V', 5}, {'X', 10},
								  {'L', 50}, {'C', 100}, {'D', 500},
								  {'M', 1000}};

	int sum = T[s.back()];

	for (int i = s.length() - 2; i >= 0; --i) {
		if (T[s[i]] < T[s[i + 1]]) {
			sum -= T[s[i]];
		} else {
			sum += T[s[i]];
		}
	}

	return sum;
}
```

***
- time: O(n)
- for decimal to roman, simply create chart for {1,2,... 9}, {10, 20, ... 90}, ...
- upper bound should exist (4 digits)

***
</details>


<details>
<summary> Get Valid IP Address </summary>

```cpp
vector<string> GetValidIpAddress(const string& s) {
	vector<string> result;

	for (size_t i = 1; i < 4 && i < size(s); ++i) {
		if (const string first = s.substr(0, i); IsValidPart(first)) {
			for (size_t j = 1; i + j < size(s) && j < 4; ++j) {
				const string second = s.substr(i, j);

				if (IsValidPart(second)) {
					for (size_t k = 1; i + j + k < size(s) && k < 4; ++k) {
						const string third = s.substr(i + j, + k),
									fourth = s.substr(i + j + k);

						if (IsValidPart(third) && IsValidPart(fourth)) {
							result.emplace_back(first + "." + second + "." + third + "." + fourth);
						}
					}
				}
			}
		}
	}

	return result;
}

bool IsValidPart(const string& s) {
	if (size(s) > 3) {
		return false;
	}

	if (s.front() == '0' && size(s) > 1) {
		return false;
	}

	int val = stoi(s);
	return val <= 255 && val >= 0;
}
```

***
- time: O(1) - total number of IP addresses is 2^23

***
</details>


<details>
<summary> Sinusoidal String </summary>

***
- ex input: "HELLO_WORLD!"
 e   _   L
H L O W R D
   L   O   !

- output: "E_LHLOWRDLO!"

***

```cpp
string SnakeString(const string& s) {
	string result;

	for (int i = 1; i < size(s); i += 4) {
		result += s[i];
	}

	for (int i = 0; i < size(s); i += 2) {
		result += s[i];
	}

	for (int i = 3; i < size(s); i += 4) {
		result += s[i];
	}

	return result;
}
```

***
- time: O(n)

***
</details>


<details>
<summary> Run Length Encoding </summary>

***
- encode ex: "aaaabcccaa" -> "4a1b3c2a"
- decode ex: "3e4f2e" -> "eeeffffee"

***

```cpp
string Decoding(const string &s) {
	int count = 0;
	string result;

	for (const char &c : s) {
		if (isdigit(c)) {
			count = count * 10 + c - '0';
		} else {
			result.append(count, c);
			count = 0;
		}
	}

	result;
}

string Encoding(const string &s) {
	string result;

	for (int i = 1, count = 1; i <= size(s); ++i) {
		if (i == size(s) || s[i] != s[i-1]) {
			result += to_string(count) + s[i - 1];
		} else {
			++count;
		}
	}

	return result;
}
```

***
- time: O(n)

***
</details>


<details>
<summary> First Occurence of a substring </summary>

***
- note: there are three linear time string matching algorithm
	a. KMP
	b. Boyer-Moore
	c. Rabin-Karp

***

```cpp
int RabinKarp(const string &t, const string &s) {
	if (size(s) > size(t)) {
		return -1;
	}

	const int kBase = 26;
	int t_hash = 0, s_hash = 0;
	int power_s = 1;

	for (int i = 0; i < size(s); ++i) {
		power_s = i ? power_s * kBase : 1; // find the power of last letter
		t_hash = t_hash * kBase + t[i];
		s_hash = s_hash * kBase + s[i];
	}

	for (int i = size(s); i < size(t); ++i) {
		// check if hash is equal, and double check the same hash in case of collision
		if (t_hash == s_hash && !t.compare(i - size(s), size(s), s)) {
			return i - size(s);
		}

		t_hash -= t[i - size(s)] * power_s;
		t_hash = t_hash * kBase + t[i];
	}

	if (t_hash == s_hash && t.compare(size(t) - size(s), size(s), s) == 0) {
		return size(t) - size(s);
	}

	return -1;
}

```

***
- time: O(n)

***
</details>
