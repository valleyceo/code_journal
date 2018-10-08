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