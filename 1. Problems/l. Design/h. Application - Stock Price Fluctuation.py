# LC 2034. Stock Price Fluctuation

'''
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.
'''

# Solution 1 using Dict and Heap
class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.latest_time = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        # Simply append updated time/price to heap, original time/price will be ignored later
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.max_heap)

        # Find largest (price, timestamp) that matches in timestamps dictionary
        while -price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.max_heap)

        heapq.heappush(self.max_heap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_heap)

        # Find the smallest (price, timestamp) that matches in timestamps dictionary
        while price != self.timestamps[timestamp]:
            price, timestamp = heapq.heappop(self.min_heap)

        heapq.heappush(self.min_heap, (price, timestamp))
        return price

# Solution 2 using SortedDict
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        self.timestamps = SortedDict()
        self.prices = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamps:
            prev_price = self.timestamps[timestamp]
            self.prices[prev_price].remove(timestamp)

            if len(self.prices[prev_price]) == 0:
                del self.prices[prev_price]

        if price not in self.prices:
            self.prices[price] = set()

        self.prices[price].add(timestamp)
        self.timestamps[timestamp] = price
                
    def current(self) -> int:
        return self.timestamps.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.prices.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.prices.peekitem(0)[0]
