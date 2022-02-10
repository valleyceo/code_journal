// Reverse string of word
/*
input: "Alice likes Bob"
output: "Bob likes Alice"
*/

// Time complexity: O(n), space complexity: O(1)
void ReverseWords(string* s) {
	reverse(begin(*s), end(*s));

	size_t start = 0, finish;

	while ((finish = s->find(" ", start)) != string::npos) {
		reverse(begin(*s) + start, begin(*s) + finish);
		start = finish + 1;
	}

	reverse(begin(*s) + start, end(*s));
}