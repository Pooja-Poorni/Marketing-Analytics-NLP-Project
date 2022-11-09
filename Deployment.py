
########################### Importing Libraries ##############################

import pandas as pd                           # Data Manipulation
import re                                     # For Regular Expression  
from wordcloud import WordCloud, STOPWORDS    # For Nlp Wordcloud
import matplotlib.pyplot as plt               # For Data Visualization
import nltk                                   # For NLP Processing
import streamlit as st                        # Deployment Framework
from sklearn.feature_extraction.text import CountVectorizer    # Scientific kit learn - it is used for machine learning and statistical model

################ Theme #################

# Primary accent for interactive elements
primaryColor = '#F63366'

# Background color for the main content area
backgroundColor = '#0EF5D9'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#F0F2F6'

# Color used for almost all text
textColor = "#31333F"

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

# Title
st.title("TOP RATED APPLICATIONS IN GOOGLE PLAY STORE ")

# Subheader
st.subheader("A SIMPLE WAY TO PREDICT APPLICATIONS FEATURES AND FREQUENCY ")

GENRE = st.selectbox('CHOOSE GENRE:',('Shopping','Productivity','Communication','Education','Travel & Local','Tools','Action','Adventure',
                                      'Social','Entertainment','Music & Audio','Finance','Health & Fitness','Maps & Navigation','Lifestyle',
                                      'Food & Drink','Books & Reference','Dating','Medical','video Players & Editors','Business','Photography',
                                      'Art & Design','News & Magazines','Public','Parenting','Casual','Board','Puzzle','Sports','Arcade','Simulation',
                                      'Racing','Card','Music','Strategy','Word','Role Playing','Trivia','Casino','Loans','Personalization','Weather',
                                      'House & Home','Libraries & Demo','Google Cast','Events','Comics','Children','Auto & Vehicles','Beauty','Watch','Watch Face'))
           
TokenCategory = st.selectbox('SELECT Category', ('Description','Reviews'))
                           
NGRAM = st.selectbox('SELECT NGRAM',('1', '2', '3'))

# To load the toprating dataset
data = pd.read_csv(r"C:\Users\User\Documents\Project 2\Topapps.csv")

# Removing unwanted symbols incase if exists
genrechoice = data.genre.unique()
description = data["description"].loc[data["genre"] == GENRE]
ngram = data["description"].loc[data["genre"] == NGRAM]


if NGRAM == '1':
    # Joining all the reviews into single paragraph 
    string = " ".join(description)
    string = re.sub("[^A-Za-z" "]+", " ", string).lower()
    string = re.sub("[0-9" "]+"," ", string)
    
    # words that contained in the reviews
    reviews_words = string.split(" ")
    reviews_words = reviews_words[1:]
    
    # To remove stopwords in the data
    with open(r"C:\Users\User\Documents\Python Scripts\Text Mining\Datasets NLP\stopwords_en.txt", "r") as sw:
     stop_words = sw.read()  
    reviews_words = [w for w in reviews_words if not w in stop_words]
    
    # Using count vectoriser to view the frequency of unigrams
    vectorizer = CountVectorizer(ngram_range=(1, 1))
    bow = vectorizer.fit_transform(reviews_words)
    
    sum_words = bow.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)  
    
    # Convert the words_freq data into dataframe
    df = pd.DataFrame(words_freq[:100], columns = ['Features', 'No. of Frequency'])
    st.table (df)
    
    # Generating wordcloud
    words_dict = dict(words_freq)
    WC_height = 1000
    WC_width = 1500
    WC_max_words = 100
    wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)

    wordCloud.generate_from_frequencies(words_dict)
    plt.figure(4)
    plt.title('Most frequently occurring bigrams connected by same colour and font size')
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

