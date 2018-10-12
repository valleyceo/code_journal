# Hash Tables

## Concept


<details>
<summary> What is a Hash Table? </summary>
- A data structure used to store keys (optionally corresponding values)

</details>


<details>
<summary> Hash table time complexity </summary>
- Well spread objects: O(1)
- Else on average: lookup, insertion, and deletion: O(1 + n/m)
	- n/m is the load where n is the number of objects and m is the length of array
- Rehashing: O(n + m)
</details>


<details>
<summary> Hashing a String </summary>

```cpp
int StringHash(const string& s, int modulus) {
	const int kMult = 997;
	return accumulate(begin(s), end(s), 0, [kMult, modulus](int val, char c) {
		return (val * kMult + c) % modulus;
	});
}
```
</details>


<details>
<summary> Find Anagrams </summary>

```cpp
vector<vector<string>> FindAnagrams(const vector<string>& dictionary) {
	unordered_map<string, vector<string>> sorted_string_to_anagrams;

	for (const string& s: dictionary) {
		string sorted_str(s);
		sort(begin(sorted_str), end(sorted_str));
		sorted_string_to_anagrams[sorted_str].emplace_back(s);
	}

	vector<vector<string>> anagram_groups;
	for (const auto& [key, group] : sorted_string_to_anagrams) {
		if (size(group) >= 2) {
			anagram_groups.emplace_back(group);
		}
	}

	return anagram_groups;
}
```

---
- Time complexity: 
	- O(nmlogm) sorting -> O(nm) for insertion, O(logm) for sorting each

---
</details>


<details>
<summary> Design of a Hashtable Class (need to review) </summary>

---
- assume each contact is a string
- it's possible that the list contains duplicates
- multiplicity is not important (three repetition is same as single instance)
---

```cpp
struct ContactList {
	bool operator==(const ContactList& that) const {
		return unordered_set<string>(begin(names), end(names)) ==
			   unordered_set<string>(begin(that.names), end(that.names));
	}

	vector<string> names;
}

struct HashContactList {
	size_t operator()(const ContactList& contacts) const {
		size_t hash_code = 0;
		for (const string& name : unordered_set<string>(begin(contacts.names), end(contacts.names))) {
			hash_code ^= hash<string>()(name);
		}
		return hash_code;
	}
};

vector<ContactList> MergeContactLists(const vector<ContactList>& contacts) {
	unordered_set<ContactList, HashContactList> unique_contacts(begin(contacts), end(contacts));
	return {begin(unique_contacts), end(unique_contacts)};
}
```

</details>


<details>
<summary> Palindrome Permuations </summary>

---
- Given a string of letters
- Test if the string can be permuted to form a palindrome

- Example: "edified" -> "deified"

---

```cpp
bool CanFormPalindrome(const string% s) {
	unordered_set<char> chars_with_odd_frequency;

	for (char c : s) {
		if (chars_with_odd_frequency.count(c)) {
			chars_with_odd_frequency.erase(c);
		} else {
			chars_with_odd_frequency.insert(c);
		}
	}

	return size(chars_with_odd_frequency) <= 1; // note that even array can only have 2, 4, 6 odd frequency
}
```

---
- Time complexity: O(n)
- Space complexity: O(c), where c is the number of distinct characters

---
</details>


<details>
<summary> Is Anonymous Letter Constructive (Ransom Note) </summary>

```cpp
bool IsLetterConstructibleFromMagazine(const string& letter_text, const string& magazine_text) {
	unordered_map<char, int> char_frequency_for_letter;

	for (char c : letter_text) {
		++char_frequency_for_letter[c];
	}

	for (char c : magazine_text) {
		if (auto it = char_frequency_for_letter.find(c);
			it != cend(char_frequency_for_letter)) {
			--it->second;

			if (it->second == 0) {
				char_frequency_for_letter.erase(it);
				if (empty(char_frequency_for_letter)) {
					break;
				}
			}
		}
	}

	return empty(char_frequency_for_letter);
}
```

---
- Time complexity: O(m + n)

---
</details>


<details>
<summary> Implement An ISBN Cache (need to review) </summary>

---

---

