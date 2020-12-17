CREATE TABLE "company" (
	"ticker_symbol"	TEXT,
	"company_name"	TEXT,
	PRIMARY KEY("ticker_symbol")
);

CREATE TABLE "company_tweet" (
	"tweet_id"	INTEGER,
	"ticker_symbol"	TEXT
);

CREATE TABLE "tweet" (
	"tweet_id"	INTEGER,
	"writer"	TEXT,
	"post_date"	INTEGER,
	"body"	TEXT,
	"comment_num"	INTEGER,
	"retweet_num"	INTEGER,
	"like_num"	INTEGER
);

/* Source data location
https://www.kaggle.com/omermetinn/tweets-about-the-top-companies-from-2015-to-2020
*/