# link - 'https://jayprakash15-blog-analysis-web-app-web-app-mi96z5.streamlit.app/'
# Use "pip show package_name" to get version package to write in requirements.txt file OR
# open terminal in pycharm and run "pip freeze > requirements.txt"
# To run streamlit use this in terminal "streamlit run app.py"
import streamlit as st
import bs4
import requests
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from textblob import TextBlob


st.write("""

# Get extracted content and sentiment analysis of blog from it's link

""")

def user_input_features():
	st.header('Past Link ')
	url = st.text_input("Past Here the link and press enter and wait.")
	return url

URL = user_input_features()
if URL:
	headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
	page = requests.get(URL, headers=headers)

	html = page.text
	soup = bs4.BeautifulSoup(html,'html.parser')

	passage = ""
	for p in soup.find_all('p'):
		passage = passage + p.text + "\n"

	blog_text = passage

	# Create a TextBlob object
	blob = TextBlob(blog_text)

	# Calculate the polarity and subjectivity of the text
	Polarity_Score = blob.sentiment.polarity
	Subjectivity_Score = blob.sentiment.subjectivity
	Word_Count = len(blog_text)

	st.write("Polarity_Score : ",Polarity_Score)
	st.write("Subjectivity_Score : ",Subjectivity_Score)
	st.write("Word count of blog : ", Word_Count)

	# divide polarity score into three parts
	if Polarity_Score > 0.25:
		Sentiment = "Positive"
	elif Polarity_Score < 0.01:
		Sentiment = "Negative"
	else:
		Sentiment = "Neutral"

	st.write("Sentiment of blog is ", Sentiment)

	if Subjectivity_Score > 0.5:
		Subjectivity = "Subjective"
	else:
		Subjectivity = "Objective"

	st.write("Given Blog is ", Subjectivity)

	st.header('Extracted contain from blog is given below.')
	st.write(passage)


else:
	st.warning("Please enter a URL to proceed.")