```cpp
class LruCache {
public:
	LruCache(size_t capacity) {}
	explicit LruCache(int capacity) : capacity_(capacity) {}

	int Lookup(int isbn) {
		if (auto it = isbn_price_table_.find(isbn);
			it == end(isbn_price_table_)) {
			return -1;
		} else {
			int price = it->second.second;

			MoveToFront(isbn, it);
			return price;
		}
	}

	void Insert(int isbn, int price) {
		if (auto it = isbn_price_table_.find(isbn);
			it != end(isbn_price_table_)) {
			MoveToFront(isbn, it);
		} else {
			if (size(isbn_price_table_) == capacity_) {
				isbn_price_table_.erase(lru_queue_.back());
				lru_queue_.pop_back();
			}

			lru_queue_.emplace_front(isbn);
			isbn_price_table_[isbn] = {begin(lru_queue_), price};
		}
	}

	bool Erase(int isbn) {
		if (auto it = isbn_price_table_.find(isbn);
			it == end(isbn_price_table_)) {
			return false;
		} else {
			lru_queue_.erase(it->second.first);
			isbn_price_table_.erase(it);
			return true;
		}
	}

private:
	typedef unordered_map<int, pair<list<int>::iterator, int>> Table;

	void MoveToFront(int isbn, const Table::iterator& it) {
		lru_queue_.erase(it->second.first);
		lru_queue_.emplace_front(isbn);
		it->second.first = begin(lru_queue_);
	}

	int capacity_;
	Table isbn_price_table_;
	list<int> lru_queue_;
};
```

---
- Time complexity: O(1)

---
</details>


<details>
<summary> Compute the LCA, Optimizing for Close Ancestors </summary>

```cpp
BinaryTreeNode<int>* LCA(const unique_ptr<BinaryTreeNode<int>>& node0,
						 const unique_ptr<BinaryTreeNode<int>>& node1) {
	BinaryTreeNode<int>*iter0 = node0.get(), *iter1 = node1.get();
	unordered_set<const BinaryTreeNode<int>*> node_on_path_to_root;

	while (iter0 || iter1) {
		if (iter0) {
			if (nodes_on_path_to_root.emplace(iter0).second == false) {
				return iter0;
			}
			iter0 = iter0->parent;
		}

		if (iter1) {
			if (nodes_on_path_to_root.emplace(iter1).second == false) {
				return iter1;
			}
			iter1 = iter1->parent;
		}
	}

	throw invalid_argument("node0 and node1 are not in the same tree");
}
```

---
- Time complexity: O(h)
- Space complexity: O(1)

- Note: nodes_on_path_to_root.emplace(iter0) returns a value(first), and a bool(second)
	- value is the existing key value or the emplaced value if key does not exist.
	- bool denotes if insertion took place

---
</details>


<details>
<summary> Find the Nearest Repeated Entires in an Array </summary>

---
- Given an array of strings
- Find the closest two pair of strings that are the same
---

```cpp
int FindNearestRepetition(const vector<string>& paragraph) {
	unordered_map<string, int> word_to_latest_index;
	int nearest_repeated_distance = numeric_limit<int>::max();

	for (int i = 0; i < size(paragraph); ++i) {
		if (auto latest_equal_word = word_to_latest_index.find(paragraph[i]);
			latest_equal_word != end(word_to_latest_index)) {
			nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word->second);
		}
		word_to_latest_index[paragraph[i]] = i;
	}

	return nearest_repeated_distance != numeric_limit<int>::max() ? nearest_repeated_distance : -1;
}
```

---
- Time complexity: O(n)
- Space complexity: O(d), where d is the number of distint strings in array

---
</details>


<details>
<summary> Find the Smallest Subarray Coverin All Values </summary>

---
- Given array of strings and a set of strings
- Return the indices of starting and ending index of a shortest subarray that contains all strings in the set

---

