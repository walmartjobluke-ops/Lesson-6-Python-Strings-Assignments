#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
#reviews = ["This product is really good. I'm impressed with its quality.",
        #"The performance of this product is excellent. Highly recommended!",
        #"I had a bad experience with this product. It didn't meet my expectations.",
        #"Poor quality product. Wouldn't recommend it to anyone.",
        #"The product was average. Nothing extraordinary about it."]
#So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    #positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    #negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
#Task 3: Review Summary

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]


keywords = ["good", "excellent", "bad", "Poor", "average"]

def highlight_keywords(review):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

print("=== Task 1: Keyword Highlighter ===")
for review in reviews:
    print(highlight_keywords(review))

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_sentiment(review):
    review_lower = review.lower()
    positive_count = sum(1 for word in positive_words if word in review_lower)
    negative_count = sum(1 for word in negative_words if word in review_lower)
    return positive_count, negative_count

print("\n=== Task 2: Sentiment Tally ===")
for review in reviews:
    pos, neg = tally_sentiment(review)
    print(f"Positive: {pos}, Negative: {neg} - {review[:50]}...")

def create_summary(review, char_limit=30):
    if len(review) <= char_limit:
        return review
    
    summary = review[:char_limit]
    last_space = summary.rfind(' ')
    
    if last_space > 0:
        summary = summary[:last_space]
    
    return summary + "…"

print("\n=== Task 3: Review Summary ===")
for review in reviews:
    print(create_summary(review))