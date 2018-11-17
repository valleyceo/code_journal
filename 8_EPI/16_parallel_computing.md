# Parallel Computing

<details>
<summary> Concept </summary>

#### Benefits:
- High performance
- Better use of resources
- Fairness
- Convenience
- Fault tolerance

#### Challenges
- Starvation: Processor never gets the resource it needs
- Deadlock: Two threads tries to acquire other, thus cannot be completed
- Livelock: Processor keeps retrying an operation that always fails

#### Concepts

##### Semaphore
- Synchronization construct, maintains a set of permits
- Usage: 
	- .acquire(): Waits till permit is available then takes it
	- .release(): adds the permit and notifies threads waiting on that semaphore


```cpp
class Semaphore {
public:
	Semaphore(int max_available) : max_available_(max_available), taken_(0) {}

	void Acquire() {
		unique_lock<mutex> lock(mx_);
		while (taken_ == max_available_) {
			cond_.wait(lock);
		}
		++taken_;
	}

	void Release() {
		lock_guard<mutex> lock(mx_);
		--taken_;
		cond_.notify_all();
	}

private:
	int max_available_;
	int taken_;
	mutex mx_;
	condition_variable cond_;
};
```

</details>


<details>
<summary> Implement Caching for a Multithreded Dictionary (Bad implementation) </summary>

---
- Given an input string
- Return an array of string in its dictionary that are the closest to input string

- part of online spell correction service
---

```cpp
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

```

---
- Critique: It has race condition (with multiple client request, cache gets messed up while processing and return wrong output)

---
</details>


<details>
<summary> Implement Caching for a Multithreded Dictionary (Good implementation) </summary>

---

---

```cpp
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

```

---
- std::lock_quard(mx: mutex wrapper that owns the mutex for duration of a scoped block)

---
</details>


<details>
<summary> Analyze two Unsynchronized Interleaved Threads </summary>

---

---

```cpp
static int counter = 0;

void IncrementThread(int N) {
	for (int i = 0; i < N; ++i) {
		++counter;
	}
}

void TwoThreadIncrementDriver(int N) {
	thread T1(IncrementThread, N);
	thread T2(IncrementThread, N);
	T1.join();
	T2.join();

	cout << counter << endl;
}
```

---

---
</details>


<details>
<summary> Implement Synchronization for Two INterleaving Threads </summary>

---

---

```cpp
class OddEvenMonitor {
public:
	static const bool ODD_TURN = true;
	static const bool EVEN_TURN = false;

	OddEvenMonitor() : turn_(ODD_TURN) {}

	void WaitTurn(bool old_turn) {
		unique_lock<mutex> lock(mx_);
		while (turn_ != old_turn) {
			cond_.wait(lock);
		}
	}

	void ToggleTurn() {
		lock_guard<mutex> lock(mx_);
		turn_ = !turn_;
		cond_.notify_one();
	}

private:
	bool turn_;
	condition_variable cond_;
	mutex mx_;
};

void OddThread(OddEvenMonitor& monitor) {
	for (int i = 1; i <= 100; i += 2) {
		monitor.WaitTurn(OddEvenMonitor::ODD_TURN);
		cout << i << endl;
		monitor.ToggleTurn();
	}
}

void EvenThread(OddEvenMonitor& monitor) {
	for (int i = 2; i <= 100; i += 2) {
		monitor.WaitTurn(OddEvenMonitor::EVEN_TURN);
		cout << i << endl;
		monitor.ToggleTurn();
	}
}
```

---

---
</details>


<details>
<summary> Implement a Thread Pool</summary>

---

---

```cpp
// Part of HTTP server
const unsigned short SEEREVERPORT = 8080;

int main(int argc, char* argv[]) {
	asio::io_service io_service;
	tcp::acceptor acceptor(io_service, tcp::endpoint(tcp::v4(), SERVERPORT));

	while (true) {
		tcp::socket sock(io_service);
		acceptor.accept(sock);
		ProcessReq(sock);
	}

	return 0;
}

// First solution (launch a new thread per request)
int main(int argc, char* argv[]) {
	asio::io_service io_service;
	tcp::acceptor acceptor(io_service, tcp::endpoint(tcp::v4(), SERVERPORT));

	while (true) {
		shared_ptr<tcp::socket> sock(new tcp::socket(io_service));
		acceptor.accept(*sock);
		thread(ProcessReq, sock).detach();
	}

	return 0;
}

// ussing Boost's sync_bounded_queue
void ThreadFunc(QueueType& q) {
	while (true) {
		unique_ptr<tcp::socket> sock;
		q >> sock;
		ProcessReq(sock);
	}
}

const unsigned short kServerPort = 8080;
const int kNThreads = 2;

int main(int argc, char* argv[]) {
	QueueType q(kNThreads);

	for (int i = 0; i < kNThreads; ++i) {
		thread(ThreadFunc, ref(q)).detach();
	}

	asio::io_service io_service;
	tcp::acceptor acceptor(io_service, tcp::endpoint(tcp::v4(), kSErverPort));

	while (true) {
		unique_ptr<tcp::socket> sock(new tcp::socket(io_service));
		acceptor.accept(*sock);
		q << move(sock);
	}

	return 0;
}

```

---

---
</details>