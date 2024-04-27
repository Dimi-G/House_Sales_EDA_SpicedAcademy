import pandas as pd
from haversine import haversine

'''
- Keeping the duplicated id values , they will be usefull for later analysis 
- Fix year rennovated 
- Convert to datetime and int accordingly
- Deduct NaN basement footage from rest area info
- Substitute the NaN renovated as 0 as 0 is anyway the majority of data
- Did not establish waterfront correlation and not relevant to client, so column is excluded
- View is also excluded as 19k of 21k data is 0 and not relevant to our client
- Adds lat_long tuple column and center_distance columns calculating each property distance from Seattle center. Unit is miles.
- Reordering columns according to our project priorities
'''
def wrangler(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['id', 'id.1', 'waterfront', 'view'])
    df.rename(columns={'date':'sold_date'}, inplace=True)
    df['sold_date'] = pd.to_datetime(df['sold_date'])
    df.yr_renovated = df.yr_renovated/10
    df['price_per_sqft'] = df['price']/df['sqft_living']
    df['sqft_basement'].fillna(df['sqft_living'] - df['sqft_above'], inplace=True)
    df['yr_renovated'] = df.yr_renovated.fillna(0)
    columns_to_int = ['price_per_sqft','sqft_living', 'sqft_lot', 'sqft_basement','sqft_living15', 'sqft_lot15', 'price', 'yr_renovated', 'sqft_above', 'bedrooms']
    df[columns_to_int] =df[columns_to_int].astype(int)
    seattle_center = (47.6018266,-122.3778238)
    df['lat_long'] = tuple(zip(df['lat'], df['long']))
    df['center_distance'] = df['lat_long'].apply( lambda row: haversine(seattle_center, row, unit='mi'))
    df= df[['price','price_per_sqft','sqft_living','grade','condition','center_distance','bedrooms', 'bathrooms', 'floors', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_living15', 'sqft_lot15','yr_built', 'yr_renovated', 'sold_date', 'zipcode', 'house_id']]
    return df
