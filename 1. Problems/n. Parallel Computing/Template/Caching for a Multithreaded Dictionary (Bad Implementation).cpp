// Caching for a Multithreaded Dictionary

/*
- Given an input string
- Return an array of string in its dictionary that are the closest to input string

- Example: Part of online spell correction service
*/

// Bad Implementation
/*
- Critique: It has race condition (with multiple client request, cache gets messed up while processing and return wrong output)
*/
class SpellCheckService {
public:
	static void Service(ServiceRequest& req, ServiceResponse& resp) {
		if (string w = req.ExtractWordToCheckFromRequest(); w != w_last_) {
			w_last_ = move(w);
			closest_to_last_word_ = ClosestInDictionary(w_last_);
		}

		resp.EncodeIntoResponse(closest_to_last_word_);
	}

private:
	static string w_last_;
	static vector<string> closest_to_last_word_;
};

// Good Implementation
/*
- std::lock_quard(mx: mutex wrapper that owns the mutex for duration of a scoped block)
*/
class SpellCheckService {
public:
	static void Service(ServiceRequest& req, ServiceResponse& resp) {
		string w = req.ExtractWordToCheckFromRequest();
		vector<string> result;
		bool found = false;
		{
			lock_guard<mutex> lock(mx);
			if (w == w_last_) {
				result = closest_to_last_word_;
				found = true;
			}
		}

		if (!found) {
		result = ClosestInDictionary(w);
		lock_guard<mutex> lock(mx);
		w_last_ = move(w);
		closest_to_last_word_ = result;
		}
		resp.EncodeIntoResponse(result);
	}

private:
	static string w_last_;
	static vector<string> closest_to_last_word_;
	static mutex mx;
}
