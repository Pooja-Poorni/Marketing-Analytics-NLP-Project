############################ Importing Libraries ##############################

import pandas as pd
from google_play_scraper import search, app
from tqdm import tqdm

# Extract the app details by using google_play_scraper
shop_app = search("Shopping apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
shop_df = pd.DataFrame(shop_app)


prod_app = search("Productivity apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
prod_df = pd.DataFrame(prod_app)


comm_app = search("Communication apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
comm_df = pd.DataFrame(comm_app)


edu_app = search("Education apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
edu_df = pd.DataFrame(edu_app)


travel_app = search("Travel & Local apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=150  # defaults to 30 (= Google's maximum)
)
travel_df = pd.DataFrame(travel_app)


tools_app = search("Tools apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
tools_df = pd.DataFrame(tools_app)


action_app = search("Action Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
action_df = pd.DataFrame(action_app)


adven_app = search("Adventure Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
adven_df = pd.DataFrame(adven_app)


social_app = search("Social apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
social_df = pd.DataFrame(social_app)


entern_app = search("Entertainment apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
entern_df = pd.DataFrame(entern_app)


music_app = search("Music & Audio apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
music_df = pd.DataFrame(music_app)


finance_app = search("Finance apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
finance_df = pd.DataFrame(finance_app)


health_app = search("Health & Fitness apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
health_df = pd.DataFrame(health_app)


maps_app = search("Maps & Navigation apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
maps_df = pd.DataFrame(maps_app)


lifestyle_app = search("Lifestyle apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
lifestyle_df = pd.DataFrame(lifestyle_app)


food_app = search("Food & Drink apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
food_df = pd.DataFrame(food_app)


books_app = search("Books & Reference apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
books_df = pd.DataFrame(books_app)


dating_app = search("Dating apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
dating_df = pd.DataFrame(dating_app)


medical_app = search("Medical apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
medical_df = pd.DataFrame(medical_app)


video_app = search("Video Players & Editors apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
video_df = pd.DataFrame(video_app)


business_app = search("Business apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
business_df = pd.DataFrame(business_app)

photo_app = search("Photography apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
photo_df = pd.DataFrame(photo_app)


art_app = search("Art & Design apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
art_df = pd.DataFrame(art_app)


news_app = search("News & Magazines apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
news_df = pd.DataFrame(news_app)


public_app = search("Public apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=100  # defaults to 30 (= Google's maximum)
)
public_df = pd.DataFrame(public_app)


parent_app = search("Parenting apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
parent_df = pd.DataFrame(parent_app)


casual_app = search("Casual Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
casual_df = pd.DataFrame(casual_app)


board_app = search("Board Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
board_df = pd.DataFrame(board_app)


puzzle_app = search("Puzzle Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
puzzle_df = pd.DataFrame(puzzle_app)


sports_app = search("Sports Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
sports_df = pd.DataFrame(sports_app)


arcade_app = search("Arcade Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
arcade_df = pd.DataFrame(arcade_app)


simmu_app = search("Simulation Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
simmu_df = pd.DataFrame(simmu_app)


racing_app = search("Racing Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
racing_df = pd.DataFrame(racing_app)


card_app = search("Card Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
card_df = pd.DataFrame(card_app)


mugame_app = search("Music Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
mugame_df = pd.DataFrame(mugame_app)


strategy_app = search("Strategy Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
strategy_df = pd.DataFrame(strategy_app)


word_app = search("Word Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
word_df = pd.DataFrame(word_app)


roleplay_app = search("Role Playing Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
roleplay_df = pd.DataFrame(roleplay_app)


trivia_app = search("Trivia Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
trivia_df = pd.DataFrame(trivia_app)


casino_app = search("Casino Game apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
casino_df = pd.DataFrame(casino_app)


loan_app = search("Loans apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
loan_df = pd.DataFrame(loan_app)


personal_app = search("Personalization apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
personal_df = pd.DataFrame(personal_app)


weather_app = search("Weather apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
weather_df = pd.DataFrame(weather_app)


house_app = search("House & Home apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
house_df = pd.DataFrame(house_app)


library_app = search("Libraries & Demo apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
library_df = pd.DataFrame(library_app)


google_app = search("Google Cast apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
google_df = pd.DataFrame(google_app)


event_app = search("Events apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
event_df = pd.DataFrame(event_app)


comics_app = search("Comics apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
comics_df = pd.DataFrame(comics_app)


children_app = search("Children apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
children_df = pd.DataFrame(children_app)


auto_app = search("Auto & Vehicles apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
auto_df = pd.DataFrame(auto_app)


beauty_app = search("Beauty apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
beauty_df = pd.DataFrame(beauty_app)


watch_app = search("Watch apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
watch_df = pd.DataFrame(watch_app)


watface_app = search("Watch Face apps",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=50  # defaults to 30 (= Google's maximum)
)
watface_df = pd.DataFrame(watface_app)

# To combine all the dataframe into single dataframe
app_info_df = pd.concat([action_df, adven_df, arcade_df, art_df, auto_df, beauty_df,
                         board_df, books_df, business_df, card_df, casino_df, casual_df,
                         children_df, comics_df, comm_df, dating_df, edu_df, entern_df,
                         event_df, finance_df, food_df, google_df, health_df, house_df, 
                         library_df, lifestyle_df, loan_df, maps_df, medical_df, mugame_df, 
                         music_df, news_df, parent_df, personal_df, photo_df, prod_df,
                         public_df, puzzle_df, racing_df, roleplay_df, shop_df, simmu_df, 
                         social_df, sports_df, strategy_df, tools_df,  travel_df, trivia_df,
                         video_df, watch_df, watface_df, weather_df,  word_df], ignore_index=True)


len(app_info_df)        # Length of the data

# In the dataset, to convert the appId column into list format 
app_packages = app_info_df['appId'].tolist()
print(app_packages)
len(app_packages)

app_infos = []

for ap in tqdm(app_packages):
  info = app(ap, lang='en', country='us')
  del info['comments']
  app_infos.append(info)
  
# Converting app information data into DataFrame  
app_infos_df = pd.DataFrame(app_infos)

# Convert the dataframe into csv file
app_infos_df.to_csv('Appinfo.csv', index=None, header=True)



                                                  

