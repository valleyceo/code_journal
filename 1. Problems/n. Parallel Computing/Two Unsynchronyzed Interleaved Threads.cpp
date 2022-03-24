// Analyze two Unsynchronized Interleaved Threads

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