```cpp
struct Subarray {
	int start, end;
};

Subarray FindSmallestSubarrayCoveringSet (const vector<string>& paragraph,
										  const unordered_set<string> &keywords) {
	unordered_map<string, int> keywords_to_cover;

	for (const string &keyword : keywords) {
		++keywords_to_cover[keyword];
	}

	Subarray result = Subarray{-1, -1};
	int remaining_to_cover = size(keywords);
	for (int left = 0, right = 0; right < size(paragraph); ++right) {
		if (keywords.count(paragraph[right]) &&
			--keywords_to_cover[paragraph[right]] >= 0) {
			--remaining_to_cover;
		}

		while (remaining_to_cover == 0) {
			if ((result.start == -1 && result.end == -1) ||
				right - left < result.end - result.start) {
				result = {left, right};
			}

			if (keywords.count(paragraph[left]) &&
				++keywords_to_cover[paragraph[left]] > 0) {
				++remaining_to_cover;
			}
			++left;
		}
	}
	
	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(n)

1. Create hashtable of the keywords (with counter)
2. For every word iteration, if it exist in the keyword
3. If counter is zero, move the left idx and add the next keyword
4. Repeat from 2

---
</details>


<details>
<summary> Find the Smallest Subarray Coverin All Values (Improved) (need to review) </summary>

```cpp
Subarray FindSmallestSubarrayCoveringSubset (vector<string>::const_iterator paragraph_begin,
											 const vector<string>::const_iterator paragraph_end,
											 const vector<string>& keywords) {
	list<int> loc;
	unordered_map<string, list<int>::iterator> dict;
	for (const string& s : keywords) {
		dict.emplace(s, end(loc));
	}

	Subarray result = Subarray{-1, -1};
	int idx = 0;
	while (paragraph_begin != paragraph_end) {
		string s = *paragraph_begin++;
		if (auto it = dict.find(s); it != end(dict)) {
			if (it->second != end(loc)) {
				loc.erase(it->second);
			}

			loc.emplace_back(idx);
			it->second = --end(loc);

			if (size(loc) == size(keywords)) {
				if ((result.start == -1 && result.end == -1) ||
					idx - loc.front() < result.end - result.start) {
					result = {loc.front(), idx};
				}
			}
		}
		++idx;
	}

	return result;
}
```

</details>


<details>
<summary> Find Smallest Subarray Sequentially Covering All Values (Need to review) </summary>

---
- Time complexity: O(n)
- Space complexity: O(n)

---

```cpp
struct Subarray {
	int start, end;
};

