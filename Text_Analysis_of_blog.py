import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
import string

file = open("blog_text.txt", "r")
if file.mode == "r":
	blog_text = file.read()
file.close()

# print(blog_text)
# print(type(blog_text))
# print(blog_text.split())

## Cleaning Data ###
# Convert text to lowercase
text = blog_text.lower()

# Create a TextBlob object from the lowercase text
blob = TextBlob(text)

# Remove stop words and punctuation marks from the TextBlob object
cleaned_blob = [word for word in blob.words if word not in string.punctuation and word.lower() not in stopwords.words('english')]

# Join the cleaned words back into a string
cleaned_blog_text = " ".join(cleaned_blob)

# Analyze the sentiment of the cleaned text using TextBlob
sentiment = TextBlob(cleaned_blog_text).sentiment

# Print the cleaned text and sentiment analysis results
#print("Cleaned Text:", cleaned_blog_text)
print("Sentiment Analysis:", sentiment)


# Create a TextBlob object
#blob = TextBlob(blog_text)
blob = TextBlob(cleaned_blog_text)

# Calculate the polarity and subjectivity of the text
Polarity_Score = blob.sentiment.polarity
Subjectivity_Score = blob.sentiment.subjectivity

print("Polarity_Score : ",Polarity_Score)
print("Subjectivity_Score : ",Subjectivity_Score)

# Before Cleaning
Word_Count = len(blog_text)
print("Word count of blog : ", Word_Count)
# print("Word count before cleaning : ", Word_Count)

## After Cleaning
# Word_Count_Cleaned = len(cleaned_blog_text)
# print("Word count after cleaning : ", Word_Count)

# divide polarity score into three parts
if Polarity_Score > 0.2:
	Sentiment = "Positive"
elif Polarity_Score < -0.2:
	Sentiment = "Negative"
else:
	Sentiment = "Neutral"
print("Sentiment of blog is ", Sentiment)

if Subjectivity_Score > 0.5:
	print("Given blog is ","Subjective")
else:
	print("Given blog is ","Objective")




