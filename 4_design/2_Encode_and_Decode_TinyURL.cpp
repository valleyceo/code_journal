// Encode and Decode TinyURL

/*
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
*/

// my solution
// https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100274/Pretty-clean-C++11-with-random-choices

class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        static const string chart =
            "0123456789"
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        static uniform_int_distribution<int> choice(0, chart.size() - 1);
        static const int hash_len = 6;

        string new_url(hash_len, ' ');
        
        // create new hash function
        auto gen_hash = [&, this] () {
            for (int i = 0; i < hash_len; ++i)
                new_url[i] = chart[choice(rand_eng)];
        };
        
        // create new hash (w/ collision check)
        gen_hash();
        while (urls.count(new_url))
            gen_hash();
        
        auto shortUrl = "http://tinyurl.com/" + new_url;
        urls[shortUrl] = longUrl;
        
        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return urls[shortUrl];
    }
    
    default_random_engine rand_eng;
    unordered_map<string, string> urls;
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));