Subarray FindSmallestSequentiallyCoveringSubset(
	const vector<string>& paragraph, const vector<string>& keywords) {
	unordered_map<string, int> keyword_to_idx;

	for (int i = 0; i < size(keywords); ++i) {
		keyword_to_idx.emplace(keywords[i], i);
	}

	vector<inst> latest_occurence(size(keywords), -1);

	vector<int> shortest_subarray_length(size(keywords),
										 numeric_limits<int>::max());

	int shortest_distance = numeric_limits<int>::max();

	subarray result = Subarray{-1, -1};

	for (int i = 0; i < size(paragraph); ++i) {
		if (keyword_to_idx.count(paragraph[i])) {
			int keyword_idx  = keyword_to_idx.find(paragraph[i])->second;

			if (keyword_idx == -) {
				shortest_subarray_length[keyword_idx] = 1;
			} else if (shortest_subarray_length[keyword_idx - 1] !=
					   numeric_limits<int>::max()) {
				int distance_to_previous_keyword = i - latest_occurence[keyword_idx - 1];
				shortest_subarray_length[keyword_idx] = distance_to_previous_keyword + 
														shortest_subarray_length[keyword_idx - 1];
			}
			latest_occurence[keyword_idx] = i;

			if (keyword_idx == size(keywords) - 1 &&
				shortest_subarray_length.back() < shortest_distance) {
				shortest_distance = shortest_subarray_length.back();
				result = {i - shortest_subarray_length.back() + 1, i};
			}
		}
	}

	return result;
}
```

---
- Time complexity: O(n)
- Space complexity: O(m)

---
</details>


<details>
<summary> Find The Longest Subarray With Distinct Entries </summary>

---
- Given an array
- Return the length of longest subarray where all its elements are distinct

- Ex: < f,s,f,e,t,w,e,n,w,e > -> < s,f,e,t,w, >
---

```cpp
int LongestSubarrayWithDistinctEntries(const vector<int>& A) {
	unordered_map<int, size_t> most_recent_occurence;
	size_t longest_dup_free_subarray_start_idx = 0, result = 0;

	for (size_t i = 0; i < size(A); ++i) {
		// inserted_entry = <A[i], i>, inserted_happen = true if inserted, else false
		const auto& [inserted_entry, inserted_happen] = most_recent_occurence.emplace(A[i], i);

		// check duplicate
		if (!inserted_happen) {
			if (inserted_entry->second >= longest_dup_free_subarray_start_idx) {
				result = max(result, i - longest_dup_free_subarray_start_idx);
				longest_dup_free_subarray_start_idx = inserted_entry->second + 1;
			}
			inserted_entry->second = i;
		}
	}

	// add last index
	return max(result, size(A) - longest_dup_free_subarray_start_idx);
}
```

---
- Time complexity: O(n)

---
</details>


<details>
<summary> Find The Length of a Longest Contained Interval </summary>

---
- Given an array
- Return the size of a largest subset of integers in the array

- Ex: < 3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8 >
- output: < -2, -1, 0, 1, 2, 3 > -> 6

---

```cpp
int LongestContainedRange(const vector<int>& A) {
	unordered_set<int> unprocessed_entries(begin(A), end(A));

	int max_interval_size = 0;
	while (!empty(unprocessed_entries)) {
		int a = *begin(unprocessed_entries);
		unprocessed_entries.erase(a);

		int lower_bound = a - 1;
		while (unprocessed_entries.count(lower_bound)) {
			unprocessed_entries.erase(lower_bound);
			--lower_bound;
		}

		int upper_bound = a + 1;
		while (unprocessed_entries.count(upper_bound) {
			unprocessed_entries.erase(upper_bound);
			++upper_bound;
		}

		max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1);
	}

	return max_interval_size;
}
```

---
- Time complexity: O(n)
- Space complexity: O(n)

---
</details>


<details>
<summary> Compute All String Decompositions (need to review) </summary>

---
- Given a input string and array of strings
- Return the starting indices of substrings of the sentence

---

```cpp
vector<int> FindAllSubstrings(const string& s, const vector<string>& words) {
	unordered_map<string, int> word_to_freq;
	for (const string& word : words) {
		++word_to_freq[word];
	}

	int unit_size = size(words.front());
	vector<int> result;

	for (int i = 0; i + unit_size * size(words) <= size(s); ++i) {
		if (MatchAllWordsInDict(s, word_to_freq, i, size(words), unit_size)) {
			result.emplace_back(i);
		}
	}

	return result;
}

bool MatchAllWordsInDict(const string& s,
						 const unordered_map<string, int>& word_to_freq,
						 int start, int num_words, int unit_size) {
	
	unordered_map<string, int> curr_string_to_freq;
	for (int i = 0; i < num_words; ++i) {
		string curr_word = s.substr(start + i * unit_size, unit_size);

		if (auto iter = word_to_freq.find(curr_word); iter == end(word_to_freq)) {
			return false;
		} else {
			++curr_string_to_freq[curr_word];
			if (curr_string_to_freq[curr_word] > iter->second) {
				// occurs too many times for match to be possible
				return false;
			}
		}
	}

	return true;
}
```

---
- Time complexity: O(Nnm)

---

</details>


<details>
<summary> Test The Collatz Conjecture </summary>

---
- Test if Collatz conjecture (currently neither proved nor disproved) is true by checking range of values

---

```cpp
bool TestCollatzConjecture(int n) {
	unordered_set<long> verified_numbers;

	for (int i = 3; i <= n; i += 2) {
		unordered_set<long> sequence;
		long test_i = i;

		while (test_i >= i) {
			if (!sequence.emplace(test_i).second) {
				return false;
			}

			if (test_i % 2) {
				if (!verified_numbers.emplace(test_i).second) {
					break;
				}
				long next_test_i = 3 * test_i + 1;
				if (next_test_i <= test_i) {
					throw overflow_error("Collatz sequence overflow for " + to_string(i));
				}
				test_i = next_test_i;
			} else {
				test_i /= 2;
			}
		}
	}

	return true;
}
```

</details>