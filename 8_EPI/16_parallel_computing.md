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