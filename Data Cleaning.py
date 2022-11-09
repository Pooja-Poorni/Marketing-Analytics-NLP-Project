################################ Importing libraries ###################################
import pandas as pd       # Data Manipulation
import dtale              # For Auto EDA Library
import seaborn as sns     # For Advanced Data Visualization 
# Load the dataset
appinfo = pd.read_csv(r"C:\Users\User\Documents\Project 2\Appinfo.csv")
appinfo.head()             # It gives first 5 rows of the data
appinfo.columns            # To get the column names
appinfo.info()             # It gives data information

# To Remove unwanted column in the  App Information dataset
appinfo.drop(['histogram','price','free','currency','sale','saleTime','originalPrice','saleText','inAppProductPrice','developer','developerId',
              'developerEmail','developerWebsite','developerAddress','privacyPolicy','genreId','icon','headerImage','screenshots','video','videoImage','contentRating',
              'contentRatingDescription','updated','version','appId','url','released','recentChangesHTML','descriptionHTML'],axis =1,inplace = True)
appinfo.head()

# Auto EDA Library for Preprocesing
# Dtale
report = dtale.show(appinfo)
report.open_browser()

# Manual Preprocessing
# To identitfy duplicate records in the data
duplicate = appinfo.duplicated()
sum(duplicate)           # There are 36 duplicate values 

# To remove duplicates in the dataset
appinfo = appinfo.drop_duplicates()

# To identify missing values in the dataset
# check for count of NA'sin each column
appinfo.isna().sum()         # There are some missing values 

# To remove 'NAN' values in the dataset
app_info = appinfo.dropna()
app_info.isna().sum()

# To remove unwanted symbols in the Rating(score) column
app_info["installs"] = app_info["installs"].str.replace("+","") 
app_info["installs"] = app_info["installs"].str.replace(",","")

# To convert the datatype into integer by using TypeCasting
app_info["installs"] = app_info["installs"].astype("int64")

# Exploratory Data Analysis (EDA)
app_info.describe()

# Data Visualization
# Checking outliers by using boxplot
sns.boxplot(data = app_info)          # Some outliers are present in this dataset

# To check the data is normally distributed or not by using histogram
sns.distplot(app_info.installs)           # It is Positively skewed
sns.distplot(app_info.score)              # It is Negatively skewed
sns.distplot(app_info.ratings)            # It is Positively skewed
sns.distplot(app_info.reviews)            # It is Positively skewed
sns.distplot(app_info.minInstalls)        # It is Positively skewed
sns.distplot(app_info.realInstalls)       # It is Positively skewed

# To find the toprating apps based on ratings and installs
# To filter the records which have < 4.0 ratings and <100000
toprating = app_info.copy()
toprating = toprating.loc[toprating["score"] >= 4.0]
toprating = toprating.loc[toprating["installs"] >=100000]
toprating.to_csv("Topapps.csv", index=None, header=True)


