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