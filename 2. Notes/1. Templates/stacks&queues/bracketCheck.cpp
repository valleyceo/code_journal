bool isWellFormed(const string& s) {
	stack<char> left_chars;
	const unordered_map<char, char> kLookup = {{'(', ')'}, {'{', '}'}, {'[', ']'}};

	for (int i = 0; i < size(s); ++i) {
		if (kLookup.count(s[i])) {
			left_chars.emplace(s[i]);
		} else {
			if (empty(left_chars) || kLookup.at(left_chars.top()) != s[i]) {
				return false;
			}
			left_chars.pop();
		}
	}
	return empty(left_chars);
}