elif NGRAM =='2':
    nltk.download('punkt')
    WNL = nltk.WordNetLemmatizer()
     
    # Joinining all the reviews into single paragraph 
    string = " ".join(description)
    
    # Lowercase the reviews
    text = string.lower()

    # Remove single quote early since it causes problems with the tokenizer.
    text = text.replace("'", "")

    tokens = nltk.word_tokenize(text)
    text1 = nltk.Text(tokens)

    # To remove punctuations in the given data 
    text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text1]

    # Create a set of stopwords
    stopwords_wc = set(STOPWORDS)
    
    # Create Customized stopwords(For adding more stopwords in the list format)
    with open(r"C:\Users\User\Documents\Python Scripts\Text Mining\Datasets NLP\stopwords_en.txt", "r") as sw:
     customised_words = sw.read()
    new_stopwords = stopwords_wc.union(customised_words)

    # Remove stop words
    text_content = [word for word in text_content if word not in new_stopwords]

    # Take only non-empty entries
    text_content = [s for s in text_content if len(s) != 0]

    # To remove inflectional endings only and to return the base or dictionary form of a word 
    text_content = [WNL.lemmatize(t) for t in text_content]
    
    # nltk_tokens = nltk.word_tokenize(text)  
    bigrams_list = list(nltk.bigrams(text_content))
    
    dict2 = [' '.join(tup) for tup in bigrams_list]

    # Using count vectoriser to view the frequency of bigrams
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    bow = vectorizer.fit_transform(dict2)
   
    sum_words = bow.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    # Convert the words_freq data into dataframe
    df = pd.DataFrame(words_freq[:100], columns = ['Features', 'No. of Frequency'])
    st.table (df)
    
   # Generating wordcloud
    words_dict = dict(words_freq)
    WC_height = 1000
    WC_width = 1500
    WC_max_words = 100
    wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)

    wordCloud.generate_from_frequencies(words_dict)
    plt.figure(4)
    plt.title('Most frequently occurring bigrams connected by same colour and font size')
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

else:
    NGRAM =='3'
    # Joinining all the reviews into single paragraph
    string = " ".join(description)
     
    # To Lowercase the string
    text = string.lower()

     # Remove single quote early since it causes problems with the tokenizer.
    text = text.replace("'", "")

    tokens = nltk.word_tokenize(text)
    text1 = nltk.Text(tokens)
     
    # To remove punctuation in the given data
    text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text1]

     # Create a set of stopwords
    stopwords_wc = set(STOPWORDS)
    
    # Create customized stopwords( For adding more stopwords in the list format)
    with open(r"C:\Users\User\Documents\Python Scripts\Text Mining\Datasets NLP\stopwords_en.txt", "r") as sw:
     customised_words = sw.read()
    new_stopwords = stopwords_wc.union(customised_words)

     # Remove stop words
    text_content = [word for word in text_content if word not in new_stopwords]

     # Take only non-empty entries
    text_content = [s for s in text_content if len(s) != 0]
    
     # To remove inflectional endings only and to return the base or dictionary form of a word 
    WNL = nltk.WordNetLemmatizer()
    text_content = [WNL.lemmatize(t) for t in text_content]

     # nltk_tokens = nltk.word_tokenize(text)  
    trigrams_list = list(nltk.trigrams(text_content))
    
    dict3 = [' '.join(tup) for tup in trigrams_list]

     # Using count vectoriser to view the frequency of trigrams
    vectorizer = CountVectorizer(ngram_range=(3, 3))
    bow = vectorizer.fit_transform(dict3)
   
    sum_words = bow.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse=True)
   
    # Convert the words_freq data into dataframe
    df = pd.DataFrame(words_freq[:100], columns = ['Features', 'No. of Frequency'])
    st.table (df)
    
    # Generating wordcloud
    words_dict = dict(words_freq)
    WC_height = 1000
    WC_width = 1500
    WC_max_words = 100
    wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width)

    wordCloud.generate_from_frequencies(words_dict)
    plt.figure(4)
    plt.title('Most frequently occurring bigrams connected by same colour and font size')
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


