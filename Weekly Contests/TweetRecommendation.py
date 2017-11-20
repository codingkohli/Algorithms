# To recommend the tweets to the target user
# Complete the function below.
# followGraph_edges is a list of tuples (userId, userId)
# likeGraph_edges is also a list of tuples (userId, tweetId)
# psuedo Algo :
# 1. Take the target user and create a list of its followers
# 2. Traverse all the tweets and increment them to a hash using the list of followers
# 3. Return the list of tweets that cross a threshold

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    tweetList = []
    hashTweet = {}
    # getting the followers of target user
    for x,y in followGraph_edges :
        if x == targetUser :
            tweetList.append(y)
    # Getting the liked tweets
    for x,y in likeGraph_edges :
        if x in tweetList :
            try :
                hashTweet[y] += 1
            except :
                hashTweet[y] = 1

    #getting the tweets crossing a threshold
    return [tweet for tweet in hashTweet if hashTweet[tweet] >= minLikeThreshold]