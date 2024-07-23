import pandas as pd
from fuzzywuzzy import process
#rate_median
# Read the list of cities from a CSV file
cities_df = pd.read_csv('target_cities.csv')
target_cities = cities_df['citys'].tolist()  # Assuming the column name is 'city'

# Read the data with prices from another CSV file
prices_df = pd.read_csv("result\rate_mean\shab.csv")
# Define the mapping of old city names to new city names
city_mapping = {
    'سلمان شهر': 'متل قو',
    "متل قو(سلمان شهر)":'متل قو'
    ,'تنکابن': 'تنکابن/شهسوار',
    "تالش":"تالش/هشتپر","سرخ رود":"سرخرود",
    "سواد کوه":"سوادکوه","محمود آباد":"محمودآباد",
"بندر انزلی":"بندرانزلی",
    "هشتپر (تالش)":"تالش/هشتپر",
    "تالش":"تالش/هشتپر",
    "انزلی":"بندرانزلی",
    "شهسوار":'تنکابن/شهسوار'




    
}

#Replace city names in the prices data according to the mapping
prices_df['city'] = prices_df['city'].replace(city_mapping)

# Normalize the city names in the prices data
unique_cities = prices_df['city'].unique().tolist()
# Function to normalize city names using fuzzy matching
def normalize_city(city_name, city_list, threshold=80):
    match, score = process.extractOne(city_name, city_list)
    if score >= threshold:
        return match
    return None
# Map target cities to their normalized names
normalized_target_cities = [normalize_city(city, unique_cities) for city in target_cities]

# Filter out None values and convert to a set for faster lookup
normalized_target_cities = [city for city in normalized_target_cities if city is not None]

# Filter the data to include only the specified cities
filtered_df = prices_df[prices_df['city'].isin(target_cities)]

# Group by city and calculate the average price
average_prices = filtered_df.groupby('city')['overall_rate'].mean().reset_index()

# Sort the DataFrame by average price in descending order
average_prices_sorted = average_prices.sort_values(by='overall_rate', ascending=False)
missing_cities = set(target_cities) - set(filtered_df['city'].unique())

# Print the missing cities
missing_cities_df = pd.DataFrame(list(missing_cities), columns=['city'])
missing_cities_df.to_csv('missing_cities.csv', index=False)
# Save the result to a new CSV file
average_prices_sorted.to_csv('average_prices_for_cities.csv', index=False)
