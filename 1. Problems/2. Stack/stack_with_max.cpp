// Stack with max

class Stack {
public:
	bool Empty() const {
		return empty(element_);
	}

	int Max() const {
		if (Empty()) {/
			throw length_error("Max(): empty stack");
		}

		return cached_max_with_count_.top().max;
	}

	int Pop() {
		if (Empty()) {
			throw  length_error("Pop(): empty stack");
		}

		int pop_element = element_.top();
		element_.pop();
		const int current_max = cached_max_with_count_.top().max;
		if (pop_element == current_max) {
			int& max_frequency = cached_max_with_count_.top().count;
			--max_frequency;

			if (max_frequency == 0) {
				cached_max_with_count_.pop();
			}
		}

		return pop_element;
	}

	void Push(int x) {
		element_.emplace(x);
		if (empty(cached_max_with_count_)) {
			cached_max_with_count_.emplace(MaxWidthCount{x, 1});
		} else {
			const int current_max = cached_max_with_count_.top().max;
			if (x == current_max) {
				int& max_frequency = cached_max_with_count_.top().count;
				++max_frequency;
			} else if (x > current_max) {
				cached_max_with_count_.emplace(MaxWidthCount{x, 1});
			}
		}
	}

private:
	stack<int> element_;

	struct MaxWidthCount {
		int max, count;
	};

	stack<MaxWidthCount> cached_max_with_count_;
}
