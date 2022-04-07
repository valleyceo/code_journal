# LC 355. Design Twitter

'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
'''
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.feedLength = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        tweet_list = []
        feeds = []

        for tid in self.tweets.keys():
            if tid in self.following[userId] or tid == userId:
                tweet_list.append(self.tweets[tid].copy())

        for _ in range(self.feedLength):
            max_time = float('-inf')
            min_tweet = None

            for tlist in tweet_list:
                if tlist and tlist[0][0] > max_time:
                    max_time = tlist[0][0]
                    min_tweet = tlist

            if max_time == float('-inf'):
                break

            feeds.append(min_tweet[0][1])
            min_tweet.popleft()

        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
