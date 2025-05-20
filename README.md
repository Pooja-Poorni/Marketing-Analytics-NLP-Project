### Marketing Analytics: Competitor Analysis and App Performance Optimization

![image](https://github.com/user-attachments/assets/b9ae7d41-c54a-4d4e-a0c2-fffe82f08486)


In this project, to build an analytical pipeline to mine app features from Google Play Store data, aiming to assist developers in identifying the most requested and trending features across top-rated applications in various categories based on domain or keyword search. The extracted insights are used to guide development and optimize mobile app performance.

**Project Objective**

* Extract features from top-rated mobile apps based on category/keyword.

* Analyze user reviews to prioritize development features.

* Build an app architecture based on user-requested functionalities.

* Deploy insights using a Streamlit dashboard for feature visualization and selection.

**Project Goals**

* Assist mobile developers in identifying market-demanded features.

* Enhance app quality and success rate based on user-driven insights.

* Provide a Product Requirement Document (PRD)-style output using review mining.

* Optimize for scalability, cost-effectiveness, and feature-rich deployment.

**Methodology**

**Framework:** CRISP-ML(Q)

**Process:**

1. Data Collection via Web Scraping (Google Play Store)

2. Data Cleaning and Preprocessing

3. Exploratory Data Analysis (EDA)

4. Natural Language Processing (NLP) for Feature Extraction

5. Model Building using Bag-of-Words

6. Streamlit Deployment

**Tech Stack**

Tools / Libraries used:

* Language       - Python
* IDE	           - Spyder, Jupyter Notebook
* Libraries      -	NLTK, scikit-learn, pandas, matplotlib, seaborn, sweetviz, pandas-profiling, D-Tale
* NLP Techniques - 	Tokenization, Stopword Removal, Lemmatization, Stemming
* Deployment	   - Streamlit
* Data Source	   - Google Play Store via google-play-scraper

**Dataset Overview**

**Total Records:** 1,413 apps

**Categories:** 53

**Attributes:** 44 columns (e.g., App Title, Rating, Reviews, Description, Developer Info, etc.)

**Variable Types:**

* Numerical: 13

* Categorical: 30

**Date:** 1

**Issues Addressed:** Duplicates (36), Missing Values (152)

**EDA Insights**

* Auto EDA tools used: Sweetviz, Pandas-Profiling, D-Tale

* Distribution analysis, skewness, outliers via boxplots

* Feature engineering through review data analysis

**NLP Pipeline**

* Regular Expressions for cleaning

* Tokenization

* Stopword and punctuation removal

* Lemmatization and stemming

* Spell correction and whitespace cleanup

* N-gram feature extraction (1-gram, 2-gram, 3-gram)

**Model Overview**

* **Technique:** Bag-of-Words (via CountVectorizer)

* **Purpose:** Convert review text to feature vectors

* **Model Outputs:** Vocabulary extraction, feature prioritization

**Deployment**

* Interface: Streamlit Web App

* Inputs: Category selection or keyword search

* Outputs: Trending features, app comparisons, review sentiment indicators

**Challenges Faced**

* Handling inconsistent or erroneous review text

* Removing emojis and customizing stopwords

* Handling spelling errors and grammar inconsistencies

**Future Enhancements**

* Expand N-gram range dynamically

* Include real-time review extraction

* Extend to other platforms (iOS App Store)

* Integrate sentiment analysis or clustering of features
