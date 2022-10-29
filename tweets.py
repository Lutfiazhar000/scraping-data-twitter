# import packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# query data from twitter 
query = input("enter your keyword: ")
tweets = []
limit = int(input("set limit: "))

# looping for every tweet
try:
    print("start Scraping...")
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=['full_date', 'user', 'tweet'])

except:
    print("scraping failed")

# display
print(df)
print('Finished')
print("--------")

# save dataframe as csv file
df.to_csv('tweets.csv', index=False)
