# Imports

# Web Scraping Imports
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import argparse
# Machine Learning Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Create argument for reading an url
ap = argparse.ArgumentParser()
ap.add_argument('-u', '--url', required=True, help="URL Path")
args = vars(ap.parse_args())
my_url = args['url']

print("\nAnalyzing... Please wait..\n")

# Read data
data_frame = pd.read_csv('#insert the path to your dataset here')

# Shape and head
data_frame.shape
data_frame.head()

# Get the labels
labels = data_frame.label
labels.head()


#best = 0
#for _ in range(100):

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data_frame['text'], labels, test_size=0.2, random_state=7)

# Initialize the TdidfVectorizer (responsible for transforming the words into a vector representation)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit and transform the train set; transform the test set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

# Initialize the Classifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

# Predicting on the thest set and calculating accuracy
# In the future i'm going to get the best model, save it and just load it the next time the script run 
#y_pred = pac.predict(tfidf_test)
#score = accuracy_score(y_test, y_pred)
#accuracy = round(score*100,2)
#print(f'Accuracy: {accuracy}%')
    #if accuracy > best:
        #best = accuracy
    

#print("Best: ", accuracy)


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

main_container = page_soup.findAll("div", {"class": "story-body__inner"})

p_tags = main_container[0].findAll("p")

news_text = ""

for p_tag in p_tags:
    news_text += p_tag.text
    

np_array = np.array([news_text])
new_series = pd.Series(np_array)
tfidf_test = tfidf_vectorizer.transform(new_series)
y_pred = pac.predict(tfidf_test)

if y_pred[0] == 'REAL':
    print("This is a real news!")
else:
    print("This is a fake news!")
