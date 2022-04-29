// Implement a Thread Pool

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
