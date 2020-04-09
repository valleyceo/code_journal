class Queue {
public:
	void Enqueue(int x) { data_.emplace_back(x); }

	int Dequeue() {
		if (empty(data_)) {
			throw length_error("empty queue");
		}

		const int val = data_.front();
		data_.pop_front();
		return val;
	}

	int Max() const {
		if (empty(data_)) {
			throw length_error("cannot perform Max() on empty queue");
		}

		return *max_element(begin(data_), end(data_));
	}

private:
	list<int> data_;
}