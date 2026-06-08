class Twitter:

    def __init__(self):
        self.followeeMap = defaultdict(set)
        self.userTweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followeeMap[userId].add(userId)

        # if len(self.followeeMap[userId]) < 10:
        for followeeId in self.followeeMap[userId]:
            if followeeId in self.userTweetMap:
                lastTweetIndex = len(self.userTweetMap[followeeId]) - 1
                time, tweetId = self.userTweetMap[followeeId][lastTweetIndex]
                heapq.heappush(maxHeap, [-time, tweetId, followeeId, lastTweetIndex])

        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, lastTweetIndex = heapq.heappop(maxHeap)
            time = -time
            res.append(tweetId)

            if lastTweetIndex > 0:
                lastTweetIndex = lastTweetIndex - 1
                time, tweetId = self.userTweetMap[followeeId][lastTweetIndex]
                heapq.heappush(maxHeap, [-time, tweetId, followeeId, lastTweetIndex])